import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

recognizer = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Say 'hello' to start the translation process.")
    recognizer.adjust_for_ambient_noise(source, duration=0.2)
    audio_input = recognizer.listen(source)
    spoken_text = recognizer.recognize_google(audio_input).lower()

if 'hello' in spoken_text:
    translator = Translator()
    source_lang = 'en'
    target_lang = 'hi'

    with mic as source:
        print("Please speak a sentence...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio_input = recognizer.listen(source)
        sentence = recognizer.recognize_google(audio_input)

        try:
            print("Sentence to be translated: " + sentence)
            translated_text = translator.translate(sentence, src=source_lang, dest=target_lang).text
            speech = gTTS(text=translated_text, lang=target_lang, slow=False)
            speech.save("translated_audio.mp3")
            os.system("start translated_audio.mp3")
        except sr.UnknownValueError:
            print("Could not understand the audio input.")
        except sr.RequestError as error:
            print(f"An error occurred: {error}")