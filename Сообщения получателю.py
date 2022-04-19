import pywhatkit

def send_message_inst():
    mobile = input('Введите номер телефона: ')
    message = input('Введите текст сообщения: ')

    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def main():
    send_message_inst()

if _name_ == '_main_':
    main()
        
    
