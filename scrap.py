# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup

web = false
while not web:
	web = raw_input("¿URL a procesar?")

# Obtener el HTML
page = urlopen(web).read()

scraped = BeautifulSoup(page, "html5lib")

# Get elements
element = raw_input('¿Qué elemento deseas obtener?')
while not element:
	element = raw_input('¿Qué elemento deseas obtener?')

elementClass = raw_input('¿Qué clase tiene dicho elemento? (empty if not)')

if elementClass:
	results = scraped.find_all(element, class_=elementClass)
else:
	results = scraped.find_all(element)


for result in results:
	print (result)