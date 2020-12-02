

def emoji_converter(message):
    emote={
    "sad":":(",
    "happy":":)",
    "lol":"xD"

    }
    l=""
    words=message.split(" ")
    for w in words:
        l+=emote.get(w,w)+" "
    return l

message=input("comment>")
print(emoji_converter(message))

