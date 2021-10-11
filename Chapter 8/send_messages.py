def send_messages(msg, sent_msgs):
	while msg:
		current_msg = msg.pop()
		print(current_msg)
		sent_msgs.append(current_msg)

def show_sent(sent_msgs):
	print("\nThese messages have been sent: ")
	for sent_msg in sent_msgs:
		print(sent_msg)

msg = ["Call you soon.", "Busy right now.", "On the toilet can't talk.", ]
sent_msgs = []

send_messages(msg, sent_msgs)
show_sent(sent_msgs)