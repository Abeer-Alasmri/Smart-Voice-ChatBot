from gtts import gTTS
import os
import pygame

text = "مرحبا عبير، هذا اختبار الصوت من الشات بوت."

tts = gTTS(text=text, lang='ar')

# حفظ الملف بصيغة mp3 في مجلد السكربت الحالي
filename = "temp_response.mp3"
tts.save(filename)

pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

# لو تبي تمسح الملف بعد التشغيل
os.remove(filename)