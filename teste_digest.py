"""
Script de teste: força o envio do digest diário pro Telegram,
sem esperar o horário certo (DIGEST_HORA_UTC).

Uso:
    python teste_digest.py brasil
    python teste_digest.py internacional
"""
import sys

from database.database import (
    iniciar_db,
    marcar_digest_enviado,
    obter_vagas_pendentes_digest,
)
from notifier.telegram import enviar_digest
from perfis import PERFIL_BR, PERFIL_INTL

PERFIS = {
    "brasil": PERFIL_BR,
    "internacional": PERFIL_INTL,
}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in PERFIS:
        print("Uso: python teste_digest.py [brasil|internacional]")
        sys.exit(1)

    perfil = PERFIS[sys.argv[1]]

    iniciar_db()

    vagas_pendentes = obter_vagas_pendentes_digest(perfil.chave)
    print(f"[{perfil.nome}] {len(vagas_pendentes)} vaga(s) pendente(s) no digest.")

    if not vagas_pendentes:
        print("Nenhuma vaga pendente — nada pra enviar. Rode o main.py --once primeiro.")
        return

    print("Enviando digest de teste pro Telegram...")
    sucesso = enviar_digest(vagas_pendentes, perfil.nome)

    if sucesso:
        marcar_digest_enviado(perfil.chave)
        print(f"✅ Digest enviado com sucesso! ({len(vagas_pendentes)} vaga(s))")
        print("Confira seu Telegram.")
    else:
        print("❌ Falha ao enviar. Confira TELEGRAM_BOT_TOKEN e TELEGRAM_CHAT_ID no .env")


if __name__ == "__main__":
    main()