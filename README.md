# OI TLE Bot

OI TLE Bot is a Discord bot designed to help competitive programmers—especially
those preparing for Olympiads in Informatics (IOI, national contests, etc.)—track their progress, get practice problems, and engage in virtual contests. The bot uses the [DMOJ](https://dmoj.ca/) API to serve high-quality OI-style problems, manage user stats, and provide personalized recommendations.

## ✨ Features

- 🔍 Search and recommend DMOJ problems by tag, difficulty, or contest
- 🧠 Daily OI-style problem challenges
- 📊 Track solved problems and user performance over time
- ⚔️ Host virtual practice contests with friends
- 🎯 Topic-based training recommendations (e.g., DP, graphs)
- 🎲 `/gimme` command for a random OI problem

## 🔌 Powered by
- [DMOJ API](https://dmoj.ca/api/)
- Python + discord.py
- SQLite (or optional PostgreSQL) for user tracking

## 📦 Setup & Run
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Set your Discord bot token as an environment variable:
   ```bash
   export DISCORD_TOKEN=your_bot_token
   ```
3. Start the bot
   ```bash
   python bot.py
   ```

## 👨‍💻 Contributions
Feel free to open issues or submit PRs to improve features, problem filters, or performance!
