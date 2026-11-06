github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"
 
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report
 
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage+"/rdf/data07.ttl", format="TTL")
report = Report()
 
result = []
for clase in g.subjects(RDF.type, RDFS.Class):
 
    superclases = list(g.objects(clase, RDFS.subClassOf)) or [None]
    result.extend((clase, sc) for sc in superclases)
 
for r in result:
  print(r)
 
report.validate_07_1a(result)
 
query = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?c ?sc
WHERE {
  ?c a rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""
 
for r in g.query(query):
  print(r.c, r.sc)
 
report.validate_07_1b(query,g)
 
people = Namespace("http://oeg.fi.upm.es/def/people#")
 
individuals = []
 
clases_persona = set(g.transitive_subjects(RDFS.subClassOf, people.Person))
for clase in clases_persona:
    individuals.extend(g.subjects(RDF.type, clase))
 
for i in individuals:
  print(i)
 
report.validate_07_02a(individuals)
 
query = """
PREFIX rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX people: <http://oeg.fi.upm.es/def/people#>
SELECT ?ind
WHERE {
  ?ind rdf:type/rdfs:subClassOf* people:Person .
}
"""
 
for r in g.query(query):
  print(r.ind)
 
report.validate_07_02b(g, query)
 
query = """
PREFIX rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX people: <http://oeg.fi.upm.es/def/people#>
SELECT ?name ?type
WHERE {
  ?x people:knows people:Curry ;
     rdfs:label   ?name ;
     a            ?type .
}
"""
 
for r in g.query(query):
  print(r.name, r.type)
 
report.validate_07_03(g, query)
 
query = """
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
PREFIX people: <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?name
WHERE {
  ?x people:hasColleague/people:hasColleague?/people:ownsPet ?mascota ;
     rdfs:label ?name .
}
"""
 
for r in g.query(query):
  print(r.name)
 
report.validate_07_04(g,query)
report.save_report("_Task_07")
