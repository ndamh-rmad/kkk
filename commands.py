import random
from telegram import InputFile
from telegram.constants import ParseMode
import os
from surah_audio import surahs

async def send_random_surah(update, context):
    try:
        surah = random.choice(surahs)
        audio_url = surah["audio"]
        surah_name = surah["name"]

        channel_id = os.getenv("CHANNEL_ID") or update.effective_chat.id

        await context.bot.send_audio(
            chat_id=channel_id,
            audio=audio_url,
            caption=f"🎧 تلاوة سورة: {surah_name}",
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        print(f"❌ خطأ أثناء الإرسال: {e}")
