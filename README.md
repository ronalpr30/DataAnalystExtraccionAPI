Partes Interesadas:

Analistas de datos interesados en eSports,organizadores de torneos y equipos competitivos,jugadores profesionales y entrenadores que buscan analizar el desempeño de sus rivales,aficionados y comunidad de Dota 2 que desean explorar el desarrollo de The International a lo largo de los años.

Descripción General de los Datos:

Origen de los datos: API de OpenDota (https://api.opendota.com/).

Años cubiertos: 2017 - 2024.

Torneos: The International y otros torneos relevantes.

Proceso de Extracción y Transformación de Datos:

Se creó un script en Python que utiliza la librería requests para conectarse a la API de OpenDota. A través de este script, se extraen datos de partidos y equipos de torneos específicos usando los identificadores de liga (league_id).

Pasos del Proceso:

Extracción de datos de las ligas seleccionadas usando requests.

Transformación de los datos crudos a un formato CSV.

Mapeo de IDs de equipos a nombres de equipos para facilitar la interpretación.

Almacenamiento de los datos en dota_league_data_selected.csv.

Limpieza y Procesamiento de Datos:

Una vez obtenido el archivo CSV, se realizó una limpieza de datos en Excel para garantizar la calidad del análisis:

Eliminación de registros duplicados o incompletos.

Conversión de la duración de partidos: De segundos a formato mm:ss.

Estandarización de nombres de equipos y ligas.

Creación de columnas adicionales para categorizar los partidos según su duración:

Turbo Game: Menos de 20 minutos.

Early Game: 20 a 40 minutos.

Mid Game: 40 a 60 minutos.

Late Game: Más de 60 minutos.

Modelamiento de Datos:

Se creó una estructura de datos que permite filtrar y analizar los partidos por:

Torneo.

Duración de la partida.

Equipo ganador (radiant o dire).

Marcador final.

Esto permite estudiar patrones de juego y evaluar el desempeño de los equipos a lo largo de los diferentes torneos.

Construcción del Dashboard y Reporte Final:

El dashboard fue diseñado en Excel usando tablas dinámicas y gráficos interactivos para mostrar:

Comparación de victorias entre equipos.

Distribución de duración de partidas.

Resultados por torneo y año.

Rendimiento de los equipos más destacados.

El reporte final incluye visualizaciones claras que permiten a las partes interesadas comprender de forma intuitiva el desempeño de los equipos y las tendencias de juego durante los torneos analizados.

Resultados Esperados:

Análisis detallado del desempeño de los equipos.

Identificación de patrones de juego y estrategias comunes.

Visualización de los torneos y sus resultados de manera organizada.

Información valiosa para equipos y organizadores de torneos.
![image](https://github.com/user-attachments/assets/fc7ffa03-08f3-4b7e-887d-1fd69a4af36c)
