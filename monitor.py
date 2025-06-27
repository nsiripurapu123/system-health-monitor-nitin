import psutil
import time
import sqlite3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

# Email config
SENDER_EMAIL = "your.email@gmail.com"
RECEIVER_EMAIL = "your.email@gmail.com"
APP_PASSWORD = "your_app_password_here"

# Setup database
conn = sqlite3.connect("system_health.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        cpu_usage REAL,
        memory_usage REAL,
        disk_usage REAL
    )
''')
conn.commit()

def send_email_alert(message):
    subject = "⚠️ System Resource Alert"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    except Exception as e:
        print("Failed to send email:", e)

def log_and_alert():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cursor.execute("INSERT INTO logs (timestamp, cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?, ?)",
                   (now, cpu, memory, disk))
    conn.commit()

    alert_triggered = False
    alert_msg = f"{now} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n"

    if cpu > CPU_THRESHOLD or memory > MEM_THRESHOLD or disk > DISK_THRESHOLD:
        alert_triggered = True
        print("⚠️ ALERT: Resource usage exceeded threshold!")
        print(alert_msg)

    if alert_triggered:
        send_email_alert(alert_msg)


while True:
    log_and_alert()
    time.sleep(10)
