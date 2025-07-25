import tkinter as tk
from datetime import datetime
import greetings
import newsx
import face
import weather


#Setup

greet = greetings.Greetings()
fd = face.FD()
email_summary = [
    "📧 2 new emails",
    "➡️ Subject: Meeting rescheduled to 3 PM",
    "➡️ Subject: Your order has been shipped",
]


#Window

root = tk.Tk()
root.title("Smart Mirror")
root.configure(bg="black")
root.attributes('-fullscreen', True)


#UI Elements

time_label = tk.Label(root, font=("Helvetica", 60), fg="white", bg="black")
date_label = tk.Label(root, font=("Helvetica", 30), fg="white", bg="black")
thought_label = tk.Label(root, font=("Helvetica", 20), fg="lightgray", bg="black", wraplength=1000, justify='center')
news_title = tk.Label(root, text="📰 Today's News", font=("Helvetica", 24, "bold"), fg="white", bg="black")
news_label = tk.Label(root, font=("Helvetica", 16), fg="white", bg="black", justify="left")
email_title = tk.Label(root, text="📧 Email Summary", font=("Helvetica", 24, "bold"), fg="white", bg="black")
email_label = tk.Label(root, font=("Helvetica", 16), fg="white", bg="black", justify="left")
weather_title = tk.Label(root, text="🌦️ Weather", font=("Helvetica", 24, "bold"), fg="white", bg="black")
weather_label = tk.Label(root, font=("Helvetica", 16), fg="white", bg="black", justify="left")


#Functions

def update_time_date():
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %d %B %Y"))
    root.after(1000, update_time_date)

def show_ui():
    thought_label.config(text=greet.greetingmsg())
    news_label.config(text="\n".join(newsx.get_top_news()))
    email_label.config(text="\n".join(email_summary))
    weather_label.config(text=weather.get_weather())

    for widget in [time_label, date_label, thought_label, news_title, news_label,
                   email_title, email_label, weather_title, weather_label]:
        widget.pack(pady=5)

def hide_ui():
    for widget in [time_label, date_label, thought_label, news_title, news_label,
                   email_title, email_label, weather_title, weather_label]:
        widget.pack_forget()


# Control flag

ui_timer_active = False

def detect_and_display():
    global ui_timer_active

    if not ui_timer_active:
        print("🔍 Running 1-second face detection...")
        if fd.detect_for_1_second():
            print("✅ Face detected! Showing UI for 10 seconds.")
            show_ui()
            ui_timer_active = True
            root.after(10000, hide_ui)  # Hide after 10 sec
            root.after(9000, reset_detection_flag)  # Re-enable detection after 9 sec

    # Check every second whether detection is allowed
    root.after(1000, detect_and_display)

def reset_detection_flag():
    global ui_timer_active
    ui_timer_active = False

# ---------- Start ----------
update_time_date()
detect_and_display()
root.mainloop()
