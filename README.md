# Clary.AI - Bot Discord para Produtividade

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=fff)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=fff)](https://discord.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Bot Discord para automatizar mensagens, resumos, insights e alertas para times técnicos.

---

## 📋 Sobre

O **Clary.AI** é um bot de produtividade para equipes de desenvolvimento, com resumos diários automáticos, integração com Notion e GitHub, e comandos para gestão de progresso e ideias.

## 🚀 Como rodar

### Pré-requisitos

- Python 3.10+
- Conta no [Discord Developer Portal](https://discord.com/developers/applications)
- Token do bot Discord

### Instalação

```bash
# Clone o repositório
git clone https://github.com/sthevan027/clary.IA.git
cd clary.IA

# Instale as dependências
pip install -r requirements.txt
pip install notion-client flask  # para integrações opcionais

# Configure o .env
# DISCORD_TOKEN=seu_token_aqui
# CHANNEL_ID=id_do_canal_aqui
# NOTION_TOKEN=opcional
# NOTION_DATABASE_ID=opcional
```

### Executar

```bash
python src/bot.py
```

## 🛠️ Tecnologias

| Biblioteca | Uso |
|------------|-----|
| discord.py | API do Discord |
| python-dotenv | Variáveis de ambiente |
| apscheduler | Tarefas agendadas |
| notion-client | Integração Notion (opcional) |
| Flask | Webhooks GitHub (opcional) |

## 📱 Comandos disponíveis

| Comando | Descrição |
|---------|-----------|
| `!ping` | Testa se o bot está online |
| `!addresumo <msg>` | Adiciona ao resumo do dia |
| `!resumo [data]` | Mostra resumo do dia ou data |
| `!progresso` | Mostra entregas do dia |
| `!ideia <msg>` | Salva ideia técnica |
| `!estudo` | Sugere tema de estudo |
| `!constancia` | Mostra constância semanal |
| `!resumo_semana` | Resumo dos últimos 7 dias |
| `!resumo_mes` | Resumo dos últimos 30 dias |
| `!settemplate` | Define template do resumo |
| `!exportar` | Exporta resumos do mês |
| `!lembrete HH:MM msg` | Agenda lembrete |

## 🔗 Integrações

- **Notion**: Salva resumos em database — configure `NOTION_TOKEN` e `NOTION_DATABASE_ID`
- **GitHub**: Alertas de PR/deploy via webhook em `http://servidor:5000/github-webhook`

---

**Desenvolvido por [Sthevan Santos](https://github.com/sthevan027)**
