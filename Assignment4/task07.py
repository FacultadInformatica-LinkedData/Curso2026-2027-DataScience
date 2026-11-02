# -*- coding: utf-8 -*-
# !pip install rdflib
# !pip install oeg-sw-class

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

g = Graph()
g.namespace_manager.bind('ns', Namespace('http://somewhere#'), override=False)
g.parse(github_storage + '/rdf/data07.ttl', format='turtle')
report = Report()

# 7.1a: clases y sus superclases
result = []
for clase in g.subjects(RDF.type, RDFS.Class):
    padres = list(g.objects(clase, RDFS.subClassOf))
    if padres:
        for padre in padres:
            result.append((clase, padre))
    else:
        result.append((clase, None))

for fila in result:
    print(fila)
report.validate_07_1a(result)

# 7.1b: lo mismo con SPARQL
query = """
SELECT ?c ?sc WHERE {
    ?c a rdfs:Class .
    OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""
for fila in g.query(query):
    print(fila.c, fila.sc)
report.validate_07_1b(query, g)

# 7.2a: personas incluyendo subclases
ns = Namespace('http://oeg.fi.upm.es/def/people#')
individuals = []
for clase in g.transitive_subjects(RDFS.subClassOf, ns.Person):
    for individuo in g.subjects(RDF.type, clase):
        if individuo not in individuals:
            individuals.append(individuo)

for individuo in individuals:
    print(individuo)
report.validate_07_02a(individuals)

# 7.2b: personas con SPARQL
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?ind WHERE {
    ?ind a ?class .
    ?class rdfs:subClassOf* ns:Person .
}
"""
for fila in g.query(query):
    print(fila.ind)
report.validate_07_02b(g, query)

# 7.3: personas que conocen a Curry
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT ?name ?type WHERE {
    ?x ns:knows ns:Curry .
    ?x rdfs:label ?name .
    ?x a ?type .
}
"""
for fila in g.query(query):
    print(fila.name, fila.type)
report.validate_07_03(g, query)

# 7.4: compañeros a uno o dos pasos que tienen perro
query = """
PREFIX ns: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name WHERE {
    ?x rdfs:label ?name .
    ?x ns:hasColleague/ns:hasColleague? ?colleague .
    ?colleague ns:ownsPet ?pet .
    ?pet a ns:Dog .
}
"""
for fila in g.query(query):
    print(fila.name)
report.validate_07_04(g, query)
report.save_report('_Task_07')
