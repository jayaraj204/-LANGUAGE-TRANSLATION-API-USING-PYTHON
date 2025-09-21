import sounddevice as sd
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import tempfile
import os


supported_langs = GoogleTranslator().get_supported_languages(as_dict=True) 

recognizer = sr.Recognizer()
print("Speak now..")

duration = 8
sample_rate = 16000
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()
audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)

rough_text = None
for lang_code in supported_langs.values():
    try:
        text = recognizer.recognize_google(audio, language=lang_code)
        rough_text = text
        print(f"Recognized.. {lang_code}: {text}")
        break
    except:
        continue

if not rough_text:
    print("Could not recognize speech in any language...")
    exit()

words = rough_text.strip().split()
target_lang_name = words[-1].lower()
message = " ".join(words[:-1])


target_lang_code = supported_langs.get(target_lang_name, None)

if not target_lang_code:
    print(f"Could not map '{target_lang_name}' to a supported language code.")
    exit()


translated = GoogleTranslator(source='auto', target=target_lang_code).translate(message)
print(f"Translated ({target_lang_name}): {translated}")

with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
    temp_file = fp.name
gTTS(translated, lang=target_lang_code).save(temp_file)

pygame.mixer.init(frequency=22050, size=-16, channels=2)
pygame.mixer.music.load(temp_file)
pygame.mixer.music.play()

print("Playing audio...")

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.mixer.music.stop()
pygame.mixer.quit()
os.remove(temp_file)
