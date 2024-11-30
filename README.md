# E_Prompts
Prompts em ação - Engenharia de prompts para leitos / Prompts em ação 2 - Engenharia de prompts

https://ollama.com/search
ollama run llama3.2
ollama run llama3.2-vision

termina:
ollama --version
python  (obtem a versão do phyton instalado previamente)

pip install uv (isntalador que criara as VM's e fara a magica acontecer)

uv init (inicializa dentro do projeto criando todas as dependencias inciais com um hello word em phyton)

Dentro do arquivo pyproject.toml : 
uv add ollama

neste momento deve ser adicionado a maquina virtual ".venv" no projeto

Exemplo de codigo para utilizar :
import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['image.jpg']
    }]
)

print(response)
