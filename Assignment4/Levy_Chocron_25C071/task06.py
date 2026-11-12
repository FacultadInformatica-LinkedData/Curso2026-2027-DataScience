# Task 06: Modifying RDF(s)

from rdflib import Graph, Namespace, Literal, URIRef, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report

# Do not change the name of the variables
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

# ejemplo del notebook
ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))


# Task 6.0: prefijos
person = Namespace("http://oeg.fi.upm.es/resource/person/")
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
ontology = Namespace("http://oeg.fi.upm.es/def/people#")

g.bind("person", person)
g.bind("organization", organization)
g.bind("ontology", ontology)


# Task 6.1: clases del diagrama
# el label igual que en el diagrama, sin idioma y como xsd:string
g.add((ontology.Person, RDF.type, RDFS.Class))
g.add((ontology.Person, RDFS.label, Literal("Person", datatype=XSD.string)))

g.add((ontology.Professor, RDF.type, RDFS.Class))
g.add((ontology.Professor, RDFS.label, Literal("Professor", datatype=XSD.string)))

g.add((ontology.FullProfessor, RDF.type, RDFS.Class))
g.add((ontology.FullProfessor, RDFS.label, Literal("FullProfessor", datatype=XSD.string)))

g.add((ontology.AssistantProfessor, RDF.type, RDFS.Class))
g.add((ontology.AssistantProfessor, RDFS.label, Literal("AssistantProfessor", datatype=XSD.string)))

g.add((ontology.AssociateProfessor, RDF.type, RDFS.Class))
g.add((ontology.AssociateProfessor, RDFS.label, Literal("AssociateProfessor", datatype=XSD.string)))

g.add((ontology.InterimAssociateProfessor, RDF.type, RDFS.Class))
g.add((ontology.InterimAssociateProfessor, RDFS.label, Literal("InterimAssociateProfessor", datatype=XSD.string)))

# subclases
g.add((ontology.Professor, RDFS.subClassOf, ontology.Person))
g.add((ontology.FullProfessor, RDFS.subClassOf, ontology.Professor))
g.add((ontology.AssistantProfessor, RDFS.subClassOf, ontology.Professor))
g.add((ontology.AssociateProfessor, RDFS.subClassOf, ontology.Professor))
g.add((ontology.InterimAssociateProfessor, RDFS.subClassOf, ontology.AssociateProfessor))

# Validation: Do not remove
r.validate_task_06_01(g)


# Task 6.2: University
g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))

# Validation: Do not remove
r.validate_task_06_02(g)


# Task 6.3: propiedades con domain y range
# las que no tienen range en el diagrama llevan rdfs:Literal
g.add((ontology.hasName, RDF.type, RDF.Property))
g.add((ontology.hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))
g.add((ontology.hasName, RDFS.domain, ontology.Person))
g.add((ontology.hasName, RDFS.range, RDFS.Literal))

g.add((ontology.hasColleague, RDF.type, RDF.Property))
g.add((ontology.hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))
g.add((ontology.hasColleague, RDFS.domain, ontology.Person))
g.add((ontology.hasColleague, RDFS.range, ontology.Person))

g.add((ontology.hasHomePage, RDF.type, RDF.Property))
g.add((ontology.hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))
g.add((ontology.hasHomePage, RDFS.domain, ontology.FullProfessor))
g.add((ontology.hasHomePage, RDFS.range, RDFS.Literal))

# el range University lo dice el enunciado
g.add((ontology.affiliatedWith, RDF.type, RDF.Property))
g.add((ontology.affiliatedWith, RDFS.label, Literal("affiliatedWith", datatype=XSD.string)))
g.add((ontology.affiliatedWith, RDFS.domain, ontology.Person))
g.add((ontology.affiliatedWith, RDFS.range, ontology.University))

# Validation: Do not remove
r.validate_task_06_03(g)


# Task 6.4: individuos
# university no estaba en la 6.0 pero lo necesito para Mannheim (y para la 6.6 y 6.7)
university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)

g.add((person.Raul, RDF.type, ontology.FullProfessor))
g.add((person.Raul, RDFS.label, Literal("Raúl", datatype=XSD.string)))
g.add((person.Raul, ontology.hasColleague, person.Juan))
g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))

g.add((person.Juan, RDF.type, ontology.AssistantProfessor))
g.add((person.Juan, RDFS.label, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, ontology.hasColleague, person.Sven))
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))

# a Sven todavía no le pongo tipo, es en la 6.6
g.add((person.Sven, RDFS.label, Literal("Sven", datatype=XSD.string)))
g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))

# Validation: Do not remove
r.validate_task_06_04(g)


# Task 6.5: email, nombre y apellidos de Juan
# los namespaces se definen a mano, no se importan
foaf = Namespace("http://xmlns.com/foaf/0.1/")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
g.bind("foaf", foaf)
g.bind("vcard", vcard)

# estas son las que mira el validador
g.add((person.Juan, foaf.givenName, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, foaf.familyName, Literal("Cano de Benito", datatype=XSD.string)))
g.add((person.Juan, foaf.mbox, URIRef("mailto:juan.cano@upm.es")))

# y estas son las del example4.rdf, que es lo que dice el enunciado
g.add((person.Juan, vcard.Given, Literal("Juan", datatype=XSD.string)))
g.add((person.Juan, vcard.Family, Literal("Cano de Benito", datatype=XSD.string)))
g.add((person.Juan, foaf.email, Literal("juan.cano@upm.es", datatype=XSD.string)))

# Validation: Do not remove
r.validate_task_06_05(g)


# Task 6.6
g.add((person.Juan, ontology.affiliatedWith, university.UPM))
g.add((person.Raul, ontology.affiliatedWith, university.UPM))
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))

# Validation: Do not remove
r.validate_task_06_06(g)


# Task 6.7
g.add((university.UPM, RDF.type, ontology.University))
g.add((university.Mannheim, RDF.type, ontology.University))

# Validation: Do not remove
r.validate_task_06_07(g)
r.save_report("_Task_06")

print(g.serialize(format="turtle"))
