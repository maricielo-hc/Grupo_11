# IMPORTACIONES DE LIBRERÍAS
import requests                    # Para conectarse a la API del Banco Mundial
import pandas as pd               # Para manejar y limpiar los datos
import matplotlib.pyplot as plt   # Para crear los gráficos
from bs4 import BeautifulSoup     # Por si la respuesta no es JSON válido

# OBTENER TODOS LOS PAÍSES DESDE LA API DEL BANCO MUNDIAL
url = "http://api.worldbank.org/v2/country?format=json&per_page=400"  # URL para obtener países
response = requests.get(url)          # Hace la solicitud GET
data = response.json()                # Convierte la respuesta en JSON

# Lista de países sudamericanos por nombre (usaremos esto para filtrar)
sudamerica_nombres = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
    "Paraguay", "Peru", "Uruguay", "Venezuela"
]

# Filtrar solo los países sudamericanos: {código: nombre}
paises = {} #Crea un diccionario vacío
for pais in data[1]: #Se recorre cada elemento de data
    if pais["name"] in sudamerica_nombres: #Verifica si el nombre del país está en la lista sudamerica_nombres
        paises[pais["id"]] = pais["name"] #Si el pais está se agrega al diccionario paises

# DEFINIR INDICADORES A CONSULTAR EN LA API 
indicadores = {
    "SP.DYN.CBRT.IN": "Tasa de Natalidad (por 1000 habitantes)",  # Nacimientos por cada 1000 personas
    "SN.ITK.DEFC.ZS": "Desnutrición (%)"                          # % de personas con desnutrición
}
fecha = "2000:2024"  # Rango de años a consultar

# FUNCIÓN PARA CONSULTAR LA API DEL BANCO MUNDIAL POR PAÍS E INDICADOR 
def obtener_datos(pais, indicador): #Se define la función con 2 argumentos
    # URL de consulta para país e indicador
    url = f"http://api.worldbank.org/v2/country/{pais}/indicator/{indicador}?format=json&date={fecha}&per_page=100"
    r = requests.get(url)  # Solicitud GET
    
    # Verificar si la respuesta es válida
    try:
        data = r.json()
    except:
        # Si no es JSON y es HTML. Se imprime aviso.
        soup = BeautifulSoup(r.text, "html.parser")#Se usa BeautifulSoup para analizar el texto de la respuesta
        print(f"Error en país {pais} - indicador {indicador}")#Se imprime mensaje de error
        return pd.DataFrame()#Se devuelve un Dataframe vacío
    
    # Si hay datos válidos , extraerlos
    if len(data) > 1:
        datos = [ #Se crea una lista llamada datos
            {
                "País": paises[pais], #Busca en el diccionario paises
                "Año": int(d["date"]), #el año del dato lo convierte a entero
                "Valor": d["value"], #el valor del inidicador en ese año
                "Indicador": indicadores[indicador] #Busca en el diccionario indicadores
            }
            for d in data[1] if d["value"] is not None #Recorre cada elemento de dentro de d[1]
        ]
        return pd.DataFrame(datos) #Convierte la lista datos en un DataFrame
    else:
        return pd.DataFrame()#Si no hay sufcientes elementos ,retorna el DataFrame vacío

# OBTENER DATOS DE TODOS LOS PAÍSES E INDICADORES
dfs = []  # Lista para guardar los dataframes
for codigo_pais in paises: #Recorre cada pais en el diccionario paises
    for indicador in indicadores: #Recorre cada indicador en el diccionario indicadores 
        df_temp = obtener_datos(codigo_pais, indicador)#Se llama a la función obtener_datos
        dfs.append(df_temp)#El dataFrame se agrega a la lista dfs

# UNIR TODOS LOS DATAFRAMES EN UNO SOLO
df = pd.concat(dfs, ignore_index=True)

# TRANSFORMAR LA TABLA DE FORMATO LARGO A FORMATO ANCHO 
# Esto pone cada indicador como columna
df_pivot = df.pivot_table(index=["Año", "País"], columns="Indicador", values="Valor").reset_index() #Crea un tabla dinámica
df_pivot = df_pivot.sort_values(["País", "Año"]) #Ordena el DataFrame final

# VISTA PREVIA DE DATOS COMBINADOS
print("Vista previa de los datos combinados:")
print(df_pivot.head())#Solo imprime los primeras 5 filas


# GRAFICAR POR PAÍS 
for pais in df_pivot["País"].unique(): #Recorre cada país en el dataDrame df_pivot
    datos_pais = df_pivot[df_pivot["País"] == pais]#Deja los registros solo del pais actual

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.set_title(f"{pais}: Tasa de Natalidad vs Desnutrición ") #Titulo del gráfico segun el psíd

    # EJE IZQUIERDO: TASA DE NATALIDAD 
    ax1.set_xlabel("Año") #Eje x
    ax1.set_ylabel("Tasa de Natalidad (por 1000 hab.)", color="tab:blue")#Eje y
    ax1.plot(
        datos_pais["Año"],
        datos_pais["Tasa de Natalidad (por 1000 habitantes)"],
        color="tab:blue",
        marker='o'
    )#Línea azul para la natalidad
    ax1.tick_params(axis="y", labelcolor="tab:blue") #Los números del eje y serán azules

    # EJE DERECHO: DESNUTRICIÓN 
    ax2 = ax1.twinx()  # Crea segundo eje Y
    ax2.set_ylabel("Desnutrición (%)", color="tab:red")#Etiqueta del eje de color rojo
    ax2.plot(
        datos_pais["Año"],
        datos_pais["Desnutrición (%)"],
        color="tab:red",
        marker='x'
    )#Línea roja para Desnutrición 
    ax2.tick_params(axis="y", labelcolor="tab:red")#Los números serán rojos

    # MOSTRAR EL GRÁFICO
    plt.grid(True)
    plt.tight_layout()#Ajusta el diseño del gráfico
    plt.show()#Muestra el gráfico
    input("Presiona ENTER para ver el siguiente gráfico...")#Pasa al sig. gráfico cuando el usuario presiona ENTER
