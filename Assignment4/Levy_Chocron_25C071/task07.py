# Task 07: Querying RDF(s)

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage + "/rdf/data07.ttl", format="TTL")
report = Report()


# TASK 7.1a: cada clase con su superclase (RDFLib)
result = []  # list of tuples

for clase, p, o in g.triples((None, RDF.type, RDFS.Class)):
    # si no tiene superclase, g.value devuelve None, que es lo que pide
    superclase = g.value(clase, RDFS.subClassOf)
    result.append((clase, superclase))

# Visualize the results
for r in result:
    print(r)

# Validation: Do not remove
report.validate_07_1a(result)


# TASK 7.1b: lo mismo en SPARQL
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?c ?sc
WHERE {
  ?c rdf:type rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc }
}
"""

# Visualize the results
for r in g.query(query):
    print(r.c, r.sc)

# Validation: Do not remove
report.validate_07_1b(query, g)


# TASK 7.2a: individuos de Person incluyendo los de sus subclases (RDFLib)
ns = Namespace("http://oeg.fi.upm.es/def/people#")

# variable to return
individuals = []

# RDFLib no hace inferencia de RDFS, así que bajo por la jerarquía yo mismo
# (son 3 niveles: Person > Professor > AssociateProfessor > InterimAssociateProfessor)
clases_persona = [ns.Person]
for clase1 in g.subjects(RDFS.subClassOf, ns.Person):
    clases_persona.append(clase1)
    for clase2 in g.subjects(RDFS.subClassOf, clase1):
        clases_persona.append(clase2)
        for clase3 in g.subjects(RDFS.subClassOf, clase2):
            clases_persona.append(clase3)

for clase in clases_persona:
    for individuo in g.subjects(RDF.type, clase):
        if individuo not in individuals:
            individuals.append(individuo)

# visualize results
for i in individuals:
    print(i)

# Validation: Do not remove
report.validate_07_02a(individuals)


# TASK 7.2b: lo mismo en SPARQL
# un UNION con Person y con cada una de sus subclases
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?ind
WHERE {
  { ?ind rdf:type ns:Person }
  UNION { ?ind rdf:type ns:Professor }
  UNION { ?ind rdf:type ns:Student }
  UNION { ?ind rdf:type ns:FullProfessor }
  UNION { ?ind rdf:type ns:AssistantProfessor }
  UNION { ?ind rdf:type ns:AssociateProfessor }
  UNION { ?ind rdf:type ns:InterimAssociateProfessor }
}
"""

# Visualize the results
for r in g.query(query):
    print(r.ind)

# Validation: Do not remove
report.validate_07_02b(g, query)


# TASK 7.3: nombre y tipo de los que conocen a Curry
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?name ?type
WHERE {
  ?x ns:knows ns:Curry .
  ?x rdfs:label ?name .
  ?x rdf:type ?type .
}
"""

# Visualize the results
for r in g.query(query):
    print(r.name, r.type)

# Validation: Do not remove
report.validate_07_03(g, query)


# Task 7.4: compañero con perro, o compañero de un compañero con perro
# el perro es un ns:Animal que alguien tiene como mascota (ns:ownsPet)
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?name
WHERE {
  ?x rdfs:label ?name .
  {
    # caso 1: un compañero con perro
    ?x ns:hasColleague ?c1 .
    ?c1 ns:ownsPet ?perro .
  }
  UNION
  {
    # caso 2: un compañero de un compañero con perro
    ?x ns:hasColleague ?c1 .
    ?c1 ns:hasColleague ?c2 .
    ?c2 ns:ownsPet ?perro .
  }
  ?perro rdf:type ns:Animal .
}
"""

# Visualize the results
for r in g.query(query):
    print(r.name)

# Validation: Do not remove
report.validate_07_04(g, query)
report.save_report("_Task_07")
