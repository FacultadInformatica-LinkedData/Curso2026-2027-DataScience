
# Autoevaluación – Hands-On Assignment 2

Durante esta entrega hemos trabajado con datos abiertos sobre accidentes de tráfico en Madrid, aplicando los conceptos de RDF, OWL, naming strategy y serialización en Turtule. El objetivo era construir una ontología ligera que describiera los elementos principales del dataset y una instancia de ejemplo conforme a las buenas prácticas de modelado semántico.

## Archivos entregados

1. analysis.html
    - Descripción detallada del dataset 2025_Accidentalidad.csv
    - Analisis de la calidad de datos, los valores que faltaban y los tipos de datos
    - Licencia
    - Estrategia de nombrado

2. ontologia_accidentes_base.ttl
    - Archivo OWL, en formato .ttl.
    - Sigue la estrategia de nombrado que se dijo en el analysis.html.
    - Contiene al menos una clase, Accidente, y varias relacionadas como Persona y Vehiculo.
    - Incluye propiedades de objeto y de datos con sus dominios y rangos correctamente definidos.
    - Las clases comienzan con mayúscula y las propiedades con minúscula.
    - Escrito en español
    - Cumple las normas de serialización y estructura requeridas.
3. ontologia_accidentes.ttl
    - Archivo RDF, en formato .ttl.
    - Ejemplo con datos sacados del dataset 2025_Accidentalidad.csv
    - Incluye individuos para persona, vehículo, distrito, clima, lesión y rango de edad.
    - No redefine términos ontológicos, cumpliendo las normas de separación entre esquema y datos.
    


## Conclusión

El grupo ha cumplido los objetivos del Hands-On 2 de forma completa.
Además, hemos aprendido a estructurar datos abiertos en RDF, aplicar una naming strategy coherente y desarrollar una ontología válida en OWL.
