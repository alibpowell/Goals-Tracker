# Goals Tracker

Public URL: https://goals-tracker-sxcd.onrender.com

**A modern, interactive web app for setting, tracking, and completing personal goals with AI-generated step-by-step plans.**

---

## Table of Contents
- [Executive Summary](#executive-sumamry)  
- [System Overview](#system-overview)  
- [Demo](#demo)  
- [Technologies](#technologies)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [Configuration](#configuration)  
- [Future Improvements](#future-improvements)  
- [License](#license)

---

## Executive Summary

Goals Tracker is a sleek, user-friendly web app that helps ANYONE define personal goals, generate AI-assisted step-by-step action plans, and track progress visually. The app leverages OpenAI’s GPT API to create actionable tasks and provides a simple interface to check off steps as they’re completed, with a modern and professional design, designed to motivate through basic steps. When you open the app, you enter your name, and are directed to a sleek dashboard, where you can create, track, accomplish, and delete different personal goals. 

---

## System Overview

### Course Concepts

* The project uses Flask to create a web service with multiple routes (`/`, `/home`, `/create_goal`, `/goal/<id>`).
* It uses environment variables via .env and to securely load the OpenAI API key.
* This demonstrates proper secret management, and the repo includes a .env.example file with placeholder variables.
* This project contains a working Dockerfile, and can run via Docker.
* `requirements.txt` makes for reproducible, easy install.

### Architecture Diagram

![Architecture Diagram](./assets/diagram.png)

### Models and Services

**Model**

This project uses a large language model (LLM) through the OpenAI API:
* Model: gpt-4o-mini
* Purpose: Generate goal steps in structured JSON
* Size: Remotely hosted model (not stored locally)
* License: OpenAI API (commercial license usage)
No machine-learning model files (.pkl, .onnx, etc.) are stored in the repository.

**Services**

| Component / Service           | Description                                      | License / Terms              |
|------------------------------|--------------------------------------------------|------------------------------|
| **Flask**                    | Web framework used for routing + session logic   | BSD-3 License                |
| **HTML Templates (Frontend)**| Renders onboarding, home, and goal detail pages  | Original (Author-Created)    |
| **OpenAI API**               | Generates step-by-step goal plans using LLM      | OpenAI API Terms of Use      |
| **openai-python library**    | Python client for calling the OpenAI API         | MIT License                  |
| **python-dotenv**            | Loads environment variables from `.env`          | MIT License                  |
| **Gunicorn**                 | Production WSGI server for deployment            | MIT License                  |
| **Docker** (optional credit) | Containerization of the application              | Apache License 2.0           |

### Features

- **Onboarding flow**: Personalize the app with your name.
- **Goal creation**: Input goal title, description, and deadline.
- **AI-generated steps**: Automatically generate actionable steps using OpenAI GPT models.
- **Step tracker**: Complete steps one by one with the next step automatically displayed.
- **Progress bar**: Track overall goal completion on the home page.
- **Delete goals**: Remove goals if no longer needed.
- **Celebration**: Confetti animation when all steps for a goal are completed.
- **Session-based storage**: Keep track of goals and progress without a database for quick prototyping.
- **Modern UI**: Clean, colorful, professional interface with responsive forms and buttons.

### Technologies

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

  ---

## Liscence and Credits

### Credits

Flask (BSD License) — web framework

OpenAI API + openai-python library — used for AI step generation

Gunicorn — production web server

Python 3.14

Render.com — hosting platform

### Liscense

**OpenAI API (commercial license usage)**

**MIT License**

Copyright (c) 2025 Ali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

