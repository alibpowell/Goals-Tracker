# Goals Tracker

**A modern, interactive web app for setting, tracking, and completing personal goals with AI-generated step-by-step plans.**

---

## Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Demo](#demo)  
- [Technologies](#technologies)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [Configuration](#configuration)  
- [Future Improvements](#future-improvements)  
- [License](#license)

---

## Overview

Goals Tracker is a sleek, user-friendly web app that helps users define personal goals, generate AI-assisted step-by-step action plans, and track progress visually. The app leverages OpenAI’s GPT API to create actionable tasks and provides a simple interface to check off steps as they’re completed, with a modern and professional design.  

---

## Features

- **Onboarding flow**: Personalize the app with your name.
- **Goal creation**: Input goal title, description, and deadline.
- **AI-generated steps**: Automatically generate actionable steps using OpenAI GPT models.
- **Step tracker**: Complete steps one by one with the next step automatically displayed.
- **Progress bar**: Track overall goal completion on the home page.
- **Delete goals**: Remove goals if no longer needed.
- **Celebration**: Confetti animation when all steps for a goal are completed.
- **Session-based storage**: Keep track of goals and progress without a database for quick prototyping.
- **Modern UI**: Clean, colorful, professional interface with responsive forms and buttons.

---

## Technologies

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **API:** OpenAI GPT (gpt-4o-mini)  
- **Environment management:** Python `venv`, `python-dotenv`  

---

## Installation

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/Goals-Tracker.git
cd Goals-Tracker
```
2. **Create Virtual Enviornment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
# OR
venv\Scripts\activate      # Windows
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Add OpenAI API Key**
Create a `.env` file in the root directory with the following content:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```
5. **Run the App**
```bash
python app.py
```
Open your browser at `http://127.0.0.1:5000` to start using the app.

---

## Usage

### Onboarding
Enter your name to personalize your dashboard.

### Create a Goal
Fill in the title, description, and deadline. Click **Generate Steps** to get AI-suggested tasks.

### Complete Steps
Go to the goal page and complete tasks one by one. Completed steps are tracked in the **progress bar** on the home page.

### Delete Goals
Use the red **Delete** button on the home page to remove any unwanted goals.

---

## Folder Structure

```bash
Goals-Tracker/
│
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API key) - NOT committed
├── templates/
│   ├── onboarding.html
│   ├── home.html
│   ├── create_goal.html
│   └── goal_detail.html
├── static/
│   ├── css/
│   └── js/
└── venv/                # Virtual environment
```

---

## Configuration

- **OpenAI API Key**  
  Ensure your OpenAI API key is set correctly in `.env`.

- **Styling**  
  You can customize styling by editing the CSS inside the templates or by linking an external stylesheet.

- **AI Settings**  
  Adjust the AI model, temperature, or prompt in `app.py` to tweak step generation.

---

## Future Improvements

- **Persistent Storage**  
  Integrate a database (SQLite/PostgreSQL) for permanent goal tracking.

- **User Authentication**  
  Add login/signup functionality for multiple users.

- **Enhanced UI**  
  Add color-coded step statuses, animations, and mobile responsiveness.

- **Notifications**  
  Implement email or browser notifications for deadlines.

- **Analytics**  
  Track progress trends over time.

