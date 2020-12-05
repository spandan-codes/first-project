rd=True
started=False
while True:
	q=input("(type help for commands)>").lower()
	if q=="help":
		print("start to start the car \n stop to stop the car \n quit to exit")
	elif q=="start":
		if started:
			print("car is already started")
		else:
			started=True
			print("car started")
	elif q=="stop":
		if not started:
			print("car is already stopped")
		else:
			started=False
			print("car stopped")
	elif q=="quit":
		print("thank you for playing see you later")
		break
	else:
		print("i don't understand that command")
print("bhoi rox")
