"""
    This module is for all functions relative to the countries
"""

import json


import interface

import io



"""Permet de charger le fichier json """
with open('countries.json') as data_file:
    countries = json.load(data_file)


def AllCountries():
    """affiche tous les pays"""
    for x in countries:
        nom = countries[x]['name']
        capital = countries[x]['capital']
        continent = countries[x]['location']
        independance = countries[x]['independance']
        president = countries[x]['president']
        langue = countries[x]['langue']
        superficie = countries[x]['superficie']
        haditant = countries[x]['population']
        pib = countries[x]['pib']

        print(f"Nom                  : {nom}")
        print(f"Capital              : {capital}")
        print(f"Continent            : {continent}")
        print(f"Date Independance    : {independance}")
        print(f"Nom President Actuel : {president}")
        print(f"Langue Offielle      : {langue}")
        print(f"Superficie           : {superficie}")
        print(f"Nombre d'habitants   : {haditant}")
        print(f"PIB                  : {pib}")


# get the country that user want to display
def getCountry():
    """affiche un pays"""
    # Read JSON file
    # with open('countries.json') as data_file:
    #     countries = json.load(data_file)

    print("===Affichage d'un pays membre===\n")
    choice = str(input("Entrer l'indicatif du pays\n"))
    country = countries[choice]
    return interface.display(country)


# Add new country
def newCountry():
    """Ajouter un nouveau pays"""

    print("===Ajout d'un pays membre===\n")
    id = str(input("Entrer l'indicatif du pays a ajouter\n"))
    name = input("Entrer le nom du pays\n")
    capital = input("Entrer la capital du pays\n")
    location = input("Entrer le continent du pays\n")
    dateIndependance = str(input("Entrer la date d'accession a l'independance JJ/MM/AA\n"))
    nomPresident = input("Entrer le nom du president actuel\n")
    langue = input("Entrer la langue officielle\n")
    superficie = str(input("Entrer la superficie\n"))
    population = str(input("Enter le nombre d'habitants\n"))
    pib = input("Entrer le PIB du pays\n")

    with io.open('countries.json', 'w', encoding='utf8') as outfile:
        countries[id] = {
            "name": name,
            "capital": capital,
            "location": location,
            "independance": dateIndependance,
            "president": nomPresident,
            "langue": langue,
            "superficie": superficie,
            "population": population,
            "pib": pib
        }
        str_ = json.dumps(countries,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)


# delete country from the dictionnary
def deleteCountry():
    """Supprimer un pays """

    index = str(input("Entrer l'indicatif du pays\n"))

    with io.open('countries.json', 'w', encoding='utf8') as outfile:
        countries.pop(index)
        str_ = json.dumps(countries,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)
    print("Country deleted")
    interface.menu()


def editCountry():
    """Modifier un pays """

    print("===Ajout d'un pays membre===\n")

    index = str(input("Entrer l'indicatif du pays\n"))
    id = str(input("Entrer l'indicatif du pays a ajouter\n"))
    name = input("Entrer le nom du pays\n")
    capital = input("Entrer la capital du pays\n")
    location = input("Entrer le continent du pays\n")
    dateIndependance = str(input("Entrer la date d'accession a l'independance JJ/MM/AA\n"))
    nomPresident = input("Entrer le nom du president actuel\n")
    langue = input("Entrer la langue officielle\n")
    superficie = str(input("Entrer la superficie\n"))
    population = str(input("Enter le nombre d'habitants\n"))
    pib = input("Entrer le PIB du pays\n")

    for x, y in countries.items():
        if (x == index):
            countries[index]["name"] = name
            countries[index]["capital"] = capital
            countries[index]["location"] = location
            countries[index]["independance"] = dateIndependance
            countries[index]["president"] = nomPresident
            countries[index]["langue"] = langue
            countries[index]["superficie"] = superficie
            countries[index]["population"] = population
            countries[index]["pib"] = pib
            break;
        else:
            print("Pays Inconnu")

    with io.open('countries.json', 'w', encoding='utf8') as outfile:

        str_ = json.dumps(countries,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)

    interface.menu()
