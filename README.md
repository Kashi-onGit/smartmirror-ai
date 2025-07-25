# SmartMirror AI

**Face-Aware Smart Mirror Display with Time, Weather, News, and Email Summary using Python & OpenCV**

This project is an intelligent smart mirror interface that uses real-time face detection to trigger a dynamic dashboard. The system shows the current time, date, weather updates, top news headlines, custom greetings based on time of day, and email summaries — all displayed **only when a face is detected**.

---

## ✨ Features

- 👤 **Face Detection Trigger** – UI is shown only when a face is visible
- ⏰ **Live Time & Date** – Auto-updates in real time
- ☁️ **Weather Information** – Fetched using OpenWeatherMap API
- 📰 **Latest News Headlines** – Pulled from Google News API
- 📧 **Email Summary** – Shows number of unread emails
- 💬 **Dynamic Greetings** – Based on time of day (morning, afternoon, evening, night)
- 🧠 **Modular & Customizable** – Built with Tkinter, OpenCV, and threaded detection loop

---

## 🧪 Technologies Used

| Tool/Library      | Purpose                           |
|-------------------|-----------------------------------|
| `OpenCV`          | Face detection via webcam         |
| `Tkinter`         | GUI display for mirror interface  |
| `requests`        | API requests (weather, news)      |
| `imaplib, email`  | Reading email summaries           |
| `geocoder`        | Auto-detects user location        |
| `dotenv`          | Load secret API keys safely       |
| `threading`       | Non-blocking face detection       |

---

## 🚀 Getting Started

### 📁 Clone the repo

bash
`git clone https://github.com/Kashi-onGit/smartmirror-ai.git
cd smartmirror-ai`

📦 Install dependencies
bash
Copy code
`pip install -r requirements.txt`
🔐 Create .env file
Create a .env file in the root directory:

env
`OPENWEATHER_API_KEY=your_openweathermap_api_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password`

▶️ Run the Project
bash
`python main.py`
📌 File Structure
bash

smartmirror-ai/
├── main.py               # Main application UI logic
├── face.py               # Face detection handler
├── greetings.py          # Time-based greetings
├── newsx.py              # News fetching logic
├── mail_list.py          # Email summary
├── weather.py            # Weather information
├── .env                  # (Not uploaded) Secrets file
├── requirements.txt      # All dependencies
├── README.md             # Project documentation
└── .gitignore            # Prevents secrets/files from being tracked


📸 Demo Preview

🙌 Acknowledgements
ChatGPT
OpenCV
OpenWeatherMap
Google News API
Python community

✉️ Contact
Kashi Nath Chourasia
📧 kashi533864@gmail.com

