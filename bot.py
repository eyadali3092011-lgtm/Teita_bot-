import os
from flask import Flask, request
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN", "PUT_YOUR_TOKEN_HERE")
app = Flask(__name__)
bot_app = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("اهلا بيك في بوت تيتا ❤️ انا شغال تمام!")

async def reply(update, context):
    await update.message.reply_text("وصلتني رسالتك: " + update.message.text)

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

@app.route('/')
def home():
    return "Teita Bot is Running!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    import asyncio
    update = telegram.Update.de_json(request.get_json(force=True), bot_app.bot)
    asyncio.run(bot_app.process_update(update))
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
