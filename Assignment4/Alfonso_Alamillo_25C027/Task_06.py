from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from oeg_sw_class import Report
 
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()
 
ns = Namespace("http://mydomain.org#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)
 
prefijos = {
    "person": "http://oeg.fi.upm.es/resource/person/",
    "organization": "http://oeg.fi.upm.es/resource/organization/",
    "ontology": "http://oeg.fi.upm.es/def/people#",
}
for alias, uri in prefijos.items():
    g.bind(alias, Namespace(uri))
 
person = Namespace(prefijos["person"])
organization = Namespace(prefijos["organization"])
ontology = Namespace(prefijos["ontology"])
 
def texto(valor):
 
    return Literal(valor, datatype=XSD.string)
 
jerarquia = {
    "Person": None,
    "Professor": "Person",
    "FullProfessor": "Professor",
    "AssociateProfessor": "Professor",
    "AssistantProfessor": "Professor",
    "InterimAssociateProfessor": "AssociateProfessor",
}
 
for nombre, padre in jerarquia.items():
    clase = ontology[nombre]
    g.add((clase, RDF.type, RDFS.Class))
    g.add((clase, RDFS.label, texto(nombre)))
    if padre is not None:
        g.add((clase, RDFS.subClassOf, ontology[padre]))
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_01(g)
 
g += [
    (ontology.University, RDF.type, RDFS.Class),
    (ontology.University, RDFS.label, texto("University")),
]
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_02(g)
 
propiedades = [
    ("hasColleague", ontology.Person, ontology.Person),
    ("hasName", ontology.Person, RDFS.Literal),
    ("hasHomePage", ontology.FullProfessor, RDFS.Literal),
    ("affiliatedWith", ontology.Person, ontology.University),
]
 
for nombre, dominio, rango in propiedades:
    prop = ontology[nombre]
    g += [
        (prop, RDF.type, RDF.Property),
        (prop, RDFS.label, texto(nombre)),
        (prop, RDFS.domain, dominio),
        (prop, RDFS.range, rango),
    ]
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_03(g)
 
university = Namespace("http://oeg.fi.upm.es/resource/university/")
g.bind("university", university)
 
tipos = {
    person.Raul: ontology.FullProfessor,
    person.Juan: ontology.AssistantProfessor,
    person.Sven: ontology.Person,
    university.Mannheim: ontology.University,
}
for individuo, clase in tipos.items():
    g.add((individuo, RDF.type, clase))
 
etiquetas = {person.Raul: "Raúl", person.Juan: "Juan", person.Sven: "Sven"}
for individuo, etiqueta in etiquetas.items():
    g.add((individuo, RDFS.label, texto(etiqueta)))
 
g += [
    (person.Raul, ontology.hasColleague, person.Juan),
    (person.Juan, ontology.hasColleague, person.Sven),
    (person.Sven, ontology.affiliatedWith, university.Mannheim),
    (person.Raul, ontology.hasHomePage, texto("http://oeg.fi.upm.es")),
    (person.Juan, ontology.hasName, texto("Juan Cano de Benito")),
]
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_04(g)
 
foaf = Namespace("http://xmlns.com/foaf/0.1/")
g.bind("foaf", foaf)
 
datos_juan = {
    foaf.mbox: "juan.cano@upm.es",
    foaf.givenName: "Juan",
    foaf.familyName: "Cano de Benito",
}
for propiedad, valor in datos_juan.items():
    g.add((person.Juan, propiedad, texto(valor)))
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_05(g)
 
g += [
    (university.UPM, RDF.type, ontology.University),
    (university.UPM, RDFS.label, texto("UPM")),
    (person.Sven, RDF.type, ontology.InterimAssociateProfessor),
]
for profesor in (person.Juan, person.Raul):
    g.add((profesor, ontology.affiliatedWith, university.UPM))
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_06(g)
 
for uni in (university.UPM, university.Mannheim):
    g.add((uni, RDF.type, ontology.University))
 
for s, p, o in g:
  print(s,p,o)
 
r.validate_task_06_07(g)
r.save_report("_Task_06")
