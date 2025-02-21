import speech_recognition as sr

audio_file= sr.Recognizer()

def capturar_audio():
    with sr.Microphone() as audio:
        print("habla, ahora...")
        audio_file.adjust_for_ambient_noise(audio)
        file= audio_file.listen(audio)
    return file 
def transcribir_audio_espaniol(file):
    try:
        text=audio_file.recognize_google(file,  language="es-Es")
        return text  
    except:
        return "no se reconoce el dialogo"     



