def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

messages = ["Halo dunia!", "Python sangat keren.", "Tetap semangat ya."]
sent_messages = []

send_messages(messages, sent_messages)

print("\n--- Status List Akhir ---")
print("List asli (messages):", messages)
print("List terkirim (sent_messages):", sent_messages)