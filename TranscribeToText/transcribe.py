import speech_recognition as sr
from pydub import AudioSegment
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
# Convertir MP3 a WAV
audio = AudioSegment.from_mp3("Power_English_Update.mp3")
audio.export("audio.wav", format="wav")

# Usar SpeechRecognition para transcribir el audio
recognizer = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio_data = recognizer.record(source)
    #texto = recognizer.recognize_google(audio_data, language="es-ES")  # Cambiar el idioma según necesidad
    texto = recognizer.recognize_google(audio_data, language="en-US")
    print("Texto transcrito:", texto)
