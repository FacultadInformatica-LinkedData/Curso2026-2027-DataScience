# Autoevaluación del Hands-on 2

Grupo 05 · Paseo Verde Madrid

- **Análisis y licencia.** `analysis.html` describe el esquema y los valores observados en los CSV de parques y jardines y de áreas caninas. Identifica al publicador, enlaza las fuentes y propone CC BY 4.0 para el conjunto RDF.
- **Estrategia de URI.** Se ha documentado una base provisional distinta de la que propone Protégé por defecto. Los términos de la ontología usan fragmentos y los individuos usan rutas distintas para parques, áreas caninas y distritos. Las URI de las propiedades son independientes de las URI de las clases.
- **Ontología.** `ontology/paseoverde.ttl` define cuatro clases, una propiedad de objeto y una propiedad de datos. Cada propiedad tiene un dominio y un rango. Las clases empiezan con mayúscula, las propiedades con minúscula y todas las etiquetas están en español. La clase `Distrito` permite enlazar instalaciones con su distrito.
- **Ejemplo.** `ontology/paseoverde-example.ttl` sigue la estrategia de URI y contiene instancias. Representa un parque y un área canina que enlazan al distrito de Barajas.
- **Validación.** RDFLib leyó ambos archivos Turtle sin errores: 20 triples en la ontología y 8 en el ejemplo.
