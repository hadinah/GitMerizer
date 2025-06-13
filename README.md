# 🚀 GitMerizer

**Git**hub Sum**Merizer** is a AI-powered tool that creates human-readable summaries of public GitHub activity.  
Built for developers, teams, and curious minds who want to understand **what’s happening in a repo** — with or without diving into every commit.

🌐 **Live Demo:** [gitmerizer.curiosityweekends.org](https://gitmerizer.curiosityweekends.org/)

---

## 🧠 Features

- 🔍 Summarizes activity by GitHub username(s)
- 🕒 Custom time windows (e.g. past 24h, 7 days...)  
>  _Although we’re limited by GitHub’s Events API: it only retains events from the past **30 days** and up to **300 events per user**, with older activity dropped — so long-term history is off the table._  (We could get around this but thays for the next version o-o)
> [📎 GitHub Events API Reference](https://docs.github.com/en/rest/activity/events)
- 🧑‍🎨 Stylish Markdown output rendered beautifully in-browser
- ⚙️ Powered by **Gemini Flash** (Generative AI by Google)
- 🧾 Shows both summaries _and_ raw logs (per repo)
- 🎨 Fully responsive modern UI

---

## 📸 Screenshots

> Comming Soon!
---

## ⚡ Quick Start

```bash
git clone https://github.com/hadinah/GitMerizer.git
cd GitMerizer
pip install -r requirements.txt
python app.py
```

> 💡 You don't need to configure `.env` – the demo version uses a public Gemini API key (safe for testing). (_But Its appreciated to use your own API_)

---

## 📜 License

This project is licensed under the **GNU GPL v3** License.  
Feel free to fork, hack, remix, and share with attribution.

---

## 🧠 Powered by AI

GitMerizer uses **Google Gemini Flash 2.0** to turn raw events like commits, PRs, and issues into a readable summary.

---

## 🏷️ Badges

![GNU GPL V3 License](https://img.shields.io/github/license/hadinah/GitMerizer)
![Issues](https://img.shields.io/github/issues/hadinah/GitMerizer)
![Stars](https://img.shields.io/github/stars/hadinah/GitMerizer)
![Forks](https://img.shields.io/github/forks/hadinah/GitMerizer)
![Last Commit](https://img.shields.io/github/last-commit/hadinah/GitMerizer)

---

## 👤 Author

Made with 💙 by [**Hadin AH**](https://github.com/hadinah)  
> _Git better insights, no meetings required._ ✨  
> (Come on, that was good... **Git** better insights? Yeah, you smiled.)