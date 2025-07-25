smart_mirror_messages = {
    "morning": [
        "Good Morning! 🌞 Today is a fresh start. Make it count!",
        "Rise and shine! The world awaits your brilliance.",
        "Wake up with determination, go to bed with satisfaction.",
        "Every sunrise is an invitation to brighten someone’s day.",
        "New day, new thoughts, new strength. Let’s go!"
    ],
    "afternoon": [
        "Good Afternoon! Keep pushing, you’re doing great. ☀️",
        "Take a breath, refocus, and keep going.",
        "Your energy defines your direction. Stay positive!",
        "Hope your day is as bright as your smile!",
        "Midday check-in: Drink water, straighten your back, and smile!"
    ],
    "evening": [
        "Good Evening! 🌇 Let the peace of dusk soothe your soul.",
        "You’ve done your best today—now it’s time to unwind.",
        "Evenings are life’s way of saying you survived the day.",
        "Reflect. Recharge. Rejoice. Another day accomplished.",
        "Peace begins with a deep breath and a calm mind."
    ],
    "night": [
        "Good Night! 🌙 Rest well and dream big.",
        "Let today go. Tomorrow is a new page in your story.",
        "Stars are out, and so should your worries be.",
        "May your dreams be sweet and your sleep be deep.",
        "Recharge your soul. A brand new day is waiting for you."
    ]
}

import random
from datetime import datetime

class Greetings():

    def timing(self):
        current_hour = datetime.now().hour

        if 5 <= current_hour < 12:
            current_time = "morning"
        elif 12 <= current_hour < 17:
            current_time = "afternoon"
        elif 17 <= current_hour < 21:
            current_time = "evening"
        else:
            current_time = "night"

        return current_time

    def greetingmsg(self):
        message = random.choice(smart_mirror_messages[self.timing()])
        return message