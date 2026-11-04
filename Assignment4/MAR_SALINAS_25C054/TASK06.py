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
