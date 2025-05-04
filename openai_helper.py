import openai

# Tu clave API aquí
import os
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def get_detailed_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente que explica de forma clara, sencilla y tranquilizadora temas de radioterapia para pacientes oncológicos. No das diagnósticos ni tratamientos."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error al conectar con OpenAI: {e}"
