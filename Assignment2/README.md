{
  "@context": {
    "ciudad": "https://schema.org/City",
    "nombre": "https://schema.org/name",
    "población": "https://schema.org/population",
    "país": "https://schema.org/country",
    "universidades": "https://schema.org/University",
    "universidad": "https://schema.org/CollegeOrUniversity",
    "Nombre": "https://schema.org/name",
    "Acrónimo": "https://schema.org/alternateName"
  },
  "@id": "https://example.org/city/madrid",
  "@type": "ciudad",
  "nombre": "Madrid",
  "población": 4000000,
  "país": {
    "@id": "https://example.org/country/spain",
	"@type": "https://schema.org/Country",
    "nombre": "España"
  },
  "universidades": [
    {
      "@id": "https://example.org/university/ucm",
	  "@type": "universidad",
      "Nombre": "Universidad Complutense de Madrid",
      "Acrónimo": "UCM"
    },
    {
      "@id": "https://example.org/university/uam",
	  "@type": "universidad",
      "Nombre": "Universidad Autónoma de Madrid",
      "Acrónimo": "UAM"
    },
    {
      "@id": "https://example.org/university/upm",
	  "@type": "universidad",
      "Nombre": "Universidad Politécnica de Madrid",
      "Acrónimo": "UPM"
    },
    {
      "@id": "https://example.org/university/urjc",
	  "@type": "universidad",
      "Nombre": "Universidad Rey Juan Carlos",
      "Acrónimo": "URJC"
    }
  ]
}
