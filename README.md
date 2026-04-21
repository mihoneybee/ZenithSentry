# 🛡️ ZenithSentry

> **Status do Projeto:** > [![CI ZenithSentry](https://github.com/mihoneybee/ZenithSentry/actions/workflows/main.yml/badge.svg)](https://github.com/mihoneybee/ZenithSentry/actions)
> ![Version](https://img.shields.io/badge/version-1.0.0-blue)

## 📋 Painel do Projeto

| Atributo | Detalhes |
| :--- | :--- |
| **🎯 Público-Alvo** | Estudantes e Freelancers |
| **💻 Interface** | CLI (Linha de Comando) |
| **🛡️ Qualidade** | Pytest + Linting (Flake8) |
| **🛠️ Pipeline** | GitHub Actions (CI) |
| **⚖️ Licença** | MIT |

---

## 🎯 Problema Real e Proposta de Valor
No cenário atual de trabalho remoto e estudos intensos, a linha entre a produtividade e o esgotamento tornou-se invisível. Muitos profissionais e estudantes sofrem com o **Burnout** por não monitorarem sua carga horária de forma consciente.

O **ZenithSentry** atua como uma "sentinela" da saúde mental. Ele categoriza a jornada diária em níveis de risco, alertando o usuário quando é necessário fazer pausas ou encerrar o expediente, garantindo que o "ápice" (Zenith) da produtividade não custe o bem-estar do indivíduo.

---

## 🚀 Funcionalidades Principais
* **Registro de Horas:** Entrada simples da carga horária líquida.
* **Cálculo de Status de Saúde:**
    * 🟢 **Verde (até 6h):** Ritmo equilibrado e saudável.
    * 🟡 **Amarelo (6h a 9h):** Atenção! Alerta para pausas longas.
    * 🔴 **Vermelho (acima de 9h):** Risco Crítico. Recomendação de parada imediata.
* **Prevenção de Erros:** Validação de dados para impedir entradas negativas ou inconsistentes.

---

## 🛠️ Tecnologias e Boas Práticas
* **Linguagem:** Python 3.10+
* **Testes Automatizados:** Implementados com `pytest` cobrindo caminhos felizes e casos de erro.
* **Análise Estática (Linting):** Configurado com `flake8` para garantir conformidade com a PEP 8.
* **CI (Integração Contínua):** Fluxo automatizado via GitHub Actions para validação a cada push.
* **Versionamento Semântico:** Seguindo o padrão `MAJOR.MINOR.PATCH`.

---

## 📦 Como Instalar e Executar

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/mihoneybee/ZenithSentry.git](https://github.com/mihoneybee/ZenithSentry.git)

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação web
streamlit run app.py
