# 📰 AutoNews Video Generator

Automatically generate daily news summary videos from top headlines using web scraping, AI-based scripting, text-to-speech, and video rendering.

---

## 🚀 Features

- **Web Scraping:** Fetches top news headlines using BeautifulSoup.
- **AI Script Writing:** Uses a Large Language Model (LLM) to create a compelling script based on the headlines.
- **Text-to-Speech (TTS):** Converts the script into audio using gTTS.
- **Video Creation:** Uses MoviePy to combine text, images, and audio into a finished video.

---

## 🛠️ Technologies Used

- Python 3.x
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Groq Llama LLM](https://console.groq.com/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [MoviePy](https://zulko.github.io/moviepy/)

---

## 📦 Installation

1. **Clone the repo:**

```
git clone https://github.com/hemantkumarlearning/News_Video_Generator.git
cd News_Video_Generator
```

2. **Install dependencies:**

```
pip install -r requirements.txt
```

## ⚙️ Usage

```
python main.py
```

## The script will:

- Scrape top headlines

- Generate a script using the LLM

- Convert it to speech using gTTS

- Create a video with audio and captions
