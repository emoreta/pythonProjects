# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:51:24 2025

@author: admin.emo
"""

#convertir pdf a imagen
from wand.image import Image

path_absoluta="Partido Social Cristiano - Henry Kronfle.pdf"
#estableciendo resolucion a imagen
with Image(filename=path_absoluta, resolution=400) as img:
    #estableciendo ancho y alto
    img.resize(1850,1850)
    img.save(filename="temp.jpg")