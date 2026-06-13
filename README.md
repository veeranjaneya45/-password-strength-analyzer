# -password-strength-analyzer
<div align="center">

# 🔐 PassGuard
### *Your passwords deserve better than "password123"*

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Security-Hardened-red?style=for-the-badge&logo=shield&logoColor=white"/>
<img src="https://img.shields.io/badge/Deployed-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Live-22c55e?style=for-the-badge"/>

<br/>

> **"The average person reuses the same password across 14 different websites."**
> PassGuard was built to end that.

<br/>

```
██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
```

**[🚀 Live Demo](https://your-vercel-url.vercel.app)** · **[📸 Screenshots](#screenshots)** · **[⚡ Features](#features)** · **[🛠 Setup](#setup)**

</div>

---

## 🧠 What is PassGuard?

PassGuard is a **real-time password intelligence tool** that doesn't just tell you your password is weak — it tells you *exactly why*, *how bad it is*, and *gives you a better one on the spot*.

Built from scratch as **Project 1** of the Thiranex Cybersecurity Internship, this isn't your average "rate my password" form. It's a full-stack security web app with a slick dark UI, live scoring, a cryptographically-aware password generator, and a session-based history tracker.

---

## ⚡ Features

| Feature | Description |
|--------|-------------|
| 🔍 **7-Point Analysis Engine** | Checks length, uppercase, lowercase, numbers, symbols, entropy, and common password blacklist |
| 📊 **Live Strength Meter** | Animated progress bar that updates in real time with color-coded severity |
| 🎲 **Password Generator** | Generates cryptographically strong passwords that pass all 7 checks |
| 📋 **Check History** | Session-based log of every password checked — masked for privacy |
| 👁️ **Show/Hide Toggle** | Peek at your password safely |
| 📱 **Fully Responsive** | Works perfectly on mobile, tablet, and desktop |
| 🌑 **Dark UI** | Glassmorphism design with animated gradient blobs |
| 📤 **One-Click Copy** | Instantly copy suggested passwords to clipboard |

---

## 🔬 How the Scoring Works

PassGuard uses a **weighted 7-point scoring system**:

```
✅ Length ≥ 12 chars     → +2 points   (length ≥ 8 → +1)
✅ Uppercase letters      → +1 point
✅ Lowercase letters      → +1 point
✅ Numbers                → +1 point
✅ Special characters     → +2 points
❌ Common password list   → Score = 0  (instant fail)
```

**Score → Strength mapping:**
```
0–1  →  🔴 WEAK          (You're one data breach away from disaster)
2–3  →  🟠 MODERATE      (Better, but hackers aren't impressed)
4–5  →  🟡 STRONG        (Solid. Not perfect, but solid.)
6–7  →  🟢 VERY STRONG   (Now we're talking.)
```

---

## 🛠 Tech Stack

```
Backend   →  Python 3.12 + Flask
Frontend  →  Vanilla HTML5 + CSS3 + JavaScript (ES6+)
Styling   →  Custom CSS with glassmorphism + Inter font
Icons     →  Font Awesome 6.5
Hosting   →  Vercel (serverless)
```

---

## 🚀 Setup & Run Locally <a name="setup"></a>

**1. Clone the repo**
```bash
git clone https://github.com/veeranjaneya45/password-strength-analyzer.git
cd password-strength-analyzer
```

**2. Install dependencies**
```bash
pip install flask
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
password-strength-analyzer/
│
├── app.py                  # Flask backend — all logic lives here
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment config
│
├── templates/
│   └── index.html          # Full frontend (HTML + JS)
│
└── static/
    └── style.css           # All styles — dark theme, animations
```

---

## 🔐 Security Concepts Learned

Building PassGuard taught me:

- **Password entropy** — why length matters more than complexity
- **Regex pattern matching** — detecting character classes in strings
- **Cryptographic randomness** — using `random.choice` over predictable methods
- **Session management** — storing user data server-side securely
- **HTTP security headers** — what Flask exposes by default
- **RESTful API design** — `/analyze`, `/generate`, `/history` endpoints

---

## 🌐 Deployment

Deployed on **Vercel** with zero configuration needed beyond `vercel.json`.

Every `git push` to `main` triggers an automatic redeploy. The live URL updates in under 60 seconds.

```bash
git add .
git commit -m "your message"
git push  # Vercel auto-deploys ✅
```

---

## 👨‍💻 Author

**Veeranjaneya**
<div align="center">

---

*"Security is not a product, but a process."* — Bruce Schneier

**⭐ Star this repo if PassGuard helped you think twice about your passwords!**

</div>
