import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from commands import send_random_surah
from dotenv import load_dotenv
import os
import nest_asyncio

nest_asyncio.apply()
load_dotenv()

# إعدادات تسجيل اللوغ
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# الدالة الرئيسية لتشغيل البوت
async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("يرجى تحديد المتغير BOT_TOKEN في ملف .env")

    application = Application.builder().token(token).build()

    # تغيير الأمر إلى اسم إنجليزي لتجنب الخطأ
    application.add_handler(CommandHandler("broadcast", send_random_surah))

    print("🚀 البوت يعمل الآن...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())

