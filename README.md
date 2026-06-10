# 🛡️ ZenithSentry - Bootcamp II (Etapa Intermediária)

> **Link da Aplicação (Deploy):** [🚀 ACESSAR ZENITHSENTRY WEB](https://zenithsentry.streamlit.app)

| Status do Projeto | Versão | Pipeline | Branch |
| :--- | :--- | :--- | :--- |
| ![CI ZenithSentry](https://github.com/mihoneybee/ZenithSentry/actions/workflows/main.yml/badge.svg) | ![Version](https://img.shields.io/badge/version-1.1.0-blue) | ![Streamlit](https://img.shields.io/badge/Deploy-Streamlit-FF4B4B) | `entrega-intermediaria` |

---

## 🎯 Visão Geral da Entrega
Esta etapa marca a evolução do ZenithSentry de um script local para uma solução conectada e acessível. O foco foi implementar o ciclo completo de desenvolvimento profissional: gestão de demandas, ramificação de código, integração com serviços externos e entrega contínua.

### ✅ Critérios Atendidos:
1. **Gestão de Demandas:** Criação e resolução da Issue #1 para rastreabilidade de novas funcionalidades.
2. **Estratégia de Branching:** Todo o desenvolvimento foi realizado na branch `entrega-intermediaria`.
3. **Consumo de API Pública:** Integração com a **ZenQuotes API** para fornecer suporte emocional personalizado baseado na carga horária do utilizador.
4. **Teste de Integração:** Implementação de testes automatizados que validam a comunicação com a API externa.
5. **Deploy Cloud:** Publicação da aplicação via **Streamlit Cloud**, permitindo o acesso público.

---

## 🛠️ Tecnologias Adicionadas
* **Python 3.x**
* **Streamlit:** Framework para a interface web e deploy.
* **Requests:** Biblioteca para consumo de APIs REST.
* **Pytest:** Framework para testes unitários e de integração.

---

## 🧪 Qualidade e Testes
O projeto utiliza **GitHub Actions** para garantir que cada alteração passe pelos seguintes critérios:
* **Linting:** Validação de estilo de código com Flake8.
* **Testes de Integração:** O arquivo `test_integration.py` garante que a conexão com a ZenQuotes API está ativa e retornando dados válidos.

---

## 🚀 Como Executar Localmente
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação web
streamlit run app.py
```
