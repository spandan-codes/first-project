emote={
"sad":":(",
"happy":":)",
"lol":"xD"

}
message=input("comment>")
words=message.split(" ")
l=""
for w in words:
    l+=emote.get(w,w)+" "
print(l)
