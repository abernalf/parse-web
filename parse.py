#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
# encoding: latin1
import urllib.request
import re
import sys
print (sys.stdout.encoding)




def cargar_links():
	expr = "map-data"


	wp = urllib.request.urlopen("http://www.webtenerife.com/que-hacer/naturaleza/senderismo/senderos/?gclid=CMfX7qWrotICFYc_GwodZi4LyQ&page-index=1&tab-view-mode=listado")
	pw = wp.read().decode(wp.headers.get_content_charset())

	res = pw.split( )
	indx = []
	res2 = []
	for i in range(0,len(res)):
		if re.search(expr, str(res[i])):
			indx += [i]
	res2 = []
	for i in range(0,len(indx)):
		aux =str(res[indx[i]]).split("/")
		tam = len(aux)
		res[indx[i]] = aux[tam-1]
		aux =str(res[indx[i]]).split("\"")
		res[indx[i]] = aux[0]
		res[indx[i]] = res[indx[i]].replace("aspx", "htm") 
		res2 += ["http://www.webtenerife.com/que-hacer/naturaleza/senderismo/senderos/"+res[indx[i]]]

	return res2

		
	print("Done")

links1 = cargar_links()

resultado = []
for i in range(0,len(links1)):
	vec_ub = urllib.request.urlopen(links1[i])
	vec_ub = vec_ub.read().decode(vec_ub.headers.get_content_charset())
	vec_ub = vec_ub.split("<")

	vec_lin = urllib.request.urlopen(links1[i])
	vec_lin = vec_lin.read().decode(vec_lin.headers.get_content_charset())
	vec_lin = vec_lin.split("<strong>")
	for i in range(0,len(vec_lin)):
		if re.search("Inicio:", str(vec_lin[i])):
			aux = vec_lin[i].split("</strong>")
			aux = aux[1].split("</li>")
			resultado += [aux[0].lstrip()]
	for i in range(0,len(vec_lin)):
		if re.search("Fin:", str(vec_lin[i])):
			aux = vec_lin[i].split("</strong>")
			aux = aux[1].split("</li>")
			resultado += [aux[0].lstrip()]
	for i in range(0,len(vec_lin)):
		if re.search("Grado de dificultad:", str(vec_lin[i])):
			aux = vec_lin[i].split("</strong>")
			aux = aux[1].split("</li>")
			resultado += [aux[0].lstrip()]
	for i in range(0,len(vec_lin)):
		if re.search("Tipo de recorrido:", str(vec_lin[i])):
			aux = vec_lin[i].split("</strong>")
			aux = aux[1].split("</li>")
			resultado += [aux[0].lstrip()]
	for i in range(0,len(vec_lin)):
		if re.search("Distancia:", str(vec_lin[i])):
			aux = vec_lin[i].split("</strong>")
			aux = aux[1].split("</li>")
			resultado += [aux[0].lstrip()]
	for i in range(0,len(vec_lin)):
		if re.search("Duraci", str(vec_lin[i])):
			aux = vec_lin[i].split("</strong>")
			aux = aux[1].split("</li>")
			resultado += [aux[0].lstrip()]
	for i in range(0,len(vec_ub)):
		if re.search("meta itemprop=", str(vec_ub[i])):
			aux = vec_ub[i].split("content=\"")
			aux = aux[1].split("\"")
			resultado += [aux[0].lstrip()]
	print(resultado)
	with open('lib/output.csv','a') as f:
		
		f.write(((str(resultado)).replace("[","")).replace("]", ""))
		f.write("\n")
		f.close()
		resultado = []




#for i in range(0,len(links1)):
	#print(links1[i])

