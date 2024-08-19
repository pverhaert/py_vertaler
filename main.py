import streamlit as st
import pandas as pd


def load_words_from_excel(file_path):
    # Lees de Excel file in
    df = pd.read_excel(file_path)
    return df['Nederlands'], df['Italiaans']


def main():
    st.title("Italiaanse Woorden Quiz")

    # Upload de Excel file
    uploaded_file = st.file_uploader("Upload een Excel-bestand met Nederlandse en Italiaanse woorden", type=["xlsx"])

    if uploaded_file is not None:
        nederlands, italiaans = load_words_from_excel(uploaded_file)

        score = 0
        total_questions = len(nederlands)

        for nl_word, it_word in zip(nederlands, italiaans):
            user_answer = st.text_input(f"Wat is de Italiaanse vertaling van '{nl_word}'?", key=nl_word)

            if st.button(f"Controleer antwoord voor '{nl_word}'", key=f"button_{nl_word}"):
                if user_answer.strip().lower() == it_word.lower():
                    st.success("Correct! Goed gedaan.")
                    score += 1
                else:
                    st.error(f"Dat is niet juist. Het juiste antwoord is '{it_word}'.")

        st.write(f"Je hebt {score} van de {total_questions} vragen correct beantwoord.")


if __name__ == "__main__":
    main()
