# Determinantes de la Desnutrición en Sudamérica (2018–2022)

## 1. 🎯 Introducción

La **desnutrición** es un fenómeno multidimensional que se manifiesta en diversas formas —desde la carencia calórica hasta deficiencias crónicas— y afecta especialmente a poblaciones vulnerables. No se trata solo de escasez de alimentos, sino de una compleja interacción entre pobreza, salud, educación, condiciones sanitarias, entorno rural, desigualdad y políticas públicas.

Este proyecto explora los **determinantes sociales, económicos, sanitarios y ambientales** que pueden estar vinculados con la persistencia de la desnutrición en **Sudamérica**, usando exclusivamente datos abiertos obtenidos de la **API oficial del Banco Mundial**, entre **2018 y 2022**.

## 2. 📌 Objetivo General

Analizar la evolución de la **prevalencia de desnutrición** en los países sudamericanos y examinar posibles determinantes estructurales que inciden en ella, mediante un enfoque comparativo, colaborativo y basado en evidencia pública del Banco Mundial.

—

## 3. 📖 Descripción del Indicador de Desnutrición (SN.ITK.DEFC.ZS)
El principal indicador utilizado en este proyecto para medir la desnutrición es:
>Prevalencia de desnutrición (% de la población)
>Código Banco Mundial: SN.ITK.DEFC.ZS
📌 **Definición técnica:**
Este indicador mide el **porcentaje de la población cuya ingesta calórica habitual es inferior a los niveles mínimos necesarios para mantener una vida activa y saludable**. No se refiere necesariamente a personas visiblemente desnutridas, sino a aquellas en riesgo de inseguridad alimentaria crónica.
🔎 **Detalles clave:**
El indicador es estimado por la FAO y difundido por el Banco Mundial.
Considera la disponibilidad de alimentos, distribución del ingreso y desigualdad alimentaria.
Se calcula usando modelos estadísticos basados en:
 - Producción y acceso a alimentos.
 - Precios.
 - Distribución del consumo calórico por país.
    -  Requerimientos energéticos mínimos por grupo poblacional.


📊**Interpretación:**
Un valor alto en este indicador **no significa que haya hambruna**, pero sí revela una **insuficiencia energética crónica a nivel poblacional**, que puede derivar en malnutrición, enfermedades y retraso en el desarrollo infantil


---

## 4. 🧩 Distribución del Trabajo por Subgrupo

A continuación, se detalla la división del análisis por áreas temáticas, cada una asignada a un integrante del equipo. Todos los subtemas se desarrollaron con datos del **World Bank** y bajo una estructura común de limpieza, visualización y análisis comparativo.

| Nº | Subtema | Indicador (Código WB) | Enfoque del análisis | Responsable |
|----|---------|------------------------|-----------------------|-------------|
| 1  | **Prevalencia de desnutrición** | `SN.ITK.DEFC.ZS` | Línea base: ¿Qué países tienen mayor desnutrición? Evolución 2018–2024 | Arturo |
| 2  | **PIB per cápita (USD)** | `NY.GDP.PCAP.CD` | ¿Existe relación entre riqueza y menor desnutrición? | Dhalia |
| 3  | **Gasto público en salud (% del PIB)** | `SH.XPD.CHEX.GD.ZS` | ¿A mayor inversión en salud, menos desnutrición? | Jorge |
| 4  | **Esperanza de vida al nacer** | `SP.DYN.LE00.IN` | Salud general como reflejo del bienestar nutricional | Eduardo |
| 5  | **Acceso a agua potable** | `SH.H2O.BASW.ZS` | Agua segura como condición básica para la nutrición | Maricielo |
| 6  | **Servicios básicos de saneamiento** | `SH.STA.BASS.ZS` | Infraestructura sanitaria como prevención de enfermedades | Jonnathan |
| 7  | **Educación secundaria femenina** | `SE.SEC.CUAT.LO.FE.ZS` | Madres con educación = mejores prácticas alimentarias | Elías |
| 8  | **Empleo agrícola (% total)** | `SL.AGR.EMPL.ZS` | El rol del agro en el sustento alimentario rural | Jhayro |
| 9  | **Población rural (% total)** | `SP.RUR.TOTL.ZS` | Brechas urbano-rurales en la malnutrición | David |
| 10 | **Tasa de natalidad (por 1000 hab.)** | `SP.DYN.CBRT.IN` | ¿Influye el tamaño de familia en la nutrición infantil? | Kemely |
| 11 | **Desigualdad de ingresos (GINI)** | `SI.POV.GINI` | ¿Existe relación entre desigualdad y desnutrición persistente? | Sean |
| 12 | **Visualización General / Dashboard** | Todos los anteriores | Integración visual y comparativa en tablero interactivo | Todos |

---

## 5. 🛠️ Metodología

- **Lenguaje**: Python (con `requests`, `pandas`, `plotly`, `BeautifulSoup`)
- **Datos**: Extraídos directamente de la API REST del World Bank.
- **Visualizaciones**: Gráficos de líneas, barras, boxplots, tablas estadísticas, y dashboard final.
- **Unidad geográfica**: Países sudamericanos.
- **Periodo de análisis**: 2018–2022 (últimos datos disponibles).

---

## 6. 🧠 Conclusión General

Los resultados muestran que **la desnutrición no puede ser explicada por un único factor**. A pesar de que algunos indicadores (como mayor PIB o mayor acceso al agua potable) se relacionan con mejoras nutricionales en ciertos países, **la interacción de múltiples determinantes** es lo que finalmente define la persistencia o reducción del problema.

El trabajo evidencia la necesidad de enfoques **multisectoriales y coordinados** en políticas públicas para atacar las verdaderas raíces de la desnutrición.

---

## 7. 📎 Recursos del Proyecto

- `/data`: Datos descargados y estructurados.
- `/code`: Scripts por subtema.
- `/graphics`: Visualizaciones estáticas y dinámicas.
- `/dashboard`: Tablero visual comparativo de todos los países.

---

## 8. 👥 Equipo de Trabajo

> Proyecto desarrollado por estudiantes de UNALM – Curso: Lenguaje de Programación II

- Maricielo
- Dhalia
- Kemely
- Eduardo
- Jorge
- Jonnathan
- Elías
- Jhayro
- David
- Arturo
- Sean

---

## 9. 🗂️ Licencia

Este proyecto utiliza datos públicos del **Banco Mundial**, que se encuentran bajo dominio abierto. El código fuente está disponible bajo licencia MIT.
https://data360.worldbank.org/en/api#/Data/get_data360_indicators 
https://data.worldbank.org/country/peru 
