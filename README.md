
📄 README.md

# 🌍 Gemini-Powered Language Translator

This is a simple and powerful Streamlit web application that uses **Google Gemini (via the `google-generativeai` API)** to translate English text into various languages such as Yoruba, Hausa, French, Spanish, Arabic, and more.

## 🚀 Features

- 🌐 Translate English into multiple target languages
- 🔐 Secure Gemini API Key input
- ⚡ Powered by Google's Gemini Pro/Flash model
- 🖥️ Built with Python and Streamlit

## 📦 Requirements

- Python 3.8+
- `streamlit`
- `google-generativeai`

Install requirements:

```bash
pip install -r requirements.txt

▶️ How to Run Locally

streamlit run app.py

🔑 Gemini API Key

You need to get your Gemini API key from Google AI Studio.

Paste the key into the input box when running the app.

🌐 Languages Supported (example)

Yoruba

Hausa

Igbo

French

Spanish

Arabic

German


> You can add more languages by updating the target_languages list in app.py.



📤 Deployment

You can deploy this app easily to Streamlit Cloud:

1. Push this folder to GitHub.


2. Go to streamlit.io/cloud.


3. Connect your GitHub repository.


4. Select app.py as the main file.


5. Add your GOOGLE_API_KEY via the interface or use a secrets file.


---

Built with ❤️ using Google Gemini and Streamlit.
