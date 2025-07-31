import warnings
warnings.filterwarnings("ignore")
import sounddevice as sd
import soundfile as sf
import whisper
import cohere
from gtts import gTTS
import os
import playsound
from datetime import datetime

# تسجيل الصوت
def record_audio(filename="input.wav", duration=10, fs=44100):
    print("🎙️ ...يتم الآن الاستماع لصوتك")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    sf.write(filename, recording, fs)
    print("✅ تم التسجيل")

# تحويل الصوت إلى نص باستخدام Whisper
def transcribe_audio(filename="input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename, language="ar")
    return result["text"]

# توليد الرد من Cohere باللغة العربية
def generate_response(prompt):
    co = cohere.Client("YOUR_API_KEY")  # ← ضعي مفتاحك الخاص  هنا
    arabic_prompt = f"أجب بالعربية فقط: {prompt}"  # ← التوجيه هنا
    response = co.generate(
        model='command-r-plus',
        prompt=arabic_prompt,
        max_tokens=100,
        temperature=0.5,
        stop_sequences=["\n"],
    )
    return response.generations[0].text.strip()

# تحويل الرد إلى صوت
def speak_response(text, filename="response.mp3"):
    tts = gTTS(text=text, lang="ar")
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# حفظ المحادثة
def save_to_log(user_input, bot_response, log_file="arabic.output.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"\n🕒 {now}\n👤 You: {user_input}\n🤖 Bot: {bot_response}\n")

# تنفيذ العملية
record_audio()
user_input = transcribe_audio()
print("🗣️ :أنت قلت", user_input)

bot_response = generate_response(user_input)
print("🤖 :رد البوت", bot_response)

speak_response(bot_response)
save_to_log(user_input, bot_response)