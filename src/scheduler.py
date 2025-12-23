from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.start()

def add_reminder(bot, user_id, text, remind_time):
    scheduler.add_job(
        bot.send_message,
        trigger="date",
        run_date=datetime.fromisoformat(remind_time),
        args=[user_id, f"⏰ Напоминание:\n{text}"]
    )
