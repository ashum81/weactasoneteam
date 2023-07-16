# client for getting correct answers and send them to the main client
from telethon import TelegramClient, events
from telethon import functions

# Вставляем api_id и api_hash
# https://docs.telethon.dev/en/stable/basic/signing-in.html
# @tmp_user
api_id = 87654321
api_hash = '23266457365234d234affd345345'
main_client = 'client1_name'

# имя файла с сессией, пока он не поменяется не надо повторно логиниться)
client = TelegramClient('run_client2', api_id, api_hash)


@client.on(events.NewMessage(chats=(main_client)))
async def normal_handler(event):
    print(event.message)
    if not event.message.to_dict()["out"] and event.message.to_dict()["media"]:

        answer = 1
        peer = event.message.to_dict()['peer_id']['user_id']
        msg_id = event.message.to_dict()['id']

        await client(functions.messages.SendVoteRequest(
            peer=peer,
            msg_id=msg_id,
            options=[f'{answer}'.encode()]
        ))

        result = await client(functions.messages.GetPollResultsRequest(
            peer=peer,
            msg_id=msg_id
        ))
        print(result)
        answers = result.updates[0].results.results
        print(answers)
        for answer in answers:
            if answer.correct:
                correct_answer = answer.option
                print(f"Correct answer: {correct_answer}")
                await client.send_message(main_client, str(correct_answer))


client.start()
client.run_until_disconnected()
