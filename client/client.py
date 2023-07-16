# main client - forward questions to client2
from telethon import TelegramClient, events
from telethon import functions

# Вставляем api_id и api_hash
# https://docs.telethon.dev/en/stable/basic/signing-in.html
# @main_user
api_id = 12345678
api_hash = '234234234234234d234affd345345'
votebot = 'votebot_name'
tmp_client = 'client2_name'

# имя файла с сессией, пока он не поменяется не надо повторно логиниться)
client = TelegramClient('run_client1', api_id, api_hash)

peer = ''
msg_id = ''


@client.on(events.NewMessage(chats=(votebot)))
async def normal_handler(event):
    if not event.message.to_dict()["out"] and event.message.to_dict()["media"]:
        question = event.message.to_dict()["media"]['poll']['question'][2:]
        print(question)
        await client.forward_messages(tmp_client, event.message)

        # answer = 1
        global peer, msg_id
        peer = event.message.to_dict()['peer_id']['user_id']
        msg_id = event.message.to_dict()['id']


@client.on(events.NewMessage(chats=(tmp_client)))
async def normal_handler_2(event):
    print(event.message)
    global peer, msg_id
    answer = event.message.message[2:3]
    print(answer)
    await client(functions.messages.SendVoteRequest(
        peer=peer,
        msg_id=msg_id,
        options=[f'{answer}'.encode()]
    ))


client.start()
client.run_until_disconnected()
client.send_message(votebot, 'onstarttest')
