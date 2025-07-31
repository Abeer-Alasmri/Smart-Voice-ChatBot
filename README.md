# 🎙️ Smart Voice ChatBot

### 👩‍💻 Project Designer: Abeer Alasmri

---

## 🛠️ Tools and Libraries Used

| Tool / Library     | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| *Python*         | Programming language used to develop the project                           |
| *Anaconda*       | Environment manager for Python packages and dependencies                    |
| *Visual Studio Code* | Code editor used to write and run the Python scripts                   |
| *Terminal*       | Interface used to run the Python files and execute the chatbot             |
| *Whisper*        | Converts user voice to text (Speech-to-Text)                               |
| *Cohere*         | Generates text replies from user input using AI (Natural Language Generation) |
| *gTTS*           | Converts text responses into voice output (Text-to-Speech)                 |
| *sounddevice*    | Records the user's voice from microphone                                   |
| *wave*           | Saves the audio recordings temporarily as .wav files                     |

---

## 💡 Project Idea:
The goal is to build an intelligent voice-based chatbot that interacts with users through spoken conversation. The bot listens to the user's voice, transcribes it to text, generates a smart response using AI, and then replies with a natural voice.

---

## 🎯 Project Objectives:
- Enable voice input and output for natural human-machine interaction.
- Use AI to understand and generate meaningful responses.
- Create a seamless conversation flow between user and chatbot.
- Store all conversations in a text file for future reference.

---

## 📌 Task Description:
This project is part of the “AI & ROS Systems” summer training course.  
The task was to design a mini project using voice technologies, combining speech-to-text (STT), natural language processing (NLP), and text-to-speech (TTS) tools.  
The system should be able to:
- Record user voice input.
- Convert speech to text using Whisper.
- Generate smart responses using Cohere.
- Convert the reply text to speech using gTTS.
- Save each question and answer in a conversation log.

---

## 📁 Project Files

| File Name               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| *arabic_chatbot.py*   | Python script for the Arabic voice chatbot logic                            |
| *arabic.output.txt* | Output file storing Arabic chatbot conversation responses                   |
| *english_chatbot.py*  | Python script for the English voice chatbot logic                           |
| *english.output.txt*  | Output file storing English chatbot conversation responses                  |
| *env*                 | Virtual environment directory containing installed dependencies              |
| *python_terminal*     | Terminal setup or launcher used to run the chatbot                          |
| *voice_test.py*       | Script for testing microphone recording and playback                         |
| *Screenshot.q1*       | Screenshot of English conversation - part 1                                 |
| *Screenshot.q2*       | Screenshot of English conversation - part 2                                 |
| *Screenshot.q3*       | Screenshot of English conversation - part 3                                 |
| *Screenshot.q4*       | Screenshot of Arabic conversation - part 1                                  |
| *Screenshot.q5*       | Screenshot of Arabic conversation - part 2                                  |
| *Screenshot.q6*       | Screenshot of Arabic conversation - part 3                                  |

---

## 🚀 How to Run the Project (Detailed Steps)

1. *Open Anaconda Navigator* and create a new environment named voicebot (or any name you prefer).  
   - Activate the environment.

2. *Install the required libraries* inside the voicebot environment by running these commands in Anaconda Prompt or Terminal:  
   ```bash
   pip install openai cohere whisper gtts sounddevice playsound
   conda install -c conda-forge ffmpeg

3. Open *Visual Studio Code* from the activated *Anaconda* environment  
   > This ensures that the correct Python interpreter is used (linked to the voicebot environment)

4. Organize the project files:

::list
* Create a folder named ARABIC-ENGLISH-VOICE-CHATBOT  
* Place all the following files and resources inside the folder:
    - arabic_chatbot.py
    - english_chatbot.py
    - voice_test.py
    - .env
    - python_terminal
::

5. Set your *Cohere API key*:

::steps
1. Open the desired script (arabic_chatbot.py or english_chatbot.py)
2. Locate the line with "YOUR_API_KEY" or similar placeholder
3. Replace it with your *actual Cohere API key*
::

6. Open the terminal in Visual Studio Code:

::steps
1. Click View > Terminal, or press Ctrl + backtick (\)
2. Make sure the terminal path shows you're inside the project folder: ARABIC-ENGLISH-VOICE-CHATBOT
::
7. Run the desired Python script by typing one of the following commands and pressing Enter:

::code
# For Arabic Voice Chatbot
python arabic_chatbot.py

# For English Voice Chatbot
python english_chatbot.py

# For Voice Input Testing (mic to text)
python voice_test.py
::

> 📌 Make sure your microphone is connected and working before running the script.
8. Interact with the chatbot:

::step
* After running the script, you will see the prompt:
🎙️ Recording… Speak now

* Speak clearly into your microphone.

* Wait for the confirmation message:
✅ Audio recorded

* The program will display your recognized speech, followed by the chatbot's response.

* The chatbot will then read the response aloud using text-to-speech.
::

9. Check the log files:

::note
* All your conversations are saved automatically in either:

- arabic.output.txt (for Arabic script)
- english.output.txt (for English script)

* You can open these files to review the entire dialogue.
::

---

## 📸 Screenshots Details

| Screenshot       | Description                                   |
|------------------|-----------------------------------------------|
| ![](/Screenshot.q1.png) | English conversation screenshot 1: user asks basic questions. |
| ![](/Screenshot.q2.png) | English conversation screenshot 2: chatbot explains Riyadh info. |
| ![](/Screenshot.q3.png) | English conversation screenshot 3: AI explanation conversation. |
| ![](/Screenshot.q4.png) | Arabic conversation screenshot 1: user greeting chatbot in Arabic. |
| ![](/Screenshot.q5.png) | Arabic conversation screenshot 2: chatbot info about Saudi Arabia. |
| ![](/Screenshot.q6.png) | Arabic conversation screenshot 3: chatbot explaining AI meaning. |


---

## Videos List 🎥

| Link File                 | Description                                      |
|--------------------------|-------------------------------------------------|
| (https://drive.google.com/file/d/1uhuLsTgr_cWkAEzDI5MmcUnuG855ABPq/view?usp=drive_link)   | Greeting and introduction: "Hi, my name is Abeer. What's your name?" (English)  |
|  (https://drive.google.com/file/d/1gt2NjgoBjYqpxFdvLeFTvEcLxazjN9Iu/view?usp=drive_link) | Asking about the location of Riyadh city (English)                            |
| (https://drive.google.com/file/d/1B587WLB0Mw_71IOwOUkdC257s8qNuJvM/view?usp=drive_link)       | Question about Artificial Intelligence (English)                             |
| (https://drive.google.com/file/d/1Rd30M9uJyXV_FfD3aKixo_AS7A5pYuhI/view?usp=drive_link) | التحية والسؤال عن الحال: "السلام عليكم، كيف حالك؟" (عربي)                   |
| (https://drive.google.com/file/d/1q4vRE6na883JIEh1ZtIIexULIOchCJqW/view?usp=drive_link)    | معلومات عامة عن السعودية (عربي)                                            |
| (https://drive.google.com/file/d/15uaAH0ZqgJNIi07SWP-ufx8WKU8eUg-b/view?usp=drive_link)   | شرح معنى الذكاء الاصطناعي (عربي)                                           |

---

### ⚠️ Project Notes

- The project *requires an active internet connection* for the Cohere API to generate responses.
- The *accuracy of speech-to-text transcription* depends heavily on the quality of the audio recording.
- *Response time* may vary based on device performance and internet speed.
- Always *keep your API keys secure and do not share them publicly*.
