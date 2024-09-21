def send_email(message, recipient, sender="university.help@gmail.com"):
    if recipient.find("@") == -1:  # or sender.find("@")==-1:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    r = 0
    if recipient[-1] == 'm' and recipient[-2] == 'o' and recipient[-3] == 'c' and recipient[-4] == '.':
        r = 1
    elif recipient[-1] == 't' and recipient[-2] == 'e' and recipient[-3] == 'n' and recipient[-4] == '.':
        r = 1
    elif recipient[-1] == 'u' and recipient[-2] == 'r' and recipient[-3] == '.':
        r = 1
    if r == 0:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    r = 0
    if sender[-1] == 'm' and sender[-2] == 'o' and sender[-3] == 'c' and sender[-4] == '.':
        r = 1
    elif sender[-1] == 't' and sender[-2] == 'e' and sender[-3] == 'n' and sender[-4] == '.':
        r = 1
    elif sender[-1] == 'u' and sender[-2] == 'r' and sender[-3] == '.':
        r = 1
    if r == 0:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


for i in range(5):
    s1 = input("message ")
    if s1 == "":
        break
    s2 = input("recipient без ковычек ")
    s3 = input("sender без ковычек ")
    if s3 == "":
        send_email(s1, s2)
    else:
        send_email(s1, s2, s3)
