from gtts import gTTS
import discord
import asyncio
import glob
import uuid
import os

TEMP_DIR = "temp"

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

async def say_gtts(text, voice_client):
    if voice_client.is_playing():
        return

    filename = f"tts_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(TEMP_DIR, filename)

    tts = gTTS(text=text, lang='uk')
    tts.save(filepath)

    if voice_client and voice_client.is_connected():
        audio_source = discord.FFmpegPCMAudio(filepath)
        voice_client.play(audio_source)
        while voice_client.is_playing():
            await asyncio.sleep(1)

    if os.path.exists(filename):
        os.remove(filename)

def cleanup_tts_files():
    for file in glob.glob("tts_*.mp3") + glob.glob("tts_*.wav"):
        try:
            os.remove(file)
        except Exception:
            pass

# Periodic cleaning TTS audio
async def periodic_cleanup():
    while True:
        cleanup_tts_files()
        await asyncio.sleep(960) # every 16 minutes