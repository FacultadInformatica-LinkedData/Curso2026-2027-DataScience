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
    "ciudad": "https://schema.org/City",
    "poblacion": "https://schema.org/population",
    "pais": "https://schema.org/Country",
    "universidades": "https://schema.org/CollegeOrUniversity",
    "fullname": "https://schema.org/name",
    "acronym": "https://schema.org/alternateName"
  },
  "@type": "City",
  "ciudad": "Madrid",
  "poblacion": 5000000,
  "pais": "España",
  "universidades": [
    {
      "@type": "CollegeOrUniversity",
      "fullname": "Universidad Politécnica de Madrid",
      "acronym": "UPM"
    },
    {
      "@type": "CollegeOrUniversity",
      "fullname": "Universidad Complutense de Madrid",
      "acronym": "UCM"
    },
    {
      "@type": "CollegeOrUniversity",
      "fullname": "Universidad Carlos III de Madrid",
      "acronym": "UC3M"
    }
  ]
}
