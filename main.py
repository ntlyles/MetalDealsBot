
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to MetalDealsBot! Type /golddeals or /silverdeals to see today’s deals.")

async def golddeals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🪙 Gold Deal: 1 oz Gold Eagle - $2345.99 (+2.0% over spot)")

async def silverdeals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🥈 Silver Deal: 1 oz Silver Maple - $27.49 (+4.8% over spot)")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("golddeals", golddeals))
    app.add_handler(CommandHandler("silverdeals", silverdeals))

    app.run_polling()

if __name__ == "__main__":
    main()
