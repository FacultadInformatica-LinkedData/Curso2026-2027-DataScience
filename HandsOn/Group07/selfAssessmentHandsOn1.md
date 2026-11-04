# Autoevaluación de la práctica 1

**Grupo:** Group07 · **Proyecto:** AirMove Madrid

## Qué hemos hecho

- Elegimos los dominios de ciudad inteligente **medio ambiente (calidad del aire)** y **movilidad (tráfico rodado)** en Madrid.
- Seleccionamos cuatro conjuntos de datos CSV del portal de datos abiertos del Ayuntamiento de Madrid: calidad del aire horaria, estaciones de control de calidad del aire, histórico de tráfico y ubicación de los puntos de medida de tráfico.
- Comprobamos los requisitos R1–R6 de cada conjunto (ver `requirements/datasetRequirements.html`).
- Definimos la aplicación *AirMove Madrid*, con usuarios, requisitos y tres bocetos de interfaz (ver `requirements/applicationRequirements.html`).

## Comprobación de requisitos

| Requisito | ¿Cumplido? | Comentario |
|---|---|---|
| R1 dominio de ciudad inteligente | Sí | Medio ambiente y movilidad |
| R2 CSV | Sí | Todos los recursos seleccionados son ficheros CSV |
| R3 licencia abierta | Sí | CC BY 4.0 en las fichas de los cuatro conjuntos de datos (comprobado en datos.madrid.es) |
| R4 enlazable con entidades del mundo real | Sí | Estaciones y puntos de medida tienen coordenadas; se pueden enlazar distritos y calles |
| R5 documentación (opcional) | En gran parte | Hay descripción de campos del tráfico y de la calidad del aire |
| R6 varias fuentes (opcional) | Parcialmente | Dos sistemas municipales distintos, publicados en el mismo portal |

## Contribución de cada miembro

| Miembro | Tareas |
|---|---|
| Martina Vázquez | Búsqueda y selección de los datasets de calidad del aire(horarios y estaciones de control), descarga los CSV y comprueba R1 y R2 |
| Naia Loriente | Gestión del GitHub(fork, commits y pull request), organización de HandsOn Group07 y README |
| Aya El Hadari | Búsqueda y selección de los datasets de tráfico(histórico y ubicación de los puntos de medida), preparación de la muestra del histórico y descripción de sus campos  |
| Alejandra Calle | Redacción de "datasetRequirements.html": análisis de R1 a R6, identificación de licencias y de las entidades enlazables con otros datasets |
| Mar Salinas | Redacción de "applicationRequirements.html": usuarios, requisitos funcionales y no funcionales, preguntas de ejemplo y mock-ups de la interfaz |

## Dificultades y lecciones aprendidas

- Algunos ficheros son muy grandes (el histórico de tráfico de un mes ocupa cientos de MB), por lo que subimos una muestra.
- Los datos usan códigos (estación, magnitud) que hay que descifrar con la documentación.
- Los ficheros no usan la misma codificación: el de ubicación de puntos de medida está en ISO-8859-1 y los de calidad del aire en UTF-8

## Comprobación de la lista de entrega

| Fichero | Se comprueba que... | ¿Cumplido? |
|---|---|---|
| "README.md" | Incluye los nombres y usuarios de GitHub de todos los miembros | Sí |
| "csv/" | Contiene al menos un fichero CSV | Sí (cuatro ficheros) |
| "datasetRequirements.html" | Identifica la licencia de todos los datasets, las entidades enlazables con otros datasets y las entidades de otros datasets enlazables con las nuestras | Sí |
| "applicationRequirements.html" | Incluye una descripción de la interfaz de usuario | Sí |

## Autocalificación

7 / 10. Entregamos todos los documentos pedidos, con la aplicación bien definida y los mock-ups hechos.