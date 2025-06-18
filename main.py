import os
import logging
import asyncio
from telegram.ext import Application, CommandHandler
from commands import send_random_surah
from dotenv import load_dotenv
import nest_asyncio

nest_asyncio.apply()
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("اذاعه", send_random_surah))

    me = await application.bot.get_me()
    logger.info("🚀 البوت يعمل الآن...")

    await application.bot.delete_webhook()
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
