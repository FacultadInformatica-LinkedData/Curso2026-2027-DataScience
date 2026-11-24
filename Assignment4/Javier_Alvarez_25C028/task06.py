# !pip install rdflib
# !pip install oeg-sw-class

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
    print(s, p, o)

# ==========================================
# TASK 6.0
# ==========================================
person = Namespace("http://oeg.fi.upm.es/resource/person/")
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
ontology = Namespace("http://oeg.fi.upm.es/def/people#")

g.namespace_manager.bind("person", person)
g.namespace_manager.bind("organization", organization)
g.namespace_manager.bind("ontology", ontology)

# ==========================================
# TASK 6.1
# ==========================================
classes_hierarchy = [
    (ontology.Person, None, "Person"),
    (ontology.Professor, ontology.Person, "Professor"),
    (ontology.FullProfessor, ontology.Professor, "FullProfessor"),
    (ontology.AssociateProfessor, ontology.Professor, "AssociateProfessor"),
    (ontology.AssistantProfessor, ontology.Professor, "AssistantProfessor"),
    (ontology.InterimAssociateProfessor, ontology.AssociateProfessor, "InterimAssociateProfessor")
]

for cls_uri, parent_cls, cls_label in classes_hierarchy:
    g.add((cls_uri, RDF.type, RDFS.Class))
    g.add((cls_uri, RDFS.label, Literal(cls_label, datatype=XSD.string)))
    if parent_cls is not None:
        g.add((cls_uri, RDFS.subClassOf, parent_cls))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_01(g)

# ==========================================
# TASK 6.2
# ==========================================
g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_02(g)

# ==========================================
# TASK 6.3
# ==========================================
properties_data = [
    (ontology.affiliatedWith, "affiliatedWith", ontology.Person, ontology.University),
    (ontology.hasColleague, "hasColleague", ontology.Person, ontology.Person),
    (ontology.hasName, "hasName", ontology.Person, RDFS.Literal),
    (ontology.hasHomePage, "hasHomePage", ontology.FullProfessor, RDFS.Literal)
]

for prop_uri, prop_label, dom, rng in properties_data:
    g.add((prop_uri, RDF.type, RDF.Property))
    g.add((prop_uri, RDFS.label, Literal(prop_label, datatype=XSD.string)))
    g.add((prop_uri, RDFS.domain, dom))
    g.add((prop_uri, RDFS.range, rng))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_03(g)

# ==========================================
# TASK 6.4
# ==========================================
university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.namespace_manager.bind("university", university)

# Individual: Juan
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Juan, RDFS.label, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))
g.add((person.Juan, ontology.hasColleague, person.Sven))

# Individual: Raul
g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Raul, RDFS.label, Literal("Raúl", datatype=XSD.string)))
g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))
g.add((person.Raul, ontology.hasColleague, person.Juan))

# Individual: Sven
g.add((person.Sven, RDFS.label, Literal("Sven", datatype=XSD.string)))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_04(g)

# ==========================================
# TASK 6.5
# ==========================================
foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.namespace_manager.bind("foaf", foaf)

juan_foaf_info = [
    (foaf.givenName, "Juan"),
    (foaf.familyName, "Cano de Benito"),
    (foaf.mbox, "juan.cano@upm.es")
]

for prop, val in juan_foaf_info:
    g.add((person.Juan, prop, Literal(val, datatype=XSD.string)))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_05(g)

# ==========================================
# TASK 6.6
# ==========================================
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))
g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_06(g)

# ==========================================
# TASK 6.7
# ==========================================
for uni in [university.UPM, university.Mannheim]:
    g.add((uni, RDF.type, ontology.University))

for s, p, o in g:
    print(s, p, o)

# Validation: Do not remove
r.validate_task_06_07(g)
r.save_report("_Task_06")