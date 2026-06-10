# 🛡️ ZenithSentry

> **Status do Projeto:** [![CI ZenithSentry](https://github.com/mihoneybee/ZenithSentry/actions/workflows/main.yml/badge.svg)](https://github.com/mihoneybee/ZenithSentry/actions)
> ![Version](https://img.shields.io/badge/version-1.0.0-blue)

## 📋 Painel do Projeto

| Atributo | Detalhes |
| :--- | :--- |
| **🎯 Público-Alvo** | Estudantes e Freelancers |
| **💻 Interface** | CLI (Linha de Comando) |
| **🛡️ Qualidade** | Pytest + Linting (Flake8) |
| **🛠️ Pipeline** | GitHub Actions (CI) |

---

## 🎯 Problema Real e Proposta de Valor

No cenário atual de trabalho remoto e estudos intensos, a linha entre a produtividade e o esgotamento tornou-se invisível. Muitos profissionais e estudantes sofrem com o **Burnout** por não monitorarem sua carga horária de forma consciente.

O **ZenithSentry** atua como uma "sentinela" da saúde mental. Ele categoriza a jornada diária em **cinco níveis de risco** progressivos, alertando o usuário quando é necessário fazer pausas ou encerrar o expediente, garantindo que o "ápice" (Zenith) da produtividade não custe o bem-estar do indivíduo.

---

## 🚀 Funcionalidades Principais

* **Registro de Horas:** Entrada simples da carga horária líquida trabalhada no dia.

* **Cálculo Inteligente com 5 Níveis de Classificação:**
  * 🔵 **Azul (0h a 4h):** Carga muito leve. Você pode aumentar sua produtividade se desejar.
  * 🟢 **Verde (4h a 6h):** Ritmo saudável. Seu ritmo está equilibrado e sustentável.
  * 🟡 **Amarelo (6h a 8h):** Atenção. Você está no limite saudável. Considere fazer uma pausa longa.
  * 🟠 **Laranja (8h a 10h):** Risco elevado. Você está entrando em zona de perigo. Considere encerrar em breve.
  * 🔴 **Vermelho (>10h):** Risco crítico. Limite de exaustão atingido. Pare imediatamente!

* **Cores ANSI no Terminal:** Visualização intuitiva com códigos de cores para melhor compreensão visual.

* **Validação Robusta:** Prevenção de entradas negativas ou inconsistentes com mensagens de erro claras.

* **Escalabilidade:** Arquitetura modular pronta para futuras expansões (histórico, gráficos, integrações).

---

## 🛠️ Tecnologias e Boas Práticas

* **Linguagem:** Python 3.10+
* **Testes Automatizados:** Implementados com `pytest` com cobertura completa de todos os níveis e casos extremos.
* **Análise Estática (Linting):** Configurado com `flake8` para garantir conformidade com a PEP 8.
* **CI (Integração Contínua):** Fluxo automatizado via GitHub Actions para validação a cada push.
* **Versionamento Semântico:** Seguindo o padrão `MAJOR.MINOR.PATCH`.
* **Códigos ANSI:** Suporte a cores no terminal compatível com Windows, macOS e Linux.

---

## 📦 Como Instalar e Executar

### Pré-requisitos
- Python 3.10 ou superior
- Git

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/mihoneybee/ZenithSentry.git
cd ZenithSentry
```

### Passo 2: Criar um ambiente virtual (recomendado)

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**No macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar as dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Executar a aplicação

```bash
python main.py
```

### Link da aplicação

```bash
https://zenithsentry.streamlit.app
```

**Exemplo de uso:**
```
--- 🛡️ ZenithSentry: Monitor de Saúde Mental ---
Digite o total de horas trabalhadas hoje: 7

[AMARELO]
Status: Atenção. Você está no limite saudável. Considere fazer uma pausa longa.
```

---

## 🧪 Como Executar os Testes

### Executar todos os testes com cobertura

```bash
pytest -v --cov=src tests/
```

### Executar testes de um arquivo específico

```bash
pytest tests/test_logic.py -v
```

### Executar um teste específico

```bash
pytest tests/test_logic.py::test_nivel_verde_ritmo_saudavel -v
```

### Visualizar cobertura em HTML

```bash
pytest --cov=src --cov-report=html tests/
# Abrir htmlcov/index.html no navegador
```

### Testes disponíveis

A suíte de testes cobre:

- ✅ Todos os 5 níveis de classificação (AZUL, VERDE, AMARELO, LARANJA, VERMELHO)
- ✅ Limites de intervalos para garantir fronteiras corretas
- ✅ Valores especiais (0 horas, valores muito altos)
- ✅ Validação de entradas negativas
- ✅ Códigos ANSI de cores
- ✅ Funções auxiliares de formatação

**Total de testes:** 30+ casos cobertos

---

## 📊 Estrutura do Projeto

```
ZenithSentry/
│
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
├── VERSION                 # Versão atual do projeto
├── README.md              # Este arquivo
│
├── src/
│   ├── __init__.py        # Inicializador do pacote
│   └── logic.py           # Lógica principal de cálculo de status
│
└── tests/
    ├── __init__.py        # Inicializador do pacote de testes
    └── test_logic.py      # Testes automatizados
```

---

## 🔧 Análise Estática (Linting)

Para garantir conformidade com PEP 8, execute:

```bash
flake8 src/ tests/ main.py --max-line-length=100
```

---

## 🤝 Contribuição

Agradecemos interesse em contribuir para o **ZenithSentry**! Aqui estão as orientações básicas para novos colaboradores:

### Como Contribuir

1. **Fork o repositório**
   ```bash
   # Clique no botão "Fork" no GitHub
   ```

2. **Clone seu fork**
   ```bash
   git clone https://github.com/seu-usuario/ZenithSentry.git
   cd ZenithSentry
   ```

3. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/minha-feature
   ```

4. **Faça suas alterações e commits**
   ```bash
   git add .
   git commit -m "Adiciona: descrição clara da mudança"
   ```

5. **Envie para seu fork**
   ```bash
   git push origin feature/minha-feature
   ```

6. **Abra um Pull Request**
   - Descreva claramente o propósito da mudança
   - Referencie issues relacionadas
   - Certifique-se que todos os testes passam

### Diretrizes

- **Código:** Siga a PEP 8. Use `flake8` para validar.
- **Testes:** Adicione testes para novas funcionalidades. Mantenha cobertura acima de 80%.
- **Commit:** Use mensagens descritivas em português ou inglês.
- **Documentação:** Atualize o README e docstrings quando necessário.
- **Python:** Mantenha compatibilidade com Python 3.10+.

### Áreas para Contribuição

- ✨ **Novas Features:** Histórico de monitoramento, exportação de dados, gráficos.
- 🐛 **Bug Fixes:** Reporte problemas na seção de Issues.
- 📚 **Documentação:** Melhorias no README e comentários de código.
- 🧪 **Testes:** Aumente cobertura e adicione novos casos de teste.
- 🌐 **Internacionalização:** Suporte para outros idiomas.

### Código de Conduta

- Seja respeitoso com todos os colaboradores
- Feedbacks construtivos e objetivos
- Não tolerância a discriminação de qualquer tipo

---

## 📝 Versionamento

O projeto segue **Versionamento Semântico (SemVer)**:

- **MAJOR:** Mudanças incompatíveis na API
- **MINOR:** Novas funcionalidades compatíveis
- **PATCH:** Correções de bugs

**Versão atual:** `1.0.0` (confira em [VERSION](VERSION))

---

## 📄 Licença

Este projeto está sob licença MIT. Veja detalhes em [LICENSE](LICENSE) (se aplicável).

---

## 👨‍💻 Autores

- **Desenvolvedor Principal:** [mihoneybee](https://github.com/mihoneybee)

---

## 🔗 Links Úteis

- 📖 [Documentação Python](https://docs.python.org/3/)
- 🧪 [Documentação Pytest](https://docs.pytest.org/)
- 🔍 [Documentação Flake8](https://flake8.pycqa.org/)
- 🎯 [GitHub Actions](https://github.com/features/actions)

---

## 💬 Feedback e Suporte

- **Encontrou um bug?** Abra uma [Issue](https://github.com/mihoneybee/ZenithSentry/issues)
- **Tem sugestões?** Vamos conversar nos [Discussions](https://github.com/mihoneybee/ZenithSentry/discussions)
- **Quer contribuir?** Veja a seção [Contribuição](#-contribuição)

---

**Última atualização:** Junho de 2026  
**Status:** ✅ Ativo e em desenvolvimento contínuo
