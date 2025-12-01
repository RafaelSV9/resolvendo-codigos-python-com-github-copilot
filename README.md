Resolvendo Códigos em Python com GitHub Copilot

Este repositório foi desenvolvido como parte do desafio “Resolvendo Códigos em Python com o GitHub Copilot”, da Digital Innovation One (DIO).
O objetivo é demonstrar, na prática, como o GitHub Copilot pode auxiliar na escrita, refatoração, documentação e testes de algoritmos em Python, aumentando significativamente a produtividade.

🎯 Objetivos do Projeto

Aplicar algoritmos básicos e intermediários em Python.

Demonstrar o uso real do GitHub Copilot no processo de desenvolvimento.

Organizar o código de forma modular e escalável.

Utilizar testes automatizados para validar as implementações.

Documentar todo o raciocínio técnico e boas práticas.

Versionar o projeto no GitHub com um repositório limpo, claro e bem estruturado.

📁 Estrutura do Projeto
resolvendo-codigos-python-com-github-copilot/
├── src/
│   ├── algorithms.py          # Módulo com todos os algoritmos do projeto
│   └── main.py                # Menu interativo para execução dos algoritmos
├── tests/
│   └── test_algorithms.py     # Testes automatizados com pytest
├── requirements.txt           # Dependências do projeto
└── README.md                  # Este arquivo

🧠 Algoritmos Implementados

Os seguintes algoritmos foram desenvolvidos com o apoio do GitHub Copilot:

Função	Descrição
soma_numeros_pares	Soma apenas os números pares de uma lista.
eh_palindromo	Verifica se uma string é um palíndromo, ignorando formatação.
contagem_caracteres	Conta a frequência de cada caractere de um texto.
fibonacci	Gera uma sequência de Fibonacci de tamanho N.
ordenar_numeros	Ordena uma lista de números inteiros.

Todas as funções possuem docstrings, exemplos e foram implementadas com boas práticas.

🚀 Execução do Projeto
1️⃣ Clonar o repositório
git clone https://github.com/SEU_USUARIO/resolvendo-codigos-python-com-github-copilot.git
cd resolvendo-codigos-python-com-github-copilot

2️⃣ Criar ambiente virtual (opcional, recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate (Windows)

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar o projeto
python -m src.main

🧪 Testes Automatizados

O projeto inclui testes criados com o apoio do Copilot.

Para executá-los:

pytest -v


Os testes incluem:

Casos simples

Casos edge

Comportamento esperado das funções

Isso deixa seu projeto muito mais profissional.

🤖 Como o GitHub Copilot foi utilizado

Durante o desenvolvimento, o Copilot ajudou em:

Geração de trechos de lógica para algoritmos.

Sugestões de docstrings e exemplos.

Autocomplete inteligente para listas, loops e condicionais.

Criação de casos de testes no pytest.

Melhoria da formatação e limpeza do código.

Todo código gerado foi revisado, ajustado e adaptado antes de ser incluído no repositório.

🧩 Decisões Técnicas

Python 3.10+ com type hints modernos.

Modularização para manter código organizado.

Simplicidade no design, focado em clareza.

Inclusão de testes automatizados (boa prática profissional).

Código 100% compatível com ferramentas de CI/CD (ex.: GitHub Actions).

✨ Possíveis Melhorias Futuras

Interface gráfica com Tkinter.

API REST com FastAPI.

Mais desafios e algoritmos avançados.

Deploy em nuvem (Render / Railway).

Dashboard web com Streamlit.

👨‍💻 Autor

Rafael Vicente
📌 GitHub: RafaelSV
