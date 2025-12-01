📌 Resolvendo Códigos em Python com GitHub Copilot








Este projeto foi desenvolvido como parte do desafio “Resolvendo Códigos em Python com GitHub Copilot” da Digital Innovation One (DIO).
O objetivo é demonstrar, na prática, como o GitHub Copilot pode auxiliar no desenvolvimento de algoritmos em Python, sugerindo soluções, acelerando a escrita de código e ajudando a aplicar boas práticas de programação.

🔥 Visão Geral do Projeto

O repositório apresenta:

✔ Um conjunto de algoritmos fundamentais desenvolvidos com apoio do Copilot
✔ Um menu interativo para execução dos algoritmos
✔ Testes automatizados com pytest
✔ Documentação completa, incluindo decisões técnicas e melhorias futuras
✔ Código limpo, modularizado e com type hints modernos

🧠 Tecnologias e Ferramentas Utilizadas

Python 3.10+

GitHub Copilot (autocompletar, sugestões, docstrings e testes)

Pytest para validações automatizadas

Git & GitHub para versionamento

Boas práticas de Clean Code + type hints

📁 Estrutura do Repositório
resolvendo-codigos-python-com-github-copilot/
├── src/
│   ├── algorithms.py          # Funções e algoritmos principais
│   └── main.py                # Aplicação CLI para rodar os algoritmos
├── tests/
│   └── test_algorithms.py     # Testes automatizados
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação completa

🧩 Algoritmos Implementados

Os seguintes algoritmos foram criados ou otimizados utilizando o GitHub Copilot como pair programmer:

🔹 soma_numeros_pares(lista)

Retorna a soma de todos os números pares de uma lista.

🔹 eh_palindromo(texto)

Verifica se uma string é palíndromo, ignorando espaços e pontuações.

🔹 contagem_caracteres(texto)

Cria um dicionário com a frequência de cada caractere na string.

🔹 fibonacci(n)

Gera os n primeiros termos da sequência de Fibonacci.

🔹 ordenar_numeros(lista)

Ordena os números em ordem crescente.

Todos incluem type hints, docstrings e exemplos.

🚀 Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/SEU-USUARIO/resolvendo-codigos-python-com-github-copilot.git
cd resolvendo-codigos-python-com-github-copilot

2️⃣ (Opcional) Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Rodar o menu principal
python -m src.main

🧪 Testes Automatizados

Os testes foram gerados com ajuda do Copilot e cobrem os principais casos das funções.

Executar os testes:
pytest -v


Exemplos verificados:

Soma correta dos números pares

Palíndromos com e sem espaços

Frequência de caracteres

Sequência de Fibonacci

Ordenação correta de inteiros

🤖 Como o GitHub Copilot foi Utilizado

O Copilot contribuiu em diversas etapas:

✨ Sugestão de códigos iniciais

Estrutura das funções

Comandos simples e loops

Padrões Pythonic

✨ Geração de docstrings e exemplos

Documentação clara e padronizada

Explicação automática dos algoritmos

✨ Criação de testes automatizados

Casos de teste mais completos

Detecção automática de edge cases

✨ Refatorações

Melhoria da legibilidade

Simplificação da lógica

Redução de duplicação

Todo o código foi revisado e ajustado manualmente, garantindo qualidade e clareza.

🧠 Decisões Técnicas

Modularização para facilitar manutenção

Type hints para tornar o código mais legível

Uso de testes como boa prática profissional

Estrutura compatível com futuros upgrades (API, GUI, Web)

🚀 Possíveis Melhorias Futuras

Adicionar interface web com Flask ou FastAPI

Criar dashboard com Streamlit

Gerar documentação automática via Sphinx

Adicionar novos algoritmos avançados

Configurar GitHub Actions (CI/CD) para testes automáticos

Criar badges de cobertura de código (CodeCov)

👤 Autor

Rafael Dos Santos Vicente
📌 GitHub: @RafaelSV9

🏁 Conclusão

Este projeto demonstra como o GitHub Copilot pode atuar como um parceiro de programação, acelerando entregas, aumentando a clareza do código e melhorando a experiência de estudo e desenvolvimento.
