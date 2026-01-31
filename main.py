import asyncio
import logging
import sys
import os
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
load_dotenv()

TOKEN=os.getenv("BOT_TOKEN")
