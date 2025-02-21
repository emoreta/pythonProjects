# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:44:52 2025

@author: admin.emo
"""

import json

# Cargar el JSON original
with open("dataset_libro.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

# Guardar en formato JSONL
with open("datos.jsonl", "w", encoding="utf-8") as f:
    for item in datos:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("Archivo JSONL generado correctamente.")
