import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Memory Challenge Game",
    page_icon="🧠",
    layout="centered"
)

# Initialize session variables
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "numbers" not in st.session_state:
    st.session_state.numbers = []

if "score" not in st.session_state:
    st.session_state.score = 0

if "best_score" not in st.session_state:
    st.session_state.best_score = 0

if "game_finished" not in st.session_state:
    st.session_state.game_finished = False


# Title
st.title("🧠 Memory Challenge Game")

st.write(
    "Test your memory! Remember the numbers shown on the screen "
    "and enter them after they disappear."
)

st.divider()

# Game settings
st.subheader("⚙️ Game Settings")

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if difficulty == "Easy":
    number_count = 4
    display_time = 5

elif difficulty == "Medium":
    number_count = 6
    display_time = 4

else:
    number_count = 8
    display_time = 3


st.info(
    f"Difficulty: {difficulty} | "
    f"Numbers: {number_count} | "
    f"Memory Time: {display_time} seconds"
)

st.divider()


# Start game
if not st.session_state.game_started:

    st.subheader("🎮 Ready to Play?")

    st.write(
        "Click the button below. A set of numbers will appear. "
        "Try to remember them before they disappear."
    )

    if st.button("🚀 Start Memory Challenge"):

        st.session_state.numbers = random.sample(
            range(10, 100),
            number_count
        )

        st.session_state.game_started = True
        st.session_state.game_finished = False
        st.session_state.score = 0

        st.rerun()


# Display memory numbers
if st.session_state.game_started and not st.session_state.game_finished:

    st.subheader("👀 Remember These Numbers")

    number_text = "   ".join(
        str(number) for number in st.session_state.numbers
    )

    st.markdown(
        f"""
        <div style="
            font-size:40px;
            font-weight:bold;
            text-align:center;
            padding:30px;
            border:2px solid #888;
            border-radius:15px;
        ">
        {number_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.warning(
        f"⏱️ You have {display_time} seconds to memorize them!"
    )

    time.sleep(display_time)

    st.session_state.game_finished = True
    st.rerun()


# Answer section
if st.session_state.game_started and st.session_state.game_finished:

    st.subheader("✍️ Enter the Numbers You Remembered")

    st.write(
        "Enter the numbers in the same order, separated by spaces."
    )

    user_answer = st.text_input(
        "Your Answer",
        placeholder="Example: 25 67 43 81"
    )

    if st.button("✅ Check My Answer"):

        correct_numbers = [
            str(number)
            for number in st.session_state.numbers
        ]

        user_numbers = user_answer.split()

        correct_count = 0

        for i in range(
            min(len(correct_numbers), len(user_numbers))
        ):
            if user_numbers[i] == correct_numbers[i]:
                correct_count += 1

        st.session_state.score = correct_count

        if correct_count > st.session_state.best_score:
            st.session_state.best_score = correct_count

        st.divider()

        st.subheader("📊 Your Result")

        st.metric(
            "Score",
            f"{correct_count}/{number_count}"
        )

        st.metric(
            "Best Score",
            f"{st.session_state.best_score}/{number_count}"
        )

        percentage = (
            correct_count / number_count
        ) * 100

        st.progress(percentage / 100)

        st.write(
            f"### 🎯 Accuracy: {percentage:.1f}%"
        )

        if percentage == 100:
            st.success(
                "🏆 Excellent! You remembered everything correctly!"
            )

        elif percentage >= 60:
            st.success(
                "👏 Good job! Your memory is strong."
            )

        elif percentage >= 40:
            st.warning(
                "🙂 Nice attempt! Try again to improve your score."
            )

        else:
            st.error(
                "💪 Keep practicing! You can improve your memory."
            )

        st.write(
            "Correct sequence:",
            " ".join(correct_numbers)
        )

        st.divider()

        if st.button("🔄 Play Again"):

            st.session_state.game_started = False
            st.session_state.game_finished = False
            st.session_state.numbers = []
            st.session_state.score = 0

            st.rerun()


# Sidebar
with st.sidebar:

    st.header("🧠 About the Game")

    st.write(
        "Memory Challenge Game is an interactive Python "
        "application developed using Streamlit."
    )

    st.subheader("🎯 Objective")

    st.write(
        "Remember the numbers displayed on the screen "
        "and reproduce them correctly."
    )

    st.subheader("📈 Scoring")

    st.write(
        "Your score is based on how many numbers you "
        "remember in the correct position."
    )

    st.divider()

    st.write(
        "Developed using Python + Streamlit"
    )