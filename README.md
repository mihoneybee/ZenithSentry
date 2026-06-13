# 🛡️ ZenithSentry

O **ZenithSentry** é uma aplicação web inteligente desenvolvida em Python com a biblioteca **Streamlit**, projetada para atuar no monitoramento e gerenciamento de dados de saúde e bem-estar (como horas trabalhadas, status de saúde e mensagens de suporte). O sistema une uma interface visual interativa e fluida a um ecossistema de banco de dados robusto e seguro na nuvem.

🚀 **Acesse a aplicação em produção:** [ZenithSentry no Streamlit Cloud](https://zenithsentry.streamlit.app)

---

## 👥 Equipe Desenvolvedora

Conheça os integrantes do grupo responsáveis pela concepção, design, engenharia de software e integração com banco de dados deste projeto:

* [**Gabriela Yasmin da Conceição Viana**](https://github.com/gabrielay-ctrl) — RA: 22505273
* [**Guilherme Neves Lourenço**](https://github.com/TheGNL) — RA: 22509395
* [**Mel Isis Costa Silva**](https://github.com/mihoneybee) — RA: 22508420
* [**Vitor dos Santos Wamburg**](https://github.com/vitorwamburg-ux) — RA: 22510570

---

## 🗄️ Arquitetura e Conexão com o Banco de Dados (Supabase)

Para o armazenamento persistente e seguro das informações da aplicação, implementamos o **Supabase**, uma plataforma de *Backend-as-a-Service (BaaS)* fundamentada em **PostgreSQL**, um dos bancos de dados relacionais mais estáveis e confiáveis do mundo.

### 🛡️ Protocolo de Segurança e Injeção de Dependências
Seguindo rigorosamente as melhores práticas de segurança corporativa e engenharia de software (mitigando riscos de vazamento descritos pela OWASP), **nenhuma credencial de acesso, token ou URL de API foi exposta diretamente no código-fonte público.**

A engenharia de conexão foi isolada em um arquivo especializado chamado `database.py`:
1. **Ambiente Isolado:** Utilizamos o módulo nativo do Python `os` através do método `os.getenv()` para realizar a leitura das credenciais diretamente da memória do servidor.
2. **Camada Local:** Durante a fase de desenvolvimento no ecossistema local (VS Code), as chaves sensíveis residiram de forma estritamente confidencial em um arquivo oculto `.env` (completamente ignorado pelo versionamento do Git).
3. **Produção Nuvem (Streamlit Secrets):** No ambiente definitivo hospedado no **Streamlit Cloud**, as chaves reais de produção `SUPABASE_URL` e `SUPABASE_KEY` foram criptografadas e injetadas de forma invisível através do painel administrativo de **Secrets** do Streamlit.

---

## ⚙️ Como o Banco de Dados Funciona na Aplicação?

A integração opera sob o padrão CRUD (Create e Read) em tempo real por meio da tabela `historico_saude`. O comportamento lógico do banco de dados na aplicação segue o fluxo abaixo:

### 1. Inserção de Dados (Create)
Quando o usuário preenche o formulário na interface visual do Streamlit e submete as informações, a aplicação aciona a função estruturada `salvar_historico(horas, status, mensagem)`. 
* Os dados brutos informados pelo usuário, juntamente com o status calculado de forma analítica pela aplicação, são empacotados em um dicionário.
* A biblioteca cliente do `supabase` realiza um disparo assíncrono enviando uma requisição do tipo `.insert(dados).execute()`.
* O PostgreSQL do Supabase processa e armazena os dados, gerando automaticamente chaves primárias únicas (`id`) e carimbos de data/hora (`created_at`).

### 2. Recuperação de Histórico (Read)
A aplicação conta com uma camada de visualização de auditoria. Para alimentar essa seção:
* É invocada a função `ler_historico()`, que executa uma query estruturada na tabela através do comando `.select("*").order("created_at", desc=True).execute()`.
* O banco de dados retorna uma coleção estruturada em formato JSON contendo todos os registros já salvos.
* O Streamlit captura esses dados e os renderiza instantaneamente na tela do usuário de forma legível em tabelas de dados ou cartões informativos, sempre organizando do registro mais recente para o mais antigo.

---

## 🛠️ Tecnologias e Dependências Utilizadas

* **Linguagem Principal:** Python 3.x
* **Framework de Interface:** Streamlit (Criação de Web Apps rápidos e reativos)
* **Ecossistema Backend:** Supabase (PostgreSQL Gerenciado em Nuvem)
* **Biblioteca de Integração:** `supabase-py` (Conector e ORM oficial)
