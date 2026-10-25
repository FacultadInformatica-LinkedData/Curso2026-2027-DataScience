{
  "@context": {
    "schema": "https://schema.org/",
    "name": "schema:name",
    "population": "schema:population",
    "country": "schema:containedInPlace",
    "universities": "schema:containsPlace",
    "acronym": "schema:alternateName"
  },

  "@id": "https://example.org/city/Madrid",
  "@type": "schema:City",

  "name": "Madrid",
  "population": 3416771,

  "country": {
    "@id": "https://example.org/country/Spain",
    "@type": "schema:Country",
    "name": "España"
  },

  "universities": [
    {
      "@id": "https://example.org/university/UPM",
      "@type": "schema:CollegeOrUniversity",
      "name": "Universidad Politécnica de Madrid",
      "acronym": "UPM"
    },
    {
      "@id": "https://example.org/university/UCM",
      "@type": "schema:CollegeOrUniversity",
      "name": "Universidad Complutense de Madrid",
      "acronym": "UCM"
    },
    {
      "@id": "https://example.org/university/UAM",
      "@type": "schema:CollegeOrUniversity",
      "name": "Universidad Autónoma de Madrid",
      "acronym": "UAM"
    },
    {
      "@id": "https://example.org/university/UC3M",
      "@type": "schema:CollegeOrUniversity",
      "name": "Universidad Carlos III de Madrid",
      "acronym": "UC3M"
    }
  ]
}
