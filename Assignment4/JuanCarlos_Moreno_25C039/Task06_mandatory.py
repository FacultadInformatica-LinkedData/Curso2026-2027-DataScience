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
  print(s,p,o)

# this task is validated in the next step
organization = Namespace("http://oeg.fi.upm.es/resource/organization/")
g.bind("organization", organization)

person = Namespace("http://oeg.fi.upm.es/resource/person/")
g.bind("person", person)

ontology = Namespace("http://oeg.fi.upm.es/def/people#")
g.bind("ontology", ontology)

g.add((ontology.Person, RDF.type, RDFS.Class))
g.add((ontology.Person, RDFS.label, Literal("Person", datatype=XSD.string)))

#TODO
# Crear las clases y añadir sus etiquetas

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

# Crear las relaciones de subclase

g.add((ontology.Professor, RDFS.subClassOf, ontology.Person))

g.add((ontology.FullProfessor, RDFS.subClassOf, ontology.Professor))

g.add((ontology.AssistantProfessor, RDFS.subClassOf, ontology.Professor))

g.add((ontology.AssociateProfessor, RDFS.subClassOf, ontology.Professor))

g.add((ontology.InterimAssociateProfessor, RDFS.subClassOf, ontology.AssociateProfessor))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_01(g)

#TODO
g.add((ontology.University, RDF.type, RDFS.Class))
g.add((ontology.University, RDFS.label, Literal("University", datatype=XSD.string)))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_02(g)

#TODO

# Propiedad hasName

g.add((ontology.hasName, RDF.type, RDF.Property))

g.add((ontology.hasName, RDFS.label, Literal("hasName", datatype=XSD.string)))

g.add((ontology.hasName, RDFS.domain, ontology.Person))

g.add((ontology.hasName, RDFS.range, RDFS.Literal))

# Propiedad hasColleague

g.add((ontology.hasColleague, RDF.type, RDF.Property))

g.add((ontology.hasColleague, RDFS.label, Literal("hasColleague", datatype=XSD.string)))

g.add((ontology.hasColleague, RDFS.domain, ontology.Person))

g.add((ontology.hasColleague, RDFS.range, ontology.Person))


# Propiedad hasHomePage

g.add((ontology.hasHomePage, RDF.type, RDF.Property))

g.add((ontology.hasHomePage, RDFS.label, Literal("hasHomePage", datatype=XSD.string)))

g.add((ontology.hasHomePage, RDFS.domain, ontology.FullProfessor))

g.add((ontology.hasHomePage, RDFS.range, RDFS.Literal))


# Propiedad affiliatedWith

g.add((ontology.affiliatedWith, RDF.type,RDF.Property))

g.add((ontology.affiliatedWith, RDFS.label, Literal("affiliatedWith", datatype=XSD.string)))

g.add((ontology.affiliatedWith, RDFS.domain, ontology.Person))

g.add((ontology.affiliatedWith, RDFS.range, ontology.University))


# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_03(g)

#TODO

# Etiqueta de Raul
g.add((person.Raul, RDFS.label, Literal("Raúl", datatype=XSD.string)))

# Raul es FullProfessor
g.add((person.Raul, RDF.type, ontology.FullProfessor))

# Página web de Raul
g.add((person.Raul, ontology.hasHomePage, Literal("http://oeg.fi.upm.es", datatype=XSD.string)))

# Raul tiene como colega a Juan
g.add((person.Raul, ontology.hasColleague, person.Juan))


# Etiqueta de Juan
g.add((person.Juan, RDFS.label, Literal("Juan", datatype=XSD.string)))

# Juan es AssistantProfessor
g.add((person.Juan, RDF.type, ontology.AssistantProfessor))

# Juan tiene como nombre Juan Cano de Benito
g.add((person.Juan, ontology.hasName, Literal("Juan Cano de Benito", datatype=XSD.string)))

# Juan tiene como colega a Sven
g.add((person.Juan, ontology.hasColleague, person.Sven))


# Etiqueta de Sven
g.add((person.Sven, RDFS.label, Literal("Sven", datatype=XSD.string)))



# Sven afiliado a la Universidad de Mannheim
# Tenemos que crear el Namespace de university, pues en el task 6.0 no hemos creado el de university
university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)

g.add((person.Sven, ontology.affiliatedWith, university.Mannheim))


# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_04(g)

foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)

#TODO

# Añadir el nombre de Juan
g.add((person.Juan, foaf.givenName, Literal("Juan", datatype=XSD.string)))

# Añadir los apellidos de Juan
g.add((person.Juan, foaf.familyName, Literal("Cano de Benito", datatype=XSD.string)))

# Añadir el correo electrónico de Juan
g.add((person.Juan, foaf.mbox, Literal("juan.cano@upm.es", datatype=XSD.string)))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_05(g)

#TODO
# Juan está afiliado a la UPM
g.add((person.Juan, ontology.affiliatedWith, university.UPM))

# Raul está afiliado a la UPM
g.add((person.Raul, ontology.affiliatedWith, university.UPM))

# Sven es InterimAssociateProfessor
g.add((person.Sven, RDF.type, ontology.InterimAssociateProfessor))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_06(g)

#TODO

# UPM es una University
g.add((university.UPM, RDF.type, ontology.University))

# Mannheim es una University
g.add((university.Mannheim, RDF.type, ontology.University))


# Visualize the results
for s, p, o in g:
  print(s,p,o)

#Validation: Do not remove
r.validate_task_06_07(g)
r.save_report("_Task_06")
