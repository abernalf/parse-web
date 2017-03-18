#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
# encoding: latin1
import re
import sys

import urllib.request

def cargar_links():
    expr = "href=\"equipamiento"

    wp = urllib.request.urlopen (
        "http://www.gobiernodecanarias.org/cmayot/centrodocumentacion/recursoseducativos/guia_equipamientos_naturaleza/guiaequip.jsp?id_isla=40&id_tipo=3" )
    pw = wp.read ( ).decode ( wp.headers.get_content_charset ( ) )

    res = pw.split ( )
    indx = [ ]
    res2 = [ ]
    for i in range ( 0 , len ( res ) ):
         if re.search ( expr , str ( res[ i ] ) ):
             indx += [ i ]
    res2 = [ ]
    for i in range ( 0 , len ( indx ) ):
         aux = str ( res[ indx[ i ] ] ).split ( "=\"" )
         tam = len ( aux )
         #print(aux)
         res[ indx[ i ] ] = aux[ tam - 1 ]
         aux = str ( res[ indx[ i ] ] ).split ( "\"" )
         res[ indx[ i ] ] = aux[ 0 ]
         res[ indx[ i ] ] = res[ indx[ i ] ].replace ( "aspx" , "htm" )
         res2 += [ "http://www.gobiernodecanarias.org/cmayot/centrodocumentacion/recursoseducativos/guia_equipamientos_naturaleza/" + res[ indx[ i ] ] ]


    #print(res2)
    print("Done")
    return res2
links1 = cargar_links()
resultado = [ ]
for i in range ( 0 , len ( links1 ) ):

    vec_ub = urllib.request.urlopen ( links1[ 0 ] )
    vec_ub = vec_ub.read ( ).decode ( vec_ub.headers.get_content_charset ( ) )
    vec_ub = vec_ub.split ( "<" )

    vec_lin = urllib.request.urlopen ( links1[ i ] )
    vec_lin = vec_lin.read ( ).decode ( vec_lin.headers.get_content_charset ( ) )
    vec_lin = vec_lin.split ( "<strong>" )

    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Nombre" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]

    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Isla" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Municipio" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Acceso&nbsp;" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Transporte" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Contacto:" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]

    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Permiso/Autorización:" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]

    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Superficie" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Accesibilidad para minusválidos:" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</td>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]

    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Agua" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( )]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Electricidad" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Duchas" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Bar" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i+1 ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Comedor" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Fogones" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Bancos," , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]
    for i in range ( 0 , len ( vec_lin ) ):
        if re.search ( "Aparcamientos" , str ( vec_lin[ i ] ) ):
            aux = vec_lin[ i ].split ( "class=\"fondogris\">" )
            aux = aux[ 1 ].split ( "</TD>" )
            resultado += [ aux[ 0 ].lstrip ( ) ]



    print (resultado)

    with open ( 'lib/output2.csv' , 'a' ) as f:
        print (len ( resultado ))
        f.write ( ((str ( resultado )).replace ( "[" , "" )).replace ( "]" , "" ) )
        f.write ( "\n" )
        f.close ( )
        resultado = [ ]