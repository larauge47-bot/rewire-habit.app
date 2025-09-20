import streamlit as st

def main():
    st.title("🧠 Kişisel Alışkanlık Kırma Simülasyonu")

    if 'day' not in st.session_state:
        st.session_state.day = 1
        st.session_state.habit_strength = 1.0
        st.session_state.dopamine_level = 0.5
        st.session_state.behavior_history = []
        st.session_state.reward_threshold = 0.8
        st.session_state.old_habit = ''
        st.session_state.new_behavior = ''
        st.session_state.finished = False

    if st.session_state.day == 1:
        st.write("Öncelikle alışkanlığını ve yeni davranışını belirt.")
        st.session_state.old_habit = st.text_input("Kırmak istediğin alışkanlık nedir?")
        st.session_state.new_behavior = st.text_input("Onun yerine koymak istediğin yeni davranış nedir?")

        if st.session_state.old_habit and st.session_state.new_behavior:
            if st.button("Başla"):
                st.session_state.day = 1
                st.experimental_rerun()

    elif not st.session_state.finished:
        st.write(f"📅 Gün {st.session_state.day}")
        st.write(f"**Alışkanlık kuvveti:** {st.session_state.habit_strength:.2f}")
        st.write(f"**Dopamin seviyesi:** {st.session_state.dopamine_level:.2f}")

        choice = st.radio(
            "Bugün ne yapmak istersin?",
            (st.session_state.old_habit + " (Eski alışkanlık)", st.session_state.new_behavior + " (Yeni davranış)"),
        )

        if st.button("Seçimini Kaydet"):
            if choice.startswith(st.session_state.old_habit):
                behavior = "old_habit"
                st.session_state.dopamine_level = max(0.0, st.session_state.dopamine_level - 0.05)
                st.session_state.habit_strength = min(1.0, st.session_state.habit_strength + 0.02)
            else:
                behavior = "new_behavior"
                st.session_state.dopamine_level = min(1.0, st.session_state.dopamine_level + 0.1)
                if st.session_state.dopamine_level > st.session_state.reward_threshold:
                    st.session_state.habit_strength = max(0.0, st.session_state.habit_strength - 0.05)

            st.session_state.behavior_history.append(behavior)

            if st.session_state.day >= 30:
                st.session_state.finished = True
            else:
                st.session_state.day += 1

            st.experimental_rerun()

    else:
        old_count = st.session_state.behavior_history.count("old_habit")
        new_count = st.session_state.behavior_history.count("new_behavior")
        st.write("### 📊 Simülasyon Özeti:")
        st.write(f"🧠 Alışkanlık: {st.session_state.old_habit}")
        st.write(f"🌱 Yeni Davranış: {st.session_state.new_behavior}")
        st.write(f"- 30 gün içinde:")
        st.write(f"  • Eski alışkanlığı seçtiğin gün: {old_count}")
        st.write(f"  • Yeni davranışı seçtiğin gün: {new_count}")
        st.write(f"📉 Final Alışkanlık Kuvveti: {st.session_state.habit_strength:.2f}")
        st.write(f"💊 Final Dopamin Seviyesi: {st.session_state.dopamine_level:.2f}")
        st.write("🎯 Her yeni davranış, eski alışkanlığı biraz daha zayıflatır.")

if __name__ == "__main__":
    main()
