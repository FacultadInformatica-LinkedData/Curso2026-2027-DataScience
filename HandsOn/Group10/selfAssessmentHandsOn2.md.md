# Hands-on assignment 2 – Self assessment

**Group:** Group10  
**Dataset:** Relación de monumentos de Castilla y León (`relacion-monumentos.csv`)  
**Source:** https://datosabiertos.jcyl.es/web/jcyl/set/es/cultura-ocio/monumentos/1284325843131

## Checklist

### The “analysis.html” file:
- [x] Includes the potential license of the dataset to be generated
- [x] Includes the resource naming strategy

### The resource naming strategy:
- [x] Uses a domain that is not the one given by default in Protégé
- [x] Uses different paths for ontology resources (i.e., classes and properties) and individuals
- [x] Ensures that the paths for individuals of different classes are not the same
- [x] Defines individual URIs independently of class URIs

### The ontology file:
- [x] Uses the .ttl extension
- [x] Is serialized in the Turtle format
- [x] Follows the resource naming strategy
- [x] Contains at least one class
- [x] Contains at least one object property (where the value of the property is a resource)
- [x] Contains at least one datatype property (where the value of the property is a string literal, usually typed)
- [x] Defines the domain of all the properties (the origin of the property)
- [x] Defines the range of all the properties (the destination of the property)
- [x] Defines all class names starting with a capital letter
- [x] Defines all property names starting with a non-capital letter
- [x] Does not mix labels in different languages (e.g., Spanish and English)
- [x] Does not define multiple domains or multiple ranges in properties
- [x] Contains at least one class that will be used to link to other entities

## Comments on the self-assessment
- **Licensing (`analysis.html`):** Both the original dataset from *Junta de Castilla y León* and the generated RDF dataset use **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
- **Resource Naming Strategy (`analysis.html`):** Uses the custom base domain `http://www.monumentoscyl.es/`, separating ontology terms under `/ontology/monuments#` (hash pattern) from data individuals under `/resource/<class>/<id>` (slash pattern, e.g., `/resource/monument/{id}`, `/resource/province/{slug}`, `/resource/municipality/{slug}`).
- **Ontology (`ontology/monuments.ttl`):** All class names use `UpperCamelCase`, all property names use `lowerCamelCase`, every property defines a single `rdfs:domain` and a single `rdfs:range`, and all ontology labels are written consistently in English (`@en`) without mixing languages. Classes `mon:Province` and `mon:Municipality` (as well as `mon:Monument`) will be used to link entities to external knowledge graphs such as Wikidata and DBpedia.