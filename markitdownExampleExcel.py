# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:16:05 2025

@author: admin.emo
"""
from markitdown import MarkItDown

md = MarkItDown()
#excel,word,presentacion
result = md.convert("Automatización del análisis de llamadas.pptx")
print(result.text_content)