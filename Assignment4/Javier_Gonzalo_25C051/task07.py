
# -*- coding: utf-8 -*-
# Task 07 - Querying RDF(s)

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

# Load RDF graph
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage + "/rdf/data07.ttl", format="TTL")
report = Report()


# TASK 7.1a - Classes and superclasses (RDFLib)

result = []

for clase in g.subjects(RDF.type, RDFS.Class):
    superior = g.value(clase, RDFS.subClassOf)
    result.append((clase, superior))

for r in result:
    print(r)

report.validate_07_1a(result)


# TASK 7.1b - Classes and superclasses (SPARQL)

query = """
SELECT ?c ?sc
WHERE {
    ?c rdf:type rdfs:Class .
    OPTIONAL {
        ?c rdfs:subClassOf ?sc .
    }
}
"""

for r in g.query(query):
    print(r.c, r.sc)

report.validate_07_1b(query, g)


# TASK 7.2a - Person individuals (RDFLib)

ns = Namespace("http://oeg.fi.upm.es/def/people#")

individuals = []
classes = [ns.Person]

# Include all subclass levels
for clase, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    classes.append(clase)

    for subclase, p, o in g.triples((None, RDFS.subClassOf, clase)):
        classes.append(subclase)

        for nivel3, p, o in g.triples((None, RDFS.subClassOf, subclase)):
            classes.append(nivel3)

for clase in classes:
    for individuo in g.subjects(RDF.type, clase):
        individuals.append(individuo)

for ind in individuals:
    print(ind)

report.validate_07_02a(individuals)


# TASK 7.2b - Person individuals (SPARQL)

query = """
SELECT ?ind
WHERE {
    ?ind rdf:type ?clase .
    ?clase rdfs:subClassOf*
        <http://oeg.fi.upm.es/def/people#Person> .
}
"""

for r in g.query(query):
    print(r.ind)

report.validate_07_02b(g, query)


# TASK 7.3 - People who know Curry

query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT ?name ?type
WHERE {
    ?person people:knows people:Curry .
    ?person rdfs:label ?name .
    ?person rdf:type ?type .
}
"""

for r in g.query(query):
    print(r.name, r.type)

report.validate_07_03(g, query)


# TASK 7.4 - Colleagues with pets

# Find entities connected to a pet owner through
# one or two colleague relationships

query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?name
WHERE {
    ?person rdfs:label ?name .
    ?person people:hasColleague{1,2} ?colleague .
    ?colleague people:ownsPet ?pet .
}
"""

for r in g.query(query):
    print(r.name)

report.validate_07_04(g, query)

# Save results
report.save_report("_Task_07")
