# System Health Monitor & Alert Tool (SHMAT)

This project is a lightweight Python-based tool that monitors system resource usage and sends alerts when critical thresholds are exceeded. It logs CPU, memory, and disk usage to a local SQLite database and can send real-time email notifications when usage crosses defined limits.

## Features
- Monitors CPU, memory, and disk usage every 10 seconds
- Stores logs in a local SQLite database (`system_health.db`)
- Triggers real-time alerts via console and email when thresholds are breached
- Easy to configure and run on any Linux or Windows system
- Designed to simulate real-world Tech Ops and QA system monitoring tasks

## Technologies Used
- Python 3
- psutil (for system metrics)
- sqlite3 (for database logging)
- smtplib (for email alerts)
- Optional: cron job or Task Scheduler for automation

## Default Thresholds
- CPU usage > 80%
- Memory usage > 80%
- Disk usage > 80%

## Setup & Usage
To get started, install the required dependencies using `pip install psutil`.

For email alerts, generate a Gmail App Password and update the following values inside `monitor.py`:
SENDER_EMAIL = "your.email@gmail.com"
RECEIVER_EMAIL = "your.email@gmail.com"
APP_PASSWORD = "your_app_password"

Run the script with `python monitor.py`. You can also schedule it to run automatically using crontab (Linux) or Task Scheduler (Windows).

## .gitignore
This project includes a `.gitignore` file to exclude:
- `system_health.db` (local data)
- `.env` or `config.ini` (email credentials)
- Python cache files like `__pycache__/`

## Example Output
2025-06-27 21:45:12 | CPU: 65.0% | Memory: 55.3% | Disk: 70.8%
ALERT: Resource usage exceeded threshold!

## Author
Nitin Siripurapu  
B.Tech Computer Science Student  
GitHub: https://github.com/yourusername  
(Replace with your actual GitHub username and repo link)

This project was created to demonstrate hands-on skills in Python scripting, system monitoring, database logging, and real-time alerting. It’s designed for Tech Ops, QA, and entry-level infrastructure roles.
