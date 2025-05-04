from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working. You're awesome.")

def main():
    token = "7250493926:AAHxUn43CY8g1TRzau05Wvruu1nTjxxdY"  # hardcoded
    print("✅ Token hardcoded, launching bot...")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
