import whisper

# Cargar el modelo preentrenado de Whisper
model = whisper.load_model("medium")

# Transcribir el archivo de audio (asegúrate de que el nombre coincide con el archivo en la misma carpeta)
result = model.transcribe('Power_English_Update.mp3', language="es")  # "es" es para español

# Mostrar la transcripción
print(result["text"])

# Guardar el texto transcrito en un archivo
output_file = "transcripcion.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result["text"])

print(f"Transcripción completa guardada en {output_file}")
