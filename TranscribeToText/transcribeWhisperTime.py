# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:05:33 2025

@author: admin.emo
"""

import whisper

# Cargar el modelo preentrenado de Whisper
model = whisper.load_model("medium")

# Transcribir el archivo de audio y obtener los segmentos con tiempos
result = model.transcribe('Power_English_Update.mp3', language="en")

# Mostrar el texto junto con los tiempos
for segment in result['segments']:
    start = segment['start']
    end = segment['end']
    text = segment['text']
    print(f"[{start:.2f}s - {end:.2f}s]: {text}")

# Guardar la transcripción con tiempos en un archivo
output_file = "transcripcion_con_tiempos.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        text = segment['text']
        file.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")

print(f"Transcripción con tiempos guardada en {output_file}")
