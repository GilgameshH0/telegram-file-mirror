from telethon import TelegramClient, events, sync

# брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''

client = TelegramClient('mirror', api_id, api_hash)

client.start()

#id чата откуда перехватывать файлы
@client.on(events.NewMessage(-1111111111111))
async def sendMyMessage(event):

    file = await client.download_media(event.message.media, file=bytes)
    #id чата куда отправлять файлы
    await client.send_message(-1111111111111, event.message.message, file=file)

client.run_until_disconnected()