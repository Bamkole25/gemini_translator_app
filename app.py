import streamlit as st
import google.generativeai as genai

# === App Title ===
st.title("🌍 Gemini-Powered Language Translator")

# === API Key Configuration ===
#api_key = st.text_input("🔐 Enter your Gemini API Key", type="password")
api_key = st.secrets["GOOGLE_API_KEY"]
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
else:
    st.warning("Please enter your Gemini API key to continue.")
    st.stop()

# === Language Options ===
target_languages = [
    "Yoruba", "Hausa", "Igbo", "French", "Spanish", "Arabic", "German"
]
text_to_translate = st.text_area("📝 Enter English text to translate:")
target_lang = st.selectbox("🌐 Choose target language:", target_languages)

# === Translation Button ===
if st.button("🔄 Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            prompt = f"Translate the following English text to {target_lang}: {text_to_translate}"
            try:
                response = model.generate_content(prompt, generation_config={"candidate_count": 1})
                st.success("✅ Translation:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")