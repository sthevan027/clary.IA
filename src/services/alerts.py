import os
import json

ALERTS_PATH = 'config/alerts.json'

# Carrega alertas customizados
def load_alerts():
    if os.path.exists(ALERTS_PATH):
        with open(ALERTS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "deploy": "🚀 Novo deploy realizado!",
        "pr_merged": "🟢 PR mergeado por {user}",
        "lembrete": "⏰ Lembrete: {mensagem}",
        # outros alertas padrão...
    }

# Salva alertas customizados
def save_alerts(alerts):
    if not os.path.exists('config'):
        os.makedirs('config')
    with open(ALERTS_PATH, 'w', encoding='utf-8') as f:
        json.dump(alerts, f, ensure_ascii=False, indent=2) 