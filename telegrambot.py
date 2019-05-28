import telepot
import time
token = 'Replace this by the your token'
Bot = telepot.Bot(token)
print(Bot.getMe())
Bot.getUpdates()
print(Bot.getUpdates())
while True:
    print("1:Send Message")
    print("2:Recieve Message")
    print("3:Glance the message")
    print("4:Maintain convo")
    print("0:Exit")
    choice = input("Choose your desired action ")
    if choice == '1':
        text = input("enter text to be sent")
        tok = input("enter your id")
        Bot.sendMessage(tok,text)
    if choice == '2':
        from telepot.loop import MessageLoop
        def handle(msg):
            print(msg)
        MessageLoop(Bot,handle).run_as_thread()
    if choice == '3':
        from telepot.loop import MessageLoop
        def handle(msg):
            content_type,chat_type,chat_id = telepot.glance(msg)
            print(content_type,chat_type,chat_id)
            if content_type == 'text':
                Bot.sendMessage(chat_id,msg['text'])
        MessageLoop(Bot,handle).run_as_thread()
        while 1:
            time.sleep(10)
    if choice == '4':
        from telepot.loop import MessageLoop
        from telepot.delegate import pave_event_space, per_chat_id, create_open

        class MessageCounter(telepot.helper.ChatHandler):
            def __init__(self, *args, **kwargs):
                super(MessageCounter, self).__init__(*args, **kwargs)
                self._count = 0

            def on_chat_message(self, msg):
                self._count += 1
                self.sender.sendMessage(self._count)
        bot = telepot.DelegatorBot(token, [pave_event_space()(per_chat_id(), create_open, MessageCounter, timeout=10),])
        MessageLoop(bot).run_as_thread()
        while 1:
            time.sleep(10)
    if choice == '0':
        break
    ch=input("again(y/n)")
    if ch == 'n':
        break
