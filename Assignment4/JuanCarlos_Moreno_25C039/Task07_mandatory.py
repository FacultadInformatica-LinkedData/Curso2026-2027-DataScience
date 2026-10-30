github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report
# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage+"/rdf/data07.ttl", format="TTL")
report = Report()

#TODO
result = [] #list of tuples

for clase in g.subjects(RDF.type, RDFS.Class):
    superclases = list(g.objects(clase, RDFS.subClassOf))

    if len(superclases) > 0:
        for superclase in superclases:
            result.append((clase, superclase))
    else:
        result.append((clase, None))

# Visualize the results
for r in result:
  print(r)

## Validation: Do not remove
report.validate_07_1a(result)

#TODO
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?c ?sc WHERE {
?c rdf:type rdfs:Class .
    OPTIONAL {
        ?c rdfs:subClassOf ?sc .
    }
}
"""

for r in g.query(query):
  print(r.c, r.sc)

## Validation: Do not remove
report.validate_07_1b(query,g)

ns = Namespace("http://oeg.fi.upm.es/def/people#")

# variable to return
individuals = []

#TODO
clases_persona = {ns.Person}

cambio = True

while cambio:
    cambio = False

    for subclase, superclase in g.subject_objects(RDFS.subClassOf):
        if superclase in clases_persona and subclase not in clases_persona:
            clases_persona.add(subclase)
            cambio = True

for clase in clases_persona:
    for individuo in g.subjects(RDF.type, clase):
        if individuo not in individuals:
            individuals.append(individuo)

# visualize results
for i in individuals:
  print(i)

# validation. Do not remove
report.validate_07_02a(individuals)

#TODO

query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>

SELECT ?ind WHERE {
  ?ind rdf:type/rdfs:subClassOf* ns:Person .
}
"""

for r in g.query(query):
  print(r.ind)
# Visualize the results

## Validation: Do not remove
report.validate_07_02b(g, query)

#TODO
query =  """
PREFIX ns:  <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?name ?type
WHERE {
    ?persona ns:knows ns:Curry .
    ?persona rdfs:label ?name .
    ?persona rdf:type ?type .
}
"""

# Visualize the results
for r in g.query(query):
  print(r.name, r.type)


## Validation: Do not remove
report.validate_07_03(g, query)

#TODO
query =  """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?name
WHERE {
    ?entidad (
        ns:hasColleague/ns:ownsPet |
        ns:hasColleague/ns:hasColleague/ns:ownsPet
    ) ?perro .

    ?perro rdf:type ns:Animal .
    ?entidad rdfs:label ?name .
}
"""

# TO DO
# Visualize the results
for r in g.query(query):
  print(r.name)

## Validation: Do not remove
report.validate_07_04(g,query)
report.save_report("_Task_07")
