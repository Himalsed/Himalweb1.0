import os
import secrets
import smtplib
from email.message import EmailMessage
from email.utils import parseaddr

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)



PROFILE = {
    "name": "Himal Sedhai",
    "role": "Full-Stack Developer",
    "tagline": "I am a Bachelor of Information Management (BIM) student from Nepal with a strong interest in Full Stack Development and Artificial Intelligence."
"Currently, I'm building practical web applications while learning Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG)."
    ,
    "location": "Based in Nepal",
    "email": os.environ.get(
        "CONTACT_RECIPIENT",
        os.environ.get("GMAIL_ADDRESS", "himalsedhai10@example.com"),
    ),
    "github": "https://github.com/Himalsed",
    "linkedin": "https://www.linkedin.com/in/himal-sedhai-32606a35b/",
}

ABOUT = {
    "summary": (
        "I'm a developer who enjoys turning ideas into structured, working "
        "software. I focus on writing readable code, understanding the "
        "problem before the solution, and building products that are "
        "simple to use and easy to maintain."
    ),
    "education": [
        {
            "period": "2024 — present",
            "title": "Bachelor in Information Management",
            "place": "Tribhvan University",
            "detail": "Coursework in data structures, databases, and web development,Python,AI.",
        },
        {
            "period": "2021 — 2023",
            "title": "Higher Secondary Education",
            "place": "New Capital Secondary School",
            "detail": "Focused on physics, mathematics, and computer science.",
        },
    ],
}
TECH_STACKS = [
    {
        "category": "Languages",
        "skills": [
            {"name": "Python", "icon": "devicon-python-plain colored"},
            {"name": "JavaScript", "icon": "devicon-javascript-plain colored"},
            {"name": "HTML5", "icon": "devicon-html5-plain colored"},
            {"name": "CSS3", "icon": "devicon-css3-plain colored"},
            {"name": "SQL", "icon": "devicon-azuresqldatabase-plain colored"},
            {"name":"PHP","icon":"devicon-php-colored"}
            
        ],
    },
    {
        "category": "Frameworks",
        "skills": [
            {"name": "Flask", "icon": "devicon-flask-original colored"},
            {"name": "React", "icon": "devicon-react-original colored"},
            {"name": "Node.js", "icon": "devicon-nodejs-plain colored"},
            {"name": "Bootstrap", "icon": "devicon-bootstrap-plain colored"}
        ],
    },
    {
        "category": "Tools",
        "skills": [
            {"name": "Git", "icon": "devicon-git-plain colored"},
            {"name": "GitHub", "icon": "devicon-github-original colored"},
            {"name": "VS Code", "icon": "devicon-vscode-plain colored"},
            {"name": "Figma", "icon": "devicon-figma-plain colored"},
  
        ],
    },
    {
        "category": "Databases",
        "skills": [
            {"name": "MySQL", "icon": "devicon-mysql-plain colored"},
            {"name": "SQLite", "icon": "devicon-sqlite-plain colored"},
            {"name": "MongoDB", "icon": "devicon-mongodb-plain colored"}
        ],
    },
]

CERTIFICATES = [
    {
        "title": "Crash Course on Python",
        "issuer": "Google",
        "platform": "Coursera",
        "date": "July 13, 2026",
        "duration": "20 hours",
        "link": "https://coursera.org/share/25c3fd8dc708ac2f08192295c31fef1b",
    },
    {
        "title": "Build Dynamic User Interfaces (UI) for Websites",
        "issuer": "Google",
        "platform": "Coursera",
        "date": "August 23, 2026",
        "duration": "15 hours",
        "link": "https://coursera.org/share/d5b3710a626bd558bfd54880c4768b74",
    },
]

PROJECTS = [
    {
        "id": 1,
        "title": "DevMemory AI",
        "status": "Featured",
        "featured": True,
        "description": (
            "An AI-powered developer memory assistant that indexes your local codebase "
            "using Retrieval-Augmented Generation (RAG). Instead of manually searching "
            "through hundreds of files, developers can ask natural language questions "
            "such as 'Where did I implement JWT authentication?' or "
            "'Show me the API validation logic.' The system performs semantic search "
            "with vector embeddings and generates context-aware answers using a local "
            "LLM, ensuring complete privacy since everything runs offline."
        ),
        "stack": "Python • Flask • RAG • ChromaDB • Ollama • Typer",
        "link": "https://github.com/Himalsed/DevMemory-AI",
    },

    {
        "id": 2,
        "title": "Hotel-Hub",
        "status": "AI Project",
        "featured": True,
        "description": (
            "An intelligent knowledge assistant built for hotels and hospitality businesses. "
            "The chatbot retrieves information directly from hotel policies, SOPs, and "
            "knowledge documents using Retrieval-Augmented Generation (RAG). "
            "Instead of hallucinating responses, it provides accurate, document-backed "
            "answers to help hotel staff access information instantly."
        ),
        "stack": "Python • Flask • LangChain • RAG • ChromaDB • Ollama",
        "link": "https://github.com/Himalsed/Hotel-Hub",
    },

    {
        "id": 3,
        "title": "Book Management System",
        "status": "Full Stack",
        "featured": False,
        "description": (
            "A modern full-stack CRUD application for managing books, authors, and "
            "inventory. Users can add, edit, delete, and search books while keeping "
            "records organized through a clean dashboard. The project demonstrates "
            "RESTful routing, database operations, and responsive UI development."
        ),
        "stack": "HTML • CSS • JavaScript • Express.js • MongoDB",
        "link": "https://book-management-sys-iv6d.vercel.app/",
    },

    {
        "id": 4,
        "title": "Huecraft",
        "status": "Full Stack",
        "featured": False,
        "description": (
            "Huecraft is a browser theme studio for developers and designers. "
            "It helps you explore color palettes, Google Fonts, motion presets, "
            "accessible contrast, and copy-ready CSS in one focused workspace. "
            "The interface is intentionally lightweight: Flask serves the application "
            "shell and the design assistant, while the interactive theme editor runs "
            "in the browser. There is no database, account system, or build step."
        ),
        "stack": "Python • Flask • HTML • CSS • JavaScript",
        "link": "https://huecraft-ten.vercel.app/",
    },
]


@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        about=ABOUT,
        tech_stacks=TECH_STACKS,
        certificates=CERTIFICATES,
        projects=PROJECTS,
    )


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in every field before sending.", "error")
    elif len(name) > 120 or len(email) > 254 or len(message) > 5000:
        flash("Please keep your name, email, and message within the field limits.", "error")
    elif parseaddr(email)[1] != email or "@" not in email or any(char.isspace() for char in email):
        flash("Please enter a valid email address.", "error")
    else:
        gmail_address = os.environ.get("GMAIL_ADDRESS", "").strip()
        gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD", "").replace(" ", "")
        recipient = os.environ.get("CONTACT_RECIPIENT", gmail_address).strip()

        if not gmail_address or not gmail_app_password or not recipient:
            flash("Email is not configured yet. Please email me directly instead.", "error")
        else:
            notification = EmailMessage()
            notification["Subject"] = "New portfolio contact message"
            notification["From"] = gmail_address
            notification["To"] = recipient
            notification["Reply-To"] = email
            notification.set_content(f"Name: {name}\nEmail: {email}\n\n{message}")

            acknowledgement = EmailMessage()
            acknowledgement["Subject"] = "Thanks for reaching out"
            acknowledgement["From"] = gmail_address
            acknowledgement["To"] = email
            acknowledgement.set_content(
                f"Hi {name},\n\nThanks for your message. I've received it and will get back to you soon.\n\nHimal"
            )

            try:
                with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as smtp:
                    smtp.starttls()
                    smtp.login(gmail_address, gmail_app_password)
                    smtp.send_message(notification)
                    smtp.send_message(acknowledgement)
                flash("Thanks — your message has been sent. A confirmation email is on its way.", "success")
            except (OSError, smtplib.SMTPException):
                app.logger.exception("Unable to send contact email")
                flash("Sorry, your message could not be sent right now. Please email me directly.", "error")

    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", "5003")))
