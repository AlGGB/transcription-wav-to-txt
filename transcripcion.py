import speech_recognition as sr 

filename = "somefile.wav" #archivo audio (formato wav)
outputFile = "somefile.txt" #archivo de salida (formato txt)

r = sr.Recognizer()

try:
    #abrir archivo de audio
    with sr.AudioFile(filename) as source:
        #duracion de audio
        duration = int(source.DURATION)

        #variable para guardar la transcripcion
        fullTranscripcion = ""

        print("procesando el archivo...")

        for i in range (0, duration, 10):
            try:

                audioData = r.record(source, duration=10)

                text= r.recognize_google(audioData, language="es-ES")
                fullTranscripcion += text + "\n"
                print(f"fragmento {i // 10 + 1}: {text}")
            except sr.UnknownValueError:
                print(f"fragmento {i // 10 + 1}: no se pudo enteder audio")
                fullTranscripcion += "[no se pudo entender el audio] \n"
            except sr.RequestError as e: 
                print(f"Error al comunicarse con google: {e}")
                break
        
        with open(outputFile, "w", encoding="utf-8") as f:
            f.write(fullTranscripcion)

        print(f"Transcripcion completada y guardada en {outputFile}")

except FileNotFoundError:
    print(f"El archivo {filename} no se encontro")
except ValueError as e:
    print(f"Error con el audio: {e}")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")

