import streamlit as st
import random

st.set_page_config(page_title="Excuse Generator 3000", page_icon="🤡", layout="centered")

st.title("🤡 Excuse Generator 3000")
st.subheader("Never run out of excuses again!")

categories = ["Work", "College", "Family", "Friends", "Fitness", "Date", "Traffic"]

category = st.selectbox("What do you need an excuse for?", categories)

severity = st.slider("How serious is the situation?", 1, 5, 3)

name = st.text_input("Your name (optional)", "")

if st.button("Generate Excuse", type="primary"):
    excuses = {
        "Work": [
            "My laptop suddenly decided to join a meditation retreat and refused to turn on.",
            "I was attacked by a flock of aggressive pigeons on my way to office.",
            "My alarm clock joined a cult and now only wakes up at 3 PM."
        ],
        "College": [
            "My dog ate my assignment… and then submitted it as his own project.",
            "There was a sudden solar eclipse and my brain stopped working.",
            "I got stuck in an intense debate with ChatGPT about life."
        ],
        "Family": [
            "My grandma challenged me to a chess match and I couldn’t disrespect her.",
            "There was a family emergency… my WiFi stopped working.",
            "I had to attend my cousin’s goldfish’s funeral."
        ],
        "Friends": [
            "I was busy saving the world… from my messy room.",
            "My phone fell into a parallel universe and never came back.",
            "I was practicing for a dance battle that doesn’t exist yet."
        ],
        "Fitness": [
            "My muscles went on strike and formed a union.",
            "The gym was closed due to excessive motivation in the air.",
            "I tripped over my own motivation and it broke."
        ],
        "Date": [
            "I was busy writing a 500-page apology letter for being late.",
            "My mirror told me I wasn’t ready yet.",
            "I got kidnapped by my own blanket."
        ],
        "Traffic": [
            "There was a turtle crossing the road and I had to escort it safely.",
            "All the traffic lights decided to have a meeting at the same time.",
            "My car wanted to take the scenic route today."
        ]
    }

    selected_excuses = excuses[category]
    excuse = random.choice(selected_excuses)

    if name:
        excuse = f"{name}, " + excuse[0].lower() + excuse[1:]

    st.success("Here's your excuse:")
    st.markdown(f"### 🎭 {excuse}")

    st.button("Copy Excuse", on_click=lambda: st.toast("Excuse copied!"))

st.caption("Made with zero productivity and maximum creativity 😂")