# -*- coding: utf-8 -*-

# !pip install rdflib
# !pip install oeg-sw-class

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

# Grafo y espacios de nombres
g = Graph()
g.namespace_manager.bind('ns', Namespace('http://somewhere#'), override=False)
r = Report()

ns = Namespace('http://mydomain.org#')
g.add((ns.Researcher, RDF.type, RDFS.Class))

# 6.0 - Prefijos
organization = Namespace('http://oeg.fi.upm.es/resource/organization/')
person = Namespace('http://oeg.fi.upm.es/resource/person/')
ontology = Namespace('http://oeg.fi.upm.es/def/people#')
university = Namespace('http://oeg.fi.upm.es/resource/university/')

g.bind('organization', organization)
g.bind('person', person)
g.bind('ontology', ontology)
g.bind('university', university)

# 6.1 - Clases y subclases
g.add((ontology.Person, RDF.type, RDFS.Class))
g.add((ontology.Person, RDFS.label, Literal('Person', datatype=XSD.string)))

classes = [
    ('Professor', 'Person'),
    ('FullProfessor', 'Professor'),
    ('AssistantProfessor', 'Professor'),
    ('AssociateProfessor', 'Professor'),
    ('InterimAssociateProfessor', 'AssociateProfessor')
]

for child, parent in classes:
    g.add((ontology[child], RDF.type, RDFS.Class))
    g.add((ontology[child], RDFS.label, Literal(child, datatype=XSD.string)))
    g.add((ontology[child], RDFS.subClassOf, ontology[parent]))

r.validate_task_06_01(g)

# 6.2 - Universidad
g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal('University', datatype=XSD.string)))
r.validate_task_06_02(g)

# 6.3 - Propiedades, dominios y rangos
properties = [
    ('hasName', ontology.Person, RDFS.Literal),
    ('hasColleague', ontology.Person, ontology.Person),
    ('hasHomePage', ontology.FullProfessor, RDFS.Literal),
    ('affiliatedWith', ontology.Person, ontology.University)
]

for name, domain, range_ in properties:
    g.add((ontology[name], RDF.type, RDF.Property))
    g.add((ontology[name], RDFS.label, Literal(name, datatype=XSD.string)))
    g.add((ontology[name], RDFS.domain, domain))
    g.add((ontology[name], RDFS.range, range_))

r.validate_task_06_03(g)

# 6.4 - Personas y relaciones
g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Raul, ontology.hasColleague, person.Juan))
g.add((person.Juan, ontology.hasColleague, person.Sven))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))
g.add((person.Raul, ontology.hasHomePage, Literal('http://oeg.fi.upm.es', datatype=XSD.string)))
g.add((person.Juan, ontology.hasName, Literal('Juan Cano de Benito', datatype=XSD.string)))

for individual, label in [(person.Raul, 'Raúl'), (person.Juan, 'Juan'), (person.Sven, 'Sven')]:
    g.add((individual, RDFS.label, Literal(label, datatype=XSD.string)))

r.validate_task_06_04(g)

# 6.5 - Datos de Juan con FOAF
foaf = Namespace('http://xmlns.com/foaf/0.1/')
g.bind('foaf', foaf)
g.add((person.Juan, foaf.mbox, Literal('juan.cano@upm.es', datatype=XSD.string)))
g.add((person.Juan, foaf.givenName, Literal('Juan', datatype=XSD.string)))
g.add((person.Juan, foaf.familyName, Literal('Cano de Benito', datatype=XSD.string)))
r.validate_task_06_05(g)

# 6.6 - Afiliaciones y tipo de Sven
g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))
r.validate_task_06_06(g)

# 6.7 - Tipos de universidades
g.add((university.UPM, RDF.type, ontology.University))
g.add((university.Mannheim, RDF.type, ontology.University))
r.validate_task_06_07(g)

r.save_report('_Task_06')
