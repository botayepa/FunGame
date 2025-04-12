import streamlit as st
import random

st.set_page_config(page_title="🐍 Snake Water Gun Game", page_icon="🎮")

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        font-size: 20px;
        height: 3em;
        width: 100%;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🐍 Snake Water Gun Game")
st.subheader("Can you beat the computer? 🤖")
st.markdown("Choose your move:")

choices = {
    "Snake 🐍": 1,
    "Water 💧": -1,
    "Gun 🔫": 0
}

reverse_dict = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

your_choice = st.radio("Select one:", list(choices.keys()), horizontal=True)

if st.button("Play! 🎮"):
    player = choices[your_choice]
    computer = random.choice([-1, 0, 1])
    st.markdown(f"**You chose:** {reverse_dict[player]}")
    st.markdown(f"**Computer chose:** {reverse_dict[computer]}")

    if player == computer:
        st.success("It's a draw! 🤝")
    elif (player == 1 and computer == -1) or \
         (player == 0 and computer == 1) or \
         (player == -1 and computer == 0):
        st.balloons()
        st.success("You Win! 🎉")
    else:
        st.error("You Lose! 😢")

st.markdown("---")
st.markdown("💡 _Tip: Snake drinks water, Water damages gun, Gun kills snake!_")
