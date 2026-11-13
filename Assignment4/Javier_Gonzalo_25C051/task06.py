
# -*- coding: utf-8 -*-
# Assignment 4 - Task 06: Modifying RDF(s)

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

# Initial configuration
g = Graph()
g.namespace_manager.bind("ns", Namespace("http://somewhere#"), override=False)
r = Report()

ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))

for s, p, o in g:
    print(s, p, o)


# TASK 6.0 - Define namespaces

person = Namespace("http://oeg.fi.upm.es/resource/person/")
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
ontology = Namespace("http://oeg.fi.upm.es/def/people#")

g.bind("person", person)
g.bind("organization", organization)
g.bind("ontology", ontology)


# TASK 6.1 - Class taxonomy

# Create the classes and their labels
classes = [
    ontology.Person,
    ontology.Professor,
    ontology.FullProfessor,
    ontology.AssistantProfessor,
    ontology.AssociateProfessor,
    ontology.InterimAssociateProfessor
]

for cls in classes:
    g.add((cls, RDF.type, RDFS.Class))
    g.add((cls, RDFS.label,
           Literal(str(cls).split("#")[-1], datatype=XSD.string)))

# Define the class hierarchy
g.add((ontology.Professor, RDFS.subClassOf, ontology.Person))
g.add((ontology.FullProfessor, RDFS.subClassOf, ontology.Professor))
g.add((ontology.AssistantProfessor, RDFS.subClassOf, ontology.Professor))
g.add((ontology.AssociateProfessor, RDFS.subClassOf, ontology.Professor))
g.add((ontology.InterimAssociateProfessor, RDFS.subClassOf,
       ontology.AssociateProfessor))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_01(g)


# TASK 6.2 - University class

g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label,
       Literal("University", datatype=XSD.string)))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_02(g)


# TASK 6.3 - Properties, domains and ranges

# Declare RDF properties
properties = [
    ontology.hasName,
    ontology.hasColleague,
    ontology.hasHomePage,
    ontology.affiliatedWith
]

for prop in properties:
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label,
           Literal(str(prop).split("#")[-1], datatype=XSD.string)))

# Set domains
g.add((ontology.hasName, RDFS.domain, ontology.Person))
g.add((ontology.hasColleague, RDFS.domain, ontology.Person))
g.add((ontology.hasHomePage, RDFS.domain, ontology.FullProfessor))
g.add((ontology.affiliatedWith, RDFS.domain, ontology.Person))

# Set ranges
g.add((ontology.hasName, RDFS.range, RDFS.Literal))
g.add((ontology.hasColleague, RDFS.range, ontology.Person))
g.add((ontology.hasHomePage, RDFS.range, RDFS.Literal))
g.add((ontology.affiliatedWith, RDFS.range, ontology.University))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_03(g)


# TASK 6.4 - Create individuals

university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)

# Assign individual types
g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Sven, RDF.type, ontology.Person))
g.add((university.Mannheim, RDF.type, ontology.University))

# Add labels
g.add((person.Raul, RDFS.label, Literal("Raúl", datatype=XSD.string)))
g.add((person.Juan, RDFS.label, Literal("Juan", datatype=XSD.string)))
g.add((person.Sven, RDFS.label, Literal("Sven", datatype=XSD.string)))

# Relationships between individuals
g.add((person.Raul, ontology.hasColleague, person.Juan))
g.add((person.Juan, ontology.hasColleague, person.Sven))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))

# Personal information
g.add((person.Raul, ontology.hasHomePage,
       Literal("http://oeg.fi.upm.es", datatype=XSD.string)))

g.add((person.Juan, ontology.hasName,
       Literal("Juan Cano de Benito", datatype=XSD.string)))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_04(g)


# TASK 6.5 - FOAF information

foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)

# Juan's email and full name
g.add((person.Juan, foaf.mbox,
       Literal("juan.cano@upm.es", datatype=XSD.string)))

g.add((person.Juan, foaf.givenName,
       Literal("Juan", datatype=XSD.string)))

g.add((person.Juan, foaf.familyName,
       Literal("Cano de Benito", datatype=XSD.string)))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_05(g)


# TASK 6.6 - University affiliations

# Create the UPM individual
g.add((university.UPM, RDF.type, ontology.University))
g.add((university.UPM, RDFS.label,
       Literal("UPM", datatype=XSD.string)))

# Connect professors with UPM
g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))

# Update Sven's type
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_06(g)


# TASK 6.7 - University types

g.add((university.UPM, RDF.type, ontology.University))
g.add((university.Mannheim, RDF.type, ontology.University))

for s, p, o in g:
    print(s, p, o)

r.validate_task_06_07(g)

# Save validation report
r.save_report("_Task_06")
