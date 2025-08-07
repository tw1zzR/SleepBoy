# SleepBoy — Discord Sleep Timer & TTS Bot

**SleepBoy** is a fun Discord bot designed for entertainment purposes only.
It can speak via TTS in Ukrainian, set a sleep timer (after which it kicks everyone from the voice channel over two minutes), and correctly pronounce hours, minutes, and seconds with proper Ukrainian grammatical endings.

> ⚠️ **Disclaimer:**
> This bot is created solely for entertainment and fun. It is **not intended** to offend, insult, or discriminate against anyone. Please use it responsibly and respectfully.
>  
> 🛠️ This bot was created by someone who is not a professional developer, so bugs or issues may occur. If you encounter any problems or have suggestions — feel free to contact me directly.
---

## Features

- Join voice channel (`/join`) and leave (`/leave`).
- Set a sleep timer (`/sleeptime`) with audio and text announcements of remaining time.
- Speak any message aloud via `/speak`.
- Notify remaining time via `/notify`.
- Stop the sleep timer via `/stop`.
- Correct Ukrainian time pronunciation with proper declensions.
- Automatic cleanup of temporary TTS audio files from the `temp` folder.

---

## Installation & Setup

1.  **Clone the repository or copy the project files.**


2.  **Create a `.env` file in the root project folder with the following content:**

    ```env
    BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
    ```

    Replace `YOUR_DISCORD_BOT_TOKEN_HERE` with your actual Discord bot token.


3.  **Create a `phrases.py` file in the root folder** with three lists:

    ```python
    greetings = ["Hello everyone", "Hey there", "Hi friends", ...]
    farewells = ["Goodbye", "See you later", "Take care", ...]
    appeals = ["friend", "buddy", "pal", ...]
    ```

    These lists contain phrases the bot will randomly speak via TTS for greetings, farewells, and appeals.

    **Important:**
    The `phrases.py` file and the `temp` folder (which stores temporary TTS audio files) are included in `.gitignore` by default, so they won’t be uploaded to GitHub.
    You must create `phrases.py` manually or replace all uses of these lists in the code with your own strings and remove unused imports if needed.


4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    Or at least:
    ```bash
    pip install discord.py python-dotenv gTTS
    ```

5.  **Run the bot:**
    ```bash
    python bot.py
    ```
    
---

## Additional Configuration

- In the `on_voice_state_update` function, set your own channel ID in this line:

  ```python
  channel = bot.get_channel(YOUR_CHANNEL_ID)
  ```
  
  This is the text channel where the bot will send the message::
  ```python
  await channel.send(f"🖕 <@{member.id}> ало вася, йди спать")
  ```
  
  - 💬 **Tip:** Use a channel like #spam or another one specifically for bot messages to avoid cluttering important chats.


- You can also change the language or content of any spoken or printed message at any point in the code by simply replacing the existing text with your own in any language.

---

## Project Structure
```bash
/project
 ├── bot.py                # Main bot launcher
 ├── .env                  # Your BOT_TOKEN (ignored by git)
 ├── phrases.py            # Your greeting/farewell/appeal lists (ignored by git)
 ├── temp/                 # Temporary TTS audio files (auto-cleaned, ignored by git)
 ├── cogs/                 # Bot command modules
 ├── tts.py                # TTS voice handling and file management
 ├── state.py              # Bot state (voice client, timers, locks)
 ├── text_utils.py         # Time and text formatting utilities (not shown)
 ├── requirements.txt      # Python dependencies
 └── README.md             # This file
 ```

---

## How It Works

The sleep timer runs for the specified minutes, then kicks all users from the voice channel over 2 minutes.

The bot announces remaining time and messages with proper Ukrainian declensions.

Temporary audio files for TTS are saved in the `temp/` folder and cleaned up automatically every 16 minutes.

Commands `/join`, `/leave`, `/sleeptime`, `/notify`, `/speak`, and `/stop` control the bot's behavior.

## Customizing Phrases

You can edit the `phrases.py` file to add your own greeting, farewell, and appeal phrases. Alternatively, replace all usages of `random.choice(greetings/farewells/appeals)` in the code with your own static strings and remove the phrases import if you don’t want to use the external file.

---

## License

This project is open for personal and educational use.

If you have any questions or need help, feel free to ask!

If necessary, I can help with the `phrases.py` template or anything else.