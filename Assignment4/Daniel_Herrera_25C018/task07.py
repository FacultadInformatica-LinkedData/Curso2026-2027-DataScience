{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nOOPLCHF7hLB"
      },
      "source": [
        "**Task 07: Querying RDF(s)**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XY7aPc86Bqoo"
      },
      "source": [
        "Spanish: Primero leemos los ficheros RDF\n",
        "\n",
        "English: First let's read the RDF file"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "9ERh415on7kF"
      },
      "outputs": [],
      "source": [
        "from rdflib import Graph, Namespace, Literal\n",
        "from rdflib.namespace import RDF, RDFS\n",
        "from oeg_sw_class import Report\n",
        "# Do not change the name of the variables\n",
        "g = Graph()\n",
        "g.namespace_manager.bind('ns', Namespace(\"http://somewhere#\"), override=False)\n",
        "g.parse(github_storage+\"/rdf/data07.ttl\", format=\"TTL\")\n",
        "report = Report()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qp1oe2Eddsvo"
      },
      "source": [
        "**TASK 7.1a:**\n",
        "\n",
        "Spanish: Para todas las clases, enumera cada classURI. Si la clase pertenece a otra clase, indica su superclase. Realiza el ejercicio en RDFLib devolviendo una lista de tuplas: (clase, superclase) denominada \"result\". Si una clase no tiene superclase, devuelve None como superclase.\n",
        "\n",
        "English: For all classes, list each classURI. If the class belogs to another class, then list its superclass. Do the exercise in RDFLib returning a list of Tuples: (class, superclass) called \"result\". If a class does not have a super class, then return None as the superclass"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uvEpQQrTlMPH",
        "outputId": "9ab07212-9260-4a8a-cd10-63f2653d5341"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 7.1a OK\n"
          ]
        }
      ],
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_1a(result)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kbY-jqw6klr9"
      },
      "source": [
        "**TASK 7.1b:**\n",
        "\n",
        "Spanish: Repite el mismo ejercicio en SPARQL, devolviendo las variables ?c (clase) y ?sc (superclase)\n",
        "\n",
        "English: Repeat the same exercise in SPARQL, returning the variables ?c (class) and ?sc (superclass)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9zf4vgVHlKR3",
        "outputId": "f885805e-cf26-450c-a3f1-1d9fb70b4c97"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 7.1b OK\n"
          ]
        }
      ],
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_1b(query,g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gM3DASkTQQ5Y"
      },
      "source": [
        "**TASK 7.2a:**\n",
        "\n",
        "Spanish: Enumera todos los individuos de \"Person\" con RDFLib (ten en cuenta las subclases). Devuelve los URI de los individuos en una lista llamada \"individuals\".\n",
        "\n",
        "English: List all individuals of \"Person\" with RDFLib (remember the subClasses). Return the individual URIs in a list called \"individuals\"\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ONrAls5uiX1G",
        "outputId": "69479ccf-d1b1-42bc-dfc6-50a96fe16ac2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 7.2a OK\n"
          ]
        }
      ],
      "source": [
        "# validation. Do not remove\n",
        "report.validate_07_02a(individuals)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "up-952A-za7A"
      },
      "source": [
        "**TASK 7.2b:**\n",
        "\n",
        "Spanish: Repite el mismo ejercicio en SPARQL, devolviendo los URI individuales en una variable ?ind.\n",
        "\n",
        "English: Repeat the same exercise in SPARQL, returning the individual URIs in a variable ?ind"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s-Hu2LxRjUQt",
        "outputId": "c4eb698b-1615-4581-ac27-7d7975b046b8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 7.2b OK\n"
          ]
        }
      ],
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_02b(g, query)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3NyI7M2VNr9R"
      },
      "source": [
        "**TASK 7.3:**\n",
        "\n",
        "Spanish: Enumera el nombre y el tipo de quienes conocen a Curry (solo en SPARQL). Utiliza el nombre y el tipo como variables en la consulta.\n",
        "\n",
        "English: List the name and type of those who know Curry (in SPARQL only). Use name and type as variables in the query"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zf3JS7tEhS2t",
        "outputId": "75dbae58-367e-4dac-9eb4-c53d9a7604a5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 7.3 OK\n"
          ]
        }
      ],
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_03(g, query)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kyjGsyxDPa2C"
      },
      "source": [
        "**Task 7.4:**\n",
        "\n",
        "Spanish: Enumera los nombres de aquellas entidades que tengan un compañero de trabajo que tenga un perro, o que tengan un compañero de trabajo que tenga un compañero de trabajo que tenga un perro (en SPARQL). Devuelve los resultados en una variable llamada «name».\n",
        "\n",
        "English: List the name of those entities who have a colleague with a dog, or that have a collegue who has a colleague who has a dog (in SPARQL). Return the results in a variable called name"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zcTZE7ngj2fc",
        "outputId": "8e4bca09-d98b-4fb5-9c80-466f7cbc9b8f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 7.4 OK\n"
          ]
        }
      ],
      "source": [
        "## Validation: Do not remove\n",
        "report.validate_07_04(g,query)\n",
        "report.save_report(\"_Task_07\")"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.5"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
