PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
SELECT DISTINCT ?property
WHERE {
        ?person rdf:type <http://dbpedia.org/ontology/Politician> .
		?person ?property ?value .
	  }
	  
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
SELECT DISTINCT ?property
WHERE {
        ?person rdf:type <http://dbpedia.org/ontology/Politician> .
		?person ?property ?value .
		FILTER (?property != rdf:type)
	  }
	 
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
SELECT DISTINCT ?value
WHERE {
        ?person rdf:type <http://dbpedia.org/ontology/Politician> .
		?person ?property ?value .
		FILTER (?property != rdf:type)
	  }
	 
	 
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
SELECT DISTINCT ?property ?value
WHERE {
        ?person rdf:type <http://dbpedia.org/ontology/Politician> .
		?person ?property ?value .
		FILTER (?property != rdf:type)
	  }
	  
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
SELECT ?property (COUNT(DISTINCT ?value) as ?number)
WHERE {
        ?person rdf:type <http://dbpedia.org/ontology/Politician> .
		?person ?property ?value .
		FILTER (?property != rdf:type)
	  }
GROUP BY ?property