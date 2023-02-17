import openai

import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("APIKEY")

def generate_question(topic):
    prompt = f"crie uma pergunta de múltipla escolha sobre {topic} no {level} nível da Taxonomia de Bloom de aprendizagem utilize o link https://pt.wikipedia.org/wiki/Docker_(software) como referência"
    model = "text-davinci-002"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    question = response.choices[0].text.strip()
    return question

topic = "Docker"
level = "primeiro"
question = generate_question(topic)
print(question)
