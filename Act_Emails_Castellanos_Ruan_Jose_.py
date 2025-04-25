{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPCslLZEkV31oMy2Q9tEuoN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/xXJoc22Xx-code/POO/blob/main/Act_Emails_Castellanos_Ruan_Jose_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jCHuBfQqVsgh",
        "outputId": "d86c305d-9e2e-4a94-e9ef-a6be80fd2d4d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Ingresa tu correosrpacman22@gmail.com\n",
            "Ingresa tu contraseña (generada con anterioridad)zaxs xxhr qwkf ebqv\n",
            "ingresa el destinatariosrpacman22@gmail.com\n",
            "Asunto: hola\n",
            "Mensaje: hola\n"
          ]
        }
      ],
      "source": [
        "import smtplib, ssl\n",
        "\n",
        "sender_email = input(\"Ingresa tu correo: \") # tu correo\n",
        "password = input(\"Ingresa tu contraseña (generada con anterioridad): \") #tu contraseña\n",
        "receiver_email =input(\"Ingresa el destinatario: \")#a quien se lo mandas\n",
        "asunto = input(\"Asunto: \")\n",
        "mensaje = input(\"Mensaje: \")\n",
        "email_message = f\"Subject: {asunto}\\n\\n{mensaje}\"\n",
        "try:\n",
        "    with smtplib.SMTP(\"smtp.gmail.com\", 587) as server:\n",
        "      server.starttls()\n",
        "      server.login(sender_email, password)\n",
        "      server.sendmail(sender_email, receiver_email, email_message)\n",
        "      print(\"Mensaje enviado!\")\n",
        "except:\n",
        "  print(\"Error: No se pudo enviar el correo\")\n"
      ]
    }
  ]
}