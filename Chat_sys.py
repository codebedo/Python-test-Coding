

chats = {
    "kim": [],
    "paty": [],
    "lalia": [],

}

# adding message sysrem func
def send_message(person, message):
    if person in chats:
        chats[person].append(message)
        print(f"{person} 's send a messafe: {message}")
    else:
        print(f"{person} did not found")

# 3 showing meassage
def show_chat(person):
    print(f"\n--{person}'s chatting---")

    if chats.get(person):
        for msg in chats[person]:
            print(f"{person}: {msg}")

    else:
        print(f"{person}' not having any message")

send_message("kim", "hello Kim!")
send_message("paty", "hi paty")

show_chat("kim")
show_chat("paty")


while True:
    choice = input("\nwhich person do you want to chat ? (kim/paty/lalia/out): ").lower()
    if choice == "out":
        break
    msg = input("Write your message: ")
    send_message(choice, msg)
    show_chat(choice)