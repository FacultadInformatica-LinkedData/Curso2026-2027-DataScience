# !pip install rdflib
# !pip install oeg-sw-class

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2026-2027-Datascience/refs/heads/master/Assignment4/course_materials"

# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage + "/rdf/data07.ttl", format="TTL")
report = Report()

# ==========================================
# TASK 7.1a
# ==========================================
result = []

for cls_uri in g.subjects(RDF.type, RDFS.Class):
    parent = g.value(subject=cls_uri, predicate=RDFS.subClassOf)
    result.append((cls_uri, parent))

for r in result:
    print(r)

## Validation: Do not remove
report.validate_07_1a(result)

# ==========================================
# TASK 7.1b
# ==========================================
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?c ?sc
WHERE {
  ?c a rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
"""

for r in g.query(query):
    print(r.c, r.sc)

## Validation: Do not remove
report.validate_07_1b(query, g)

# ==========================================
# TASK 7.2a
# ==========================================
ns = Namespace("http://oeg.fi.upm.es/def/people#")
individuals = []

target_classes = set(g.transitive_subjects(RDFS.subClassOf, ns.Person))

for target_cls in target_classes:
    for ind_uri in g.subjects(RDF.type, target_cls):
        if ind_uri not in individuals:
            individuals.append(ind_uri)

for i in individuals:
    print(i)

# validation. Do not remove
report.validate_07_02a(individuals)

# ==========================================
# TASK 7.2b
# ==========================================
query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX people: <http://oeg.fi.upm.es/def/people#>

SELECT DISTINCT ?ind
WHERE {
  ?subClass rdfs:subClassOf* people:Person .
  ?ind a ?subClass .
}
"""

for r in g.query(query):
    print(r.ind)

## Validation: Do not remove
report.validate_07_02b(g, query)

# ==========================================
# TASK 7.3
# ==========================================
query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?name ?type
WHERE {
  ?s people:knows people:Curry ;
     rdfs:label ?name ;
     rdf:type ?type .
}
"""

for r in g.query(query):
    print(r.name, r.type)

## Validation: Do not remove
report.validate_07_03(g, query)

# ==========================================
# TASK 7.4
# ==========================================
query = """
PREFIX people: <http://oeg.fi.upm.es/def/people#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?name
WHERE {
  {
    ?s people:hasColleague ?col1 .
    ?col1 people:ownsPet ?pet .
  }
  UNION
  {
    ?s people:hasColleague ?col1 .
    ?col1 people:hasColleague ?col2 .
    ?col2 people:ownsPet ?pet .
  }
  ?pet a people:Animal .
  ?s rdfs:label ?name .
}
"""

for r in g.query(query):
    print(r.name)

## Validation: Do not remove
report.validate_07_04(g, query)
report.save_report("_Task_07")