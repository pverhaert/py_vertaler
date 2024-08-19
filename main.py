import streamlit as st
import pandas as pd
import random


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

        # Optie om de richting van de vertaling te kiezen
        direction = st.radio("Kies de richting van de vertaling:",
                             ("Nederlands naar Italiaans", "Italiaans naar Nederlands"))

        # Invoerveld voor het aantal vragen
        num_questions = st.number_input("Aantal vragen:", min_value=1, max_value=len(nederlands), value=10, step=1)

        # Initialiseer of reset de sessiestatus voor de vragenlijst
        if 'selected_pairs' not in st.session_state or st.button(
                "Start de test") or 'direction' not in st.session_state or st.session_state.direction != direction:
            # Combineer de woorden in een lijst van tuples en schud deze
            word_pairs = list(zip(nederlands, italiaans))
            random.shuffle(word_pairs)
            # Selecteer het aantal vragen dat de gebruiker heeft gekozen
            st.session_state.selected_pairs = word_pairs[:num_questions]
            st.session_state.score = 0  # Reset de score bij het opnieuw starten
            st.session_state.direction = direction  # Sla de huidige richting op
            st.session_state.answered = [False] * num_questions  # Houd bij welke vragen al beantwoord zijn

        score = st.session_state.score

        for idx, (nl_word, it_word) in enumerate(st.session_state.selected_pairs):
            if direction == "Nederlands naar Italiaans":
                question_word = nl_word
                correct_answer = it_word
            else:
                question_word = it_word
                correct_answer = nl_word

            # Disable het invulveld als de vraag al beantwoord is
            user_answer = st.text_input(
                f"Wat is de vertaling van '{question_word}'?",
                key=f"input_{idx}",
                disabled=st.session_state.answered[idx]
            )

            # Gebruik columns om de knop en het feedbackbericht naast elkaar te plaatsen
            col1, col2 = st.columns([2, 3])
            with col1:
                if st.button(f"Controleer antwoord voor '{question_word}'", key=f"button_{idx}"):
                    if not st.session_state.answered[idx]:  # Controleer of de vraag al beantwoord is
                        if user_answer.strip().lower() == correct_answer.lower():
                            st.session_state[f"feedback_{idx}"] = "success"
                            st.session_state.score += 1  # Verhoog de score alleen als het antwoord correct is
                        else:
                            st.session_state[f"feedback_{idx}"] = "error"
                        st.session_state.answered[idx] = True  # Markeer de vraag als beantwoord

            with col2:
                feedback = st.session_state.get(f"feedback_{idx}", None)
                if feedback == "success":
                    st.success("Correct! Goed gedaan.")
                elif feedback == "error":
                    st.error(f"Dat is niet juist. Het juiste antwoord is '{correct_answer}'.")

        st.write(f"Je hebt {st.session_state.score} van de {num_questions} vragen correct beantwoord.")


if __name__ == "__main__":
    main()
