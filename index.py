from config import *
from time import sleep
from pyrogram  import Client, filters, sync

client = Client('ghoul-session', api_id, api_hash)

client.start()

me = client.get_me()

client.stop()

print('Бот запущен, теперь ты - Гуль')

@client.on_message(filters.text)
async def normal_handler(client, message):
    if(message.text.lower() == start_command and message.from_user.id == me.id):
        i = 1000
        while i > 0:
            sleep(1/messages_per_second)
            await client.send_message(message.chat.id, str(i)+' - 7 = '+str(i-7*step))
            i -= 7*step
            if(end_message != ''):
                await client.send_message(message.chat.id, end_message)  

client.run()
