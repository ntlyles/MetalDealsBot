from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Hardcoded bot token – REMOVE once ENV vars are working
TOKEN = "7250493926:AAHxUn43CY8g1TRzau05Wvruu1nTjxxdY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Metal Deals Bot is online and working!")

def main():
    print("🟢 Launching bot with hardcoded token...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
