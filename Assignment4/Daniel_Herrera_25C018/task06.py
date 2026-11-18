{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nOOPLCHF7hLB"
      },
      "source": [
        "# **Task 06: Modifying RDF(s)**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XY7aPc86Bqoo"
      },
      "source": [
        "Spanish: Importar la librería RDFLib\n",
        "\n",
        "English: Import RDFLib main methods"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "id": "9ERh415on7kF"
      },
      "outputs": [],
      "source": [
        "from rdflib import Graph, Namespace, Literal, XSD\n",
        "from rdflib.namespace import RDF, RDFS\n",
        "from oeg_sw_class import Report\n",
        "# Do not change the name of the variables\n",
        "g = Graph()\n",
        "g.namespace_manager.bind('ns', Namespace(\"http://somewhere#\"), override=False)\n",
        "r = Report()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gM3DASkTQQ5Y"
      },
      "source": [
        "Spanish: Crear una nueva clase llamada \"Researcher\"\n",
        "\n",
        "English: Create a new class named Researcher"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZX8w9jnV5Xhp"
      },
      "source": [
        "### **Task 6.0:**\n",
        "\n",
        "Spanish: Crea nuevos prefijos para \"ontology\", \"organization\" and \"person\", con la siguiente información:\n",
        "\n",
        "*   person: http://oeg.fi.upm.es/resource/person/\n",
        "*   organization: http://oeg.fi.upm.es/resource/organization/\n",
        "*   ontology: http://oeg.fi.upm.es/def/people#\n",
        "\n",
        "English: Create new prefixes for \"ontology\", \"organization\" and \"person\", with the following information:\n",
        "\n",
        "*   person: http://oeg.fi.upm.es/resource/person/\n",
        "*   organization: http://oeg.fi.upm.es/resource/organization/\n",
        "*   ontology: http://oeg.fi.upm.es/def/people#"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "b1ZQgYgB5vi7"
      },
      "outputs": [],
      "source": [
        "# this task is validated in the next step\n",
        "organization = Namespace(\"http://oeg.fi.upm.es/resource/organization/\")\n",
        "g.bind(\"organization\", organization)\n",
        "\n",
        "person = Namespace(\"http://oeg.fi.upm.es/resource/person/\")\n",
        "g.bind(\"person\", person)\n",
        "\n",
        "ontology = Namespace(\"http://oeg.fi.upm.es/def/people#\")\n",
        "g.bind(\"ontology\", ontology)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qp1oe2Eddsvo"
      },
      "source": [
        "### **Task 6.1**\n",
        "\n",
        "Spanish: Reproduce la taxonomía de clases que aparece en el diagrama (`Assignment4/course_materials/diagram/diagram.jpg`). Añade etiquetas para cada una de ellas tal y como aparecen en el diagrama (exactamente), sin etiquetas de idioma. Recuerda añadir el tipo de datos correcto (xsd:String) cuando sea necesario.\n",
        "\n",
        "English: Reproduce the taxonomy of classes shown in the diagram (`Assignment4/course_materials/diagram/diagram.jpg`). Add labels for each of them as they are in the diagram (exactly) with no language tags. Remember adding the correct datatype (xsd:String) when appropriate.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-G_onfBuxKaz",
        "outputId": "56093bf0-247d-4abd-c220-9ea8bb50289d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.1 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_01(g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mp696_Sa1_fx"
      },
      "source": [
        "### **Task 6.2**\n",
        "\n",
        "Spanish: Crea la clase ontology:University.\n",
        "\n",
        "English: Create the ontology:University class."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JSDajXT7_YW4",
        "outputId": "401c688f-ecbc-447c-a6ee-00f3992289ba"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.2 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_02(g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MXBqtBkJd22I"
      },
      "source": [
        "### **Task 6.3**\n",
        "\n",
        "Spanish: Añade las propiedades que aparecen en el diagrama. Añade etiquetas para cada una de ellas (exactamente como aparecen en la diapositiva, sin etiquetas de idioma), así como sus dominios y rangos correspondientes utilizando RDFS. Recuerda añadir el tipo de datos correcto (xsd:String) cuando sea necesario. Si una propiedad no tiene rango, conviértela en un literal (cadena de caracteres). Por otra parte, ontology:affiliatedWith tendrá como dominio ontology:Person y rango ontology:University.\n",
        "\n",
        "English: Add the properties shown in the previous diagram. Add labels for each of them (exactly as they are in the slide, with no language tags), and their corresponding domains and ranges using RDFS. Remember adding the correct datatype (xsd:String) when appropriate. If a property has no range, make it a literal (string). Furthermore, the ontology:affiliatedWith property will have ontology:Person as its domain and ontology:University as its range.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xdxmDe3HxJcT",
        "outputId": "e4ef9bb1-b2d5-4b25-ac94-3af62e1341ab"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.3 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_03(g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OGct6k7Ld9O0"
      },
      "source": [
        "### **Task 6.4**\n",
        "\n",
        "Spanish: Crea los individuos que aparecen en el diagrama, en la sección «Datos». Vincúlalos con las mismas relaciones que se muestran en el diagrama.\n",
        "\n",
        "English: Create the individuals shown in the diagram under \"Datos\". Link them with the same relationships shown in the diagram.\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ofqVMI8WxIPD",
        "outputId": "7423f69c-97b8-45ed-d36d-153d71324675"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.4 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_04(g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tD383J__eHfV"
      },
      "source": [
        "### **Task 6.5**\n",
        "\n",
        "Spanish: Añadir a person:Juan la dirección email (juan.cano@upm.es), el nombre (given) y los apellidos (family). Utiliza las propiedades que ya se incluyen en el ejemplo 4 para describir a Jane y John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). No importes los espacios de nombres; añádelos manualmente.\n",
        "\n",
        "English: Add to the individual person:Juan the email address (juan.cano@upm.es), given and family names. Use the properties already included in example 4 to describe Jane and John (https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/rdf/example4.rdf). Do not import the namespaces, add them manually.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6mahMZlNxM1K",
        "outputId": "f87fd611-7ce2-4540-a2d8-5c245a502327"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.5 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_05(g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q_eoRAIdusgb"
      },
      "source": [
        "### **Task 6.6**\n",
        "\n",
        "Spanish: Añade que Juan y Raúl están afiliados (affiliatedWith) a university:UPM. También que Sven es de tipo InterimAssociateProfessor.\n",
        "\n",
        "English:  Add that Juan and Raúl are affiliated (affiliatedWith) with the university:UPM. Also add that Sven is a InterimAssociateProfessor"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 41,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A7JdhmrBxNDk",
        "outputId": "ee6932da-b2fb-4425-824f-0defbf87c98a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.6 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_06(g)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Y3wNc3fKuEdf"
      },
      "source": [
        "### **Task 6.7**\n",
        "\n",
        "Spanish: Tanto university:UPM como university:Mannheim son de tipo ontology:University.\n",
        "\n",
        "English:  Both university:UPM and university:Mannheim are ontology:University type."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 43,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7TNaKMGTxNZK",
        "outputId": "3db109d9-abaf-46d6-8e38-8665d46358ae"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "TASK 6.7 OK\n"
          ]
        }
      ],
      "source": [
        "#Validation: Do not remove\n",
        "r.validate_task_06_07(g)\n",
        "r.save_report(\"_Task_06\")"
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
