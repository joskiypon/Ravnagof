from argparse import Namespace
from .. import loader, utils
import asyncio, pytz, re, telethon
from telethon.tl.types import MessageEntityTextUrl
import json as JSON
from datetime import datetime, date, time
import telethon.events as events
import random;
import string;

client = 0;
class data:
	owner_id = [ 1739987250 ];
	iris_ids = [ 866983694 ];

class AJMod(loader.Module):
	strings = {"name": "RavMod"};
	async def client_ready(self, client_var, db):
		# loading the bot
		global client;
		client = client_var;

	async def watcher(self, message):
		if not isinstance(message, telethon.tl.types.Message): return;
		author, content = await message.get_sender(), message.message;

		#	virus log	#
		if author.id in data.iris_ids and content.find("гоф бей =") != -1:
			await message.reply("ЗАрАзИтЬ =")

		#	command handle	#	
		if author.id != data.owner_id: return
