import ollama

try:
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'O que tem nessa imagem?',
            'images': ['image.jpeg']
        }]
    )
    print(response)
except Exception as e:
    print(f"Erro: {e}")
