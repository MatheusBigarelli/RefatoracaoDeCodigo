from xml.dom.minidom import *
import csv
from XMLParser import XMLParser
from hero import Hero
#Biblioteca usada somente para criar o diretorio dadosMarvel diretamente
import os

# Functions
def get_heroes_from_file(file):
    universe = get_universe_tree(file)
    # Get all the heroes in the universe
    heroes_xml_element = universe.getElementsByTagName('hero')
    heroes = []
    for hero_xml_element in heroes_xml_element:
        new_hero = create_new_hero(hero_xml_element)
        heroes.append(new_hero)
    return heroes

def get_universe_tree(file):
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(file)
    universe = DOMTree.documentElement

    return universe

def create_new_hero(hero_xml_element):
    parser = XMLParser()
    id = hero_xml_element.getAttribute('id')
    information = parser.create_info_object_with_attributes(hero_xml_element, Hero.keys)
    new_hero = Hero(id, information)
    return new_hero

def write_csv_files(herois, herois_good, herois_bad, heroes):
    for hero in heroes:
        write_hero_file(herois, hero)

        if hero.attributes['alignment'] == 'Good':
            write_hero_file(herois_good, hero)

        if hero.attributes['alignment'] == 'Bad':
            write_hero_file(herois_bad, hero)

def write_hero_file(file, hero):
    writer = csv.writer(file)
    row = []
    for value in hero.attributes.values():
        row.append(value)
    writer.writerow(row)

def print_information_about_heroes():
    #Variaveis para dados pedidos
    goods = 0
    bads = 0
    pesos = 0
    total_herois = 0

    for hero in heroes:
        if hero.attributes['alignment'] == 'Good':
            goods += 1
        if hero.attributes['alignment'] == 'Bad':
            bads += 1

        #Para calcular a media do peso dos personagens
        pesos += float(hero.attributes['weight_kg'])
        total_herois += 1

        #Canculando o indice de massa corporal do hulk
        if hero.attributes['name'] == 'Hulk':
            peso_Hulk = float(hero.attributes['weight_kg'])
            altura_Hulk = float(hero.attributes['height_m'])
            IMC =  peso_Hulk/(altura_Hulk**2)

    proportion = float(goods)/bads

    print ('Proporcao entre herois bons e maus (bons/maus): ' + str(proportion))
    print ('Media de peso dos herois: ' + str(round(pesos/total_herois, 2)))
    print ('Indice de massa corporal (IMC) do Hulk: ' + str(IMC))


# Program

os.system("mkdir -p dadosMarvel")

heroes = get_heroes_from_file('marvel_simplificado.xml')

#Arquivo onde serao guardados os dados dos herois da marvel.
herois = open("dadosMarvel/herois.csv", "w")
herois_good = open("dadosMarvel/herois_good.csv", "w")
herois_bad = open("dadosMarvel/herois_bad.csv", "w")
write_csv_files(herois, herois_good, herois_bad, heroes)
herois.close
herois_bad.close
herois_good.close

print_information_about_heroes()
