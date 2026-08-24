"""
Teste minimo: manda so uma mensagem de texto simples pro Telegram,
pra confirmar se TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID estao certos
(sem entrar na logica de digest/tamanho de mensagem).

Uso:
    python teste_telegram_simples.py
"""
from notifier.telegram import enviar_mensagem

if __name__ == "__main__":
    print("Enviando mensagem de teste...")
    sucesso = enviar_mensagem("🔧 Teste do JobRadar — se você recebeu isso, o Telegram está configurado certo!")
    if sucesso:
        print("✅ Mensagem enviada! Confira seu Telegram.")
    else:
        print("❌ Falha. TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID incorretos no .env.")