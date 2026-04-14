import smtplib
import random
import datetime
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Email account setup ---
sender_email = os.environ.get("agudadayo158@gmail.com")
receiver_email = os.environ.get("androniqueglasgow14@gmail.com")
password = os.environ.get("vxcwpdzutivapxqq")  # Use an app password, not your main password

# --- Love messages bank (60 messages) ---
messages = [
    "Good morning Andg, you make my world brighter every day ❤️",
    "Andg, thinking of you always fills me with joy 💕,"
    "You are my sunshine, Andg ☀️",
    "Life feels perfect with you in it, my love 🌸",
    "Every heartbeat whispers your name, Andg 💓",
    "You’re my favorite hello and hardest goodbye 💖",
    "Andg, you’re the reason I smile every morning 😊",
    "My love for you grows stronger each day 🌹",
    "You’re my safe place, my home, my everything 🏡",
    "Andg, you’re the best part of me 💞",
    "I’m grateful for you every single day 🙏",
    "You’re my dream come true, Andg ✨",
    "My heart belongs to you forever 💍",
    "You’re my partner, my love, my best friend 🤝",
    "Andg, you make ordinary days extraordinary 🌈",
    "I fall in love with you again every day 💘",
    "You’re my sweetest addiction, Andg 🍯",
    "My love for you is endless, like the stars 🌌",
    "You’re the melody to my heart’s song 🎶",
    "Andg, you’re my forever and always 💎",
    "You make me believe in magic ✨",
    "You’re the reason I believe in love 💗",
    "My world is better with you in it 🌍",
    "You’re my favorite person, Andg 💐",
    "You’re the calm in my storm 🌊",
    "You’re my anchor, my strength ⚓",
    "You’re the light in my darkest days 🕯️",
    "You’re my happily ever after 📖",
    "You’re my soulmate, Andg 💫",
    "You’re my heart’s greatest treasure 💰",
    "You’re the love story I always wanted 📚",
    "You’re my miracle, Andg 🌟",
    "You’re the reason I believe in destiny 🔮",
    "You’re my perfect match 🧩",
    "You’re my sweetest blessing 🙌",
    "You’re my forever Valentine 💝",
    "You’re my sunshine after the rain 🌦️",
    "You’re my guiding star 🌠",
    "You’re my endless inspiration 🎨",
    "You’re my favorite chapter in life 📖",
    "You’re my joy, my peace, my love 🕊️",
    "You’re my heart’s desire 💓",
    "You’re my reason to keep going 💪",
    "You’re my sweetest dream 🌙",
    "You’re my love, my life, my all 💞",
    "You’re my destiny, Andg 🌹",
    "You’re my eternal flame 🔥",
    "You’re my sweetest gift 🎁",
    "You’re my one and only 💍",
    "You’re my forever love 💖",
    "You’re my heart’s song 🎵",
    "You’re my endless joy 😍",
    "You’re my sweetest memory 🖼️",
    "You’re my love story 💌",
    "You’re my everything, Andg 💕",
    "You’re my heart’s keeper 🔐",
    "You’re my forever happiness 🌸",
    "You’re my true love 💘",
    "You’re my world, Andg 🌍"
]

# --- Pick a random message each day ---
random.seed(datetime.date.today().toordinal())  # ensures same message for the same day
daily_message = random.choice(messages)

# --- Compose the email ---
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Daniel's Daily Love Note ❤️"

message.attach(MIMEText(daily_message, "plain"))

# --- Send the email ---
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Love message sent to Andg:", daily_message)
