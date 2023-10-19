import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
import logging
from features import get_subdomains

load_dotenv()

TOKEN = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
<strong> Welcome to the SubdomainX Bot!</strong>
                                    
This bot will help you find all subdomains for a given domain.
                                    
<em>How to use</em>
Just send the URL you want to find subdomains for.
-------------
telegram.org
-------------

<em>Notes</em>
This bot doesn't have any logic for finding subdomains, just grab the result of request from [rapiddns.io](https://rapiddns.io)
""", parse_mode=telegram.constants.ParseMode.HTML)

async def extract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    # await update.message.reply_text("Getting subdomains...")
    message = await context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Getting subdomains...",
    )
    await context.bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=telegram.constants.ChatAction.TYPING,
    )

    subdomains = get_subdomains(url.replace("http://", "").replace("https://", "").rstrip("/"))
    result = "\n━━━━━━━━━━━\n| ".join([f"{subdomain}" for subdomain in subdomains]) + f"\n━━━━━━━━━━━\ntotal: {len(subdomains)}"

    await context.bot.edit_message_text(
        chat_id=message.chat_id,
        message_id=message.message_id,
        text=result
    )
    

def main():
    application = Application.builder().token(TOKEN).read_timeout(5).write_timeout(5).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, extract))

    application.run_polling()

if __name__ == "__main__":
    main()