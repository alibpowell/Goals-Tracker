from flask import Flask, render_template, request, redirect, url_for, session
import os
from dotenv import load_dotenv
import json
import re
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("API KEY FOUND?", api_key is not None)

client = OpenAI(api_key=api_key)

app = Flask(__name__)
app.secret_key = "supersecretkey"

def parse_numbered_list(text):
    """Parse simple '1. step' style lists if JSON fails."""
    steps = []
    for line in text.strip().split("\n"):
        match = re.match(r"(\d+)[\.\)]\s*(.+)", line)
        if match:
            steps.append({"id": int(match.group(1)), "task": match.group(2)})
    return steps


def generate_steps(title, description, deadline):
    prompt = f"""
You are a goal-planning assistant.
Generate a JSON array of steps to complete this goal.

FORMAT:
[
  {{"id": 1, "task": "..." }},
  {{"id": 2, "task": "..." }}
]

Goal title: "{title}"
Description: "{description}"
Deadline: "{deadline}"

Return ONLY the JSON. No explanation.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()

        # Remove ```json blocks
        if content.startswith("```"):
            content = "\n".join(content.split("\n")[1:-1])

        try:
            steps = json.loads(content)
        except:
            steps = parse_numbered_list(content)

        # Add done=False flag
        for s in steps:
            s["done"] = False

        if not steps:
            steps = [{"id": 1, "task": "AI did not generate steps.", "done": False}]

        return steps

    except Exception as e:
        print("AI ERROR:", e)
        return [{"id": 1, "task": "AI failed to generate steps.", "done": False}]


@app.route("/", methods=["GET", "POST"])
def onboarding():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["goals"] = []
        return redirect(url_for("home"))
    return render_template("onboarding.html")


@app.route("/home")
def home():
    name = session.get("name", "User")
    goals = session.get("goals", [])

    # Compute progress for each goal
    for g in goals:
        total = len(g["steps"])
        completed = sum(1 for s in g["steps"] if s.get("done"))
        g["total_steps"] = total
        g["completed_steps"] = completed
        g["percent"] = 0 if total == 0 else int((completed / total) * 100)

    session["goals"] = goals
    return render_template("home.html", name=name, goals=goals)


@app.route("/delete_goal/<int:goal_id>", methods=["POST"])
def delete_goal(goal_id):
    goals = session.get("goals", [])
    goals = [g for g in goals if g["id"] != goal_id]
    session["goals"] = goals
    return redirect(url_for("home"))


@app.route("/create_goal", methods=["GET", "POST"])
def create_goal():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        deadline = request.form.get("deadline")

        steps = generate_steps(title, description, deadline)

        goals = session.get("goals", [])
        goal_id = len(goals) + 1

        goals.append({
            "id": goal_id,
            "title": title,
            "description": description,
            "deadline": deadline,
            "steps": steps
        })

        session["goals"] = goals
        return redirect(url_for("goal_detail", goal_id=goal_id))

    return render_template("create_goal.html")


@app.route("/goal/<int:goal_id>", methods=["GET", "POST"])
def goal_detail(goal_id):
    goals = session.get("goals", [])
    goal = next((g for g in goals if g["id"] == goal_id), None)

    if not goal:
        return "Goal not found", 404

    if request.method == "POST":
        step_id = int(request.form.get("step_id"))

        # Mark the step as done instead of deleting it
        for s in goal["steps"]:
            if s["id"] == step_id:
                s["done"] = True

        session["goals"] = goals
        return redirect(url_for("goal_detail", goal_id=goal_id))

    # Show ONLY the next incomplete step
    remaining_steps = [s for s in goal["steps"] if not s["done"]]
    steps_to_show = remaining_steps[:1]

    return render_template("goal_detail.html", goal=goal, steps=steps_to_show)


if __name__ == "__main__":
    app.run(debug=True)
