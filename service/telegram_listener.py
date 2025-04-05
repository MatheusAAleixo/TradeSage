from telegram.ext import ApplicationBuilder, CommandHandler
from config_manager import set_modo, get_modo

TELEGRAM_TOKEN = ""

async def mudar_modo(update, context):
    if context.args:
        novo_modo = context.args[0].lower()
        if novo_modo in ["conservador", "agressivo"]:
            set_modo(novo_modo)
            await update.message.reply_text(f"✅ Modo de análise alterado para: *{novo_modo.upper()}*", parse_mode="Markdown")
        else:
            await update.message.reply_text("❌ Modo inválido. Use `/modo conservador` ou `/modo agressivo`.")
    else:
        await update.message.reply_text("ℹ️ Envie `/modo agressivo` ou `/modo conservador`.")

async def status(update, context):
    modo = get_modo()
    await update.message.reply_text(f"📊 Modo atual: *{modo.upper()}*", parse_mode="Markdown")

def iniciar_escuta():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("modo", mudar_modo))
    app.add_handler(CommandHandler("status", status))

    print("👂 Bot escutando comandos no Telegram...")
    app.run_polling()

if __name__ == "__main__":
    iniciar_escuta()
