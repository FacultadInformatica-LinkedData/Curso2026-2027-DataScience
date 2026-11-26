Placeholder to generate the folder
JSON
{
	"ciudad":"Madrid",
	"población":5000000,
	"país":"España",
	"universidades":[
		{
		 "fullname":"universidad politécnica de Madrid",
		 "acronym":"UPM"
		},
		{
		 "fullname":"universidad complutense de Madrid",
		 "acronym":"UCM"
		},
		{
		 "fullname":"universidad Carlos III de Madrid",
		 "acronym":"UC3M"
		}

	]
}



JSON-LD
{
  "@context": {
    "schema": "https://schema.org/",
    "ciudad": "schema:City",
    "poblacion": "schema:population",
    "pais": "schema:Country",
    "universidades": "schema:CollegeOrUniversity",
    "fullname": "schema:name",
    "acronym": "schema:alternateName"
  },

  "@id": "https://www.wikidata.org/entity/Q2807",
  "@type": "schema:City",

  "ciudad": "Madrid",
  "poblacion": 5000000,
  "pais": "España",

  "universidades": [
    {
      "@id": "https://www.upm.es/",
      "@type": "schema:CollegeOrUniversity",
      "fullname": "Universidad Politécnica de Madrid",
      "acronym": "UPM"
    },
    {
      "@id": "https://www.ucm.es/",
      "@type": "schema:CollegeOrUniversity",
      "fullname": "Universidad Complutense de Madrid",
      "acronym": "UCM"
    },
    {
      "@id": "https://www.uc3m.es/",
      "@type": "schema:CollegeOrUniversity",
      "fullname": "Universidad Carlos III de Madrid",
      "acronym": "UC3M"
    }
  ]
}
