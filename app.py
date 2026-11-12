from pathlib import Path
import joblib
import streamlit as st

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model.joblib"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

st.set_page_config(page_title="Пікір көңіл күйі", page_icon="💬")
st.title("💬 Қазақша / орысша пікір көңіл күйін анықтау")
st.write("Пікірді енгізіңіз. Модель оның жалпы реңкін оң, бейтарап немесе теріс деп болжайды.")
st.info("Дерек үлгісі шағын оқу жиынына негізделген. Нәтижені нақты тұтынушы пікірі ретінде қабылдамаңыз.")
text = st.text_area("Пікір мәтіні", placeholder="Мысалы: Қызметкерлер сыпайы, бәрі ұнады", max_chars=1000)
if st.button("Талдау", type="primary"):
    if not text.strip():
        st.warning("Алдымен пікір мәтінін енгізіңіз.")
    else:
        model = load_model()
        label = model.predict([text.strip()])[0]
        probabilities = model.predict_proba([text.strip()])[0]
        confidence = float(max(probabilities))
        names = {"positive": "Оң 😊", "neutral": "Бейтарап 😐", "negative": "Теріс 🙁"}
        st.subheader(f"Нәтиже: {names[label]}")
        st.caption(f"Модельдің ең жоғары ықтималдығы: {confidence:.1%}. Бұл сенімділіктің толық кепілі емес.")
        st.write("Кіру → TF-IDF мәтін векторлары → Logistic Regression → сынып болжамы")
st.caption("Жеке дерек енгізбеңіз: қолданба пікірді сақтамайды және сыртқы қызметке жібермейді.")
