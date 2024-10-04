import speech_recognition as sr

"""
The code below converts Lithuanian speech from an audio file into text.  It initializes a recognizer and defines 
a function, lithuanian_speech_to_text, which processes the audio file.  The function adjusts for ambient noise, 
records the audio, and uses Google's speech recognition API to transcribe  the speech into text. 
The transcription is then printed and saved to a text file. Error handling is included to manage potential issues 
with API requests and unrecognized speech.
"""

recognizer = sr.Recognizer()

def lithuanian_speech_to_text(audio_file):
    try:
        with sr.AudioFile(audio_file) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="lt-LT")
            return text
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    except sr.UnknownValueError:
        return "Unknown error occurred"

audio_file_path = "record.wav"
transcription = lithuanian_speech_to_text(audio_file_path)
print(transcription)

with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(transcription)