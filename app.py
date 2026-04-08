import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Our Story ❤️", layout="wide")


# ---------------- BACKGROUND MUSIC ----------------
def play_audio(file_path):
    audio_file = open(file_path, "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")

# Call it
play_audio("assets/music.mp3")
# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
    body {
        background-color: #FFEBEB;
    }
    .title {
        text-align: center;
        font-size: 48px;
        color: #c9184a;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #6d6875;
        margin-bottom: 40px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }
    .section-title {
        font-size: 28px;
        color: #d00000;
        margin-bottom: 10px;
        text-align: center;
    }
    .text {
        font-size: 18px;
        color: #333;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    background-color: #FFEBEB;
}

/* This is the REAL card styling */
[data-testid="column"] > div {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LANDING ----------------
st.markdown('<div class="title">Hi Anant!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I made something for you...</div>', unsafe_allow_html=True)

st.write("")

# ---------------- TIMELINE ----------------

def memory(title, text, image):
    with st.container():
        # CARD WRAPPER USING STREAMLIT
        col1, col2, col3 = st.columns([1, 8, 1])

        with col2:
            # Title
            st.markdown(f"""
                <h3 style='text-align:center; color:#d00000; margin-bottom:10px;'>
                {title}
                </h3>
            """, unsafe_allow_html=True)

            # Image
            st.image(image, use_container_width=True)

            # Text
            st.markdown(f"""
                <p style='text-align:center; font-size:18px; color:#333; margin-top:10px;'>
                {text}
                </p>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

# 🌱 Beginning
memory(
    "🌱 The Beginning",
    "From that first conversation on 20th October… to meeting you in November… to you proposing on 5th December 💍. Everything felt so natural, like I had known you forever.",
    "assets/image1.png"
)

# 🌧️ Rough Patch
memory(
    "🌧️ The Storm That Made Us Stronger",
    "January wasn’t easy. We had our rough patch, and you fell sick… but somehow, even then, we didn’t let go.",
    "assets/image2.png"
)

# 💻 Building Together
memory(
    "💻 Building Together",
    "From January to July, working on our first creation… building our first website together. We weren’t just in love, we were building something real.",
    "assets/image3.png"
)

# 🎂 Birthdays
memory(
    "🎂 The Little Big Moments",
    "Your birthday with that red velvet cake ❤️, and then later that year where you surprised me with sweets, a proposal, and that overloaded McDonald’s burger 😭",
    "assets/image4.png"
)

# ✨ College Life
memory(
    "✨ Us, Living Life",
    "Roorkee trip, our first drink, learning ML together… those college days felt different because you were there.",
    "assets/image5.png"
)

# 🧠 Growth
memory(
    "🧠 Growing Together",
    "From research papers to placements… FNPC25, your job on 15th September, my internship on 4th December… we grew together.",
    "assets/image6.png"
)

# 🌄 Recent
memory(
    "🌄 Still Choosing You",
    "Seven hills, summers, all the little moments… even when life keeps changing, one thing hasn’t — I choose you.",
    "assets/image7.png"
)

# ---------------- FINAL MESSAGE ----------------
st.markdown('<div class="section-title">🎉 Happy 21st Birthday ❤️</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text">
Your Pikachu will always choose you, Charmander ⚡🔥<br><br>
Happy 21st, my love.<br>
You are my safest place, my biggest strength, and my favorite person.<br><br>
And no matter where life takes us…<br>
I’m just really glad it’s you.
</div>
""", unsafe_allow_html=True)

st.balloons()
st.markdown('</div>', unsafe_allow_html=True)