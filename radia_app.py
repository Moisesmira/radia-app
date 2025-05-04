# radia_app.py

import streamlit as st
from openai_helper import get_detailed_response

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        background-color: #e6f0ff;
        padding: 2rem;
    }
    .stButton>button {
        color: white;
        background-color: #4da6ff;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 1.2em;
    }
    </style>
""", unsafe_allow_html=True)

class RADIAChatbot:
    def __init__(self):
        self.categories = {
            "Inicio del tratamiento": {
                "¿Cuándo empezaré el tratamiento?": "Tras el estudio de planificación, te llamaremos para darte la fecha de inicio.",
                "¿Por qué tarda en empezar el tratamiento después de la primera consulta?": "La planificación precisa y los cálculos para tu seguridad requieren varios días."
            },
            "Durante el tratamiento": {
                "¿Duele recibir radioterapia?": "No, la radioterapia es indolora.",
                "¿Cuánto dura cada sesión?": "Cada sesión dura entre 10 y 30 minutos en total.",
                "¿Necesito estar en ayunas para el tratamiento?": "En general, no. Te informaremos si debes hacer alguna preparación específica.",
                "¿Qué ropa debo usar para venir a la radioterapia?": "Usa ropa cómoda, holgada y preferiblemente de algodón.",
                "¿Qué pasa si me siento mal durante la sesión?": "Avísanos. Podemos detener el tratamiento y atenderte."
            },
            "Efectos secundarios": {
                "¿Voy a perder el pelo con la radioterapia?": "Solo si la zona tratada es el cuero cabelludo.",
                "¿Cuándo aparecerán los efectos secundarios?": "Después de varias sesiones, dependiendo del caso.",
                "¿Cómo puedo aliviar la irritación en la piel?": "Usa cremas recomendadas y evita el sol en la zona tratada."
            },
            "Vida diaria y transporte": {
                "¿Podré seguir trabajando durante el tratamiento?": "Sí, si te sientes con energía suficiente.",
                "¿Puedo hacer ejercicio?": "Sí, ejercicio moderado según te sientas.",
                "¿Puedo ducharme y usar jabón normal?": "Sí, con productos suaves, sin frotar la zona tratada.",
                "¿Puedo tomar el sol durante el tratamiento?": "Evítalo en la zona tratada.",
                "¿Voy a ser radiactivo después del tratamiento?": "No, puedes convivir con normalidad.",
                "¿Cómo llego al hospital si tengo dificultades de movilidad?": "Consulta si puedes acceder a transporte sanitario.",
                "¿Necesito pedir cita para cada sesión?": "No, recibirás un calendario de sesiones.",
                "¿Qué pasa si un día no puedo asistir a la sesión?": "Avísanos para reprogramar la sesión."
            },
            "Sexualidad y fertilidad": {
                "¿Puedo mantener relaciones sexuales durante el tratamiento?": "Sí, salvo molestias en caso de radioterapia pélvica.",
                "¿La radioterapia afecta la fertilidad?": "Puede afectar si el tratamiento es en la zona pélvica.",
                "¿La radioterapia puede afectar el deseo sexual?": "Sí, por fatiga o cambios emocionales temporales.",
                "¿Puedo quedar embarazada o dejar embarazada durante el tratamiento?": "No se recomienda. Usa métodos anticonceptivos."
            }
        }

    def get_response(self, category, question):
        return self.categories.get(category, {}).get(question, "Lo siento, no encuentro respuesta para esa pregunta.")

# Aplicación Streamlit
radia = RADIAChatbot()

st.title("🏥 RADIA - Tu asistente en Radioterapia")
st.image("logo_arnau.png", width=200)
st.write("Bienvenido/a al Servicio de Oncología Radioterápica de Lleida.")
st.write("Estoy aquí para ayudarte. Por favor, selecciona una categoría para consultar tus dudas.")

st.divider()

category = st.selectbox("Elige una categoría:", list(radia.categories.keys()))

if category:
    question = st.selectbox("Elige una pregunta:", list(radia.categories[category].keys()))
    if question:
        st.divider()
        response = radia.get_response(category, question)
        st.success(f"💬 {response}")

        # Botón para ampliar información con IA
        if st.button("Ampliar información sobre este tema con IA"):
            with st.spinner("Consultando a nuestro asistente..."):
                detailed_info = get_detailed_response(question)
                st.info(detailed_info)

st.write("\n")
st.info("¿No ves tu pregunta? Por ahora RADIA responde solo a las preguntas más frecuentes.")