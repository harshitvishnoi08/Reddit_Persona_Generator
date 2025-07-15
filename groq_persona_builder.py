# groq_persona_builder.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chunk_data(data, chunk_size=3000):
    """
    Splits Reddit data into chunks suitable for LLMs.
    """
    chunks = []
    current_chunk = ""

    for item in data:
        entry = f"{item['content']} [source: {item['permalink']}]\n\n"
        if len(current_chunk) + len(entry) > chunk_size:
            chunks.append(current_chunk)
            current_chunk = entry
        else:
            current_chunk += entry

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def generate_persona_from_chunk(chunk):
    """
    Sends a chunk to Groq LLM and returns the persona insights.
    """
    system_prompt = (
        "You are a behavioral analyst. Analyze the Reddit content below and infer the following about the user:\n"
        "- Interests\n- Writing style\n- Political or ideological views\n- Humor/sarcasm\n- Emotional tone\n"
        "Provide citations using [source: <link>] wherever possible.\n\n"
    )

    response = client.chat.completions.create(
        model="gemma2-9b-it",  # You can also use "llama3-8b-8192"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": chunk}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


def build_persona(data):
    """
    Builds full persona from Reddit data.
    """
    chunks = chunk_data(data)
    full_persona = ""

    for i, chunk in enumerate(chunks):
        print(f"🔍 Processing chunk {i+1}/{len(chunks)}...")
        persona_part = generate_persona_from_chunk(chunk)
        #full_persona += f"\n\n--- Persona Chunk {i+1} ---\n{persona_part}"

    return persona_part
