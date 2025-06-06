# 🛫 SimBrief Flight Planner (Flask App)

Este é um aplicativo web feito em **Python com Flask** que consome a API da **SimBrief** para exibir informações detalhadas sobre planos de voo. Também possui páginas auxiliares para pesquisa de METAR, download de AIRAC e uma seção "Sobre".

---

## 🌐 Funcionalidades

- Busca e exibe dados do plano de voo por ID do piloto (SimBrief).
- Extrai e mostra informações como:
  - Código ICAO de origem, destino e alternado
  - Runways, rota, nível de voo
  - METARs, combustível, carga útil e passageiros
- Página para consulta de METAR
- Página para download de AIRAC
- Página "Sobre"

---

## 🚀 Tecnologias Usadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML5 / CSS3 / JavaScript
- [SimBrief API (JSON)](https://www.simbrief.com/)
- Regex (`re`) para extração de dados

---

## 🛠️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# (Recomendado) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o app
python app.py
