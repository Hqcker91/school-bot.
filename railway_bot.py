import os
import telebot
from telebot.types import ReplyKeyboardMarkup
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()

# ایجاد ربات
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print("❌ خطا: توکن ربات پیدا نشد!")
    print("✅ مطمئن شوی فایل .env را درست پر کرده‌ای")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)

# دیتابیس ساده
users_db = {}

print("🎯 ربات اعلام تعطیلی مدارس")
print("🔧 در حال راه‌اندازی...")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    users_db[user_id] = chat_id
    
    print(f"👤 کاربر جدید: {message.from_user.first_name} (ID: {user_id})")
    
    # ایجاد کیبورد
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add('📊 وضعیت تعطیلی', '🔔 اطلاع‌رسانی', 'ℹ️ راهنما')
    
    welcome_text = (
        "🎓 **ربات اعلام تعطیلی مدارس**\n\n"
        "به ربات خوش آمدید!\n"
        "از طریق دکمه‌های زیر می‌تونید وضعیت تعطیلی رو بررسی کنید."
    )
    
    bot.send_message(chat_id, welcome_text, reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['status'])
def send_status(message):
    user_id = message.from_user.id
    print(f"📊 کاربر {user_id} وضعیت رو چک کرد")
    
    status_message = (
        "🏫 <b>وضعیت تعطیلی مدارس:</b>\n\n"
        "• تهران: 🟢 باز\n"
        "• اصفهان: 🟢 باز\n"
        "• شیراز: 🟢 باز\n\n"
        "📅 آخرین بروزرسانی: امروز\n"
        "⚠️ این اطلاعات آزمایشی هستند"
    )
    bot.reply_to(message, status_message, parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text
    
    if text == '📊 وضعیت تعطیلی':
        send_status(message)
    elif text == '🔔 اطلاع‌رسانی':
        bot.reply_to(message, "✅ شما در لیست اطلاع‌رسانی عضو هستید")
    elif text == 'ℹ️ راهنما':
        bot.reply_to(message, 
            "📖 <b>راهنما:</b>\n\n"
            "• از دکمه 'وضعیت تعطیلی' برای بررسی استفاده کن\n"
            "• برای اطلاعات بیشتر با ادمین تماس بگیر",
            parse_mode='HTML'
        )

if __name__ == '__main__':
    print("=" * 50)
    print("🤖 ربات در حال اجراست!")
    print("📱 به ربات در تلگرام برو و /start رو بفرست")
    print("🛑 برای توقف ربات: Ctrl + C")
    print("=" * 50)
    
    try:
        bot.polling(none_stop=True, interval=1)
    except KeyboardInterrupt:
        print("\n⏹️ ربات متوقف شد")
    except Exception as e:
        print(f"❌ خطا: {e}")
        import os
import telebot
from telebot.types import ReplyKeyboardMarkup

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

users_db = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    users_db[user_id] = message.chat.id
    
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('📊 وضعیت تعطیلی', '🔔 اطلاع‌رسانی')
    
    bot.send_message(
        message.chat.id,
        "🎓 ربات تعطیلی مدارس فعال شد!",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '📊 وضعیت تعطیلی':
        bot.reply_to(message, "🏫 مدارس امروز باز هستند")
    else:
        bot.reply_to(message, "دستور نامعتبر")

print("🤖 ربات روی Railway اجرا شد!")
bot.polling()