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


    print(res2)
    print("Done")
    return res2

cargar_links()
