# def read_messages(filter1, user1, imap_server1, password1):
#     import imaplib
#     import email
#     email_info_holder = []
#     imap_server = imap_server1
#     email_address = user1
#     password = password1
#     imap = imaplib.IMAP4_SSL(imap_server)
#     imap.login(email_address, password)
#     imap.select("Inbox")
#     def read_all(filter2):
#         _, msgnums = imap.search(None, "ALL")
#         for msgnum in msgnums[0].split():
#             _, data = imap.fetch(msgnum, "(RFC822)")
#             message = email.message_from_bytes(data[0][1])
#             subject_string = f"Subject: {message.get('Subject')}"
#             if filter2 in subject_string:
#                 email_info_holder.append(f"Message Number: {msgnum}")
#                 email_info_holder.append(f"From: {message.get('From')}")
#                 email_info_holder.append(f"To: {message.get('To')}")
#                 email_info_holder.append(f"BCC: {message.get('BCC')}")
#                 email_info_holder.append(f"Subject: {message.get('Subject')}")
#                 # print("Content:\n")
#                 # print(f"Message Number: {msgnum}")
#                 # print(f"From: {message.get('From')}")
#                 # print(f"To: {message.get('To')}")
#                 # print(f"BCC: {message.get('BCC')}")
#                 # print(f"Subject: {message.get('Subject')}")
#                 for part in message.walk():
#                     if part.get_content_type() == "text/plain":
#                         email_info_holder.append(part.as_string().split("wrote:")[1])
#     read_all(filter1)
#     imap.close()
#     return email_info_holder

# read_messages()











def read_messages(filter1, user1, imap_server1, password1):
    import imaplib
    import email
    email_info_holder = []
    imap_server = imap_server1
    email_address = user1
    password = password1
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_address, password)
    imap.select("Inbox")
    def read_all(filter2):
        _, msgnums = imap.search(None, "ALL")
        for msgnum in msgnums[0].split():
        #     # print(msgnum)
            _, data = imap.fetch(msgnum, "(RFC822)")
            message = email.message_from_bytes(data[0][1])
            subject_string = f"Subject: {message.get('Subject')}"
            # print(subject_string)
            # print(message)
            # my_array = data[0][1]
        #     if msgnum > msgnums[0].split():
        #         for i in my_array:
        #             print[i]
        #             print(my_array[i])

            # print(len(my_array))
            # print(msgnums[0].split())




            # trying to zero in on the exact spot that the body of the email is

            body = message.as_string()
            # print(body)
            if len(body.split('<div dir="ltr">')) > 0:
                print('this is the body')
                print(body.split('<div dir="ltr">')[len(body.split('<div dir="ltr">'))-1])
                print('this is not the body')
            body = len(body.split('\n\n'))
            # body = body[1].split('</div>')
            # print(body)






            email_info_holder.append([f"From: {message.get('From')}",f"To: {message.get('To')}",f"Subject: {message.get('Subject')}",f"Message Number: {msgnum}"])
            # print(len(message))
            # email_info_holder.append(f"From: {message.get('From')}")
            # email_info_holder.append(f"To: {message.get('To')}")
            # email_info_holder.append(f"BCC: {message.get('BCC')}")
            # print((data[0][1]))

            # if filter2 in subject_string:
            #     email_info_holder.append(f"Message Number: {msgnum}")
            #     email_info_holder.append(f"From: {message.get('From')}")
            #     email_info_holder.append(f"To: {message.get('To')}")
            #     email_info_holder.append(f"BCC: {message.get('BCC')}")
            #     email_info_holder.append(f"Subject: {message.get('Subject')}")
            #     print('this is mgnum')
            #     # print("Content:\n")
            #     print(f"Message Number: {msgnum}")
            #     # print(f"From: {message.get('From')}")
            #     # print(f"To: {message.get('To')}")
            #     print('this is bcc')
            #     print(f"BCC: {message.get('BCC')}")
            #     # print(f"Subject: {message.get('Subject')}")
            #     for part in message.walk():
            #         if part.get_content_type() == "text/plain":
            #             email_info_holder.append(part.as_string().split("wrote:")[1])
            #     print(email_info_holder)
    # print('info')
    # print(email_info_holder)
    read_all(filter1)
    # print('this is the filter1 result')
    # print(filter1)
    imap.close()
    return email_info_holder


def get_html(user1, imap_server1, password1):
    import imaplib
    import email
    email_info_holder = []
    html_holder = []
    imap_server = imap_server1
    email_address = user1
    password = password1
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_address, password)
    imap.select("Inbox")
    filter2 = 'html'
    _, msgnums = imap.search(None, "ALL")
    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        subject_string = f"Subject: {message.get('Subject')}"
        if filter2 in subject_string:
            email_info_holder.append((message.get('BCC')))
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    # print(part.as_string())

                    # print(((part.as_string().split("\n\n")[1])))

                    if (len(part.as_string().split("wrote:"))>0):
                        email_info_holder.append(part.as_string().split("\n\n")[1])
    for item in email_info_holder:
        if item is not None:
            item1 = item[1]
            # print(item)
            html_holder.append(item1.replace('\n\n>', '').replace('\n>\n', ''))
        # item.replace('\n\n>', '').replace('\n>\n', '')
    # html_holder.append(email_info_holder[1].replace('\n\n>', '').replace('\n>\n', ''))
    # print(html_holder)
    # email_info_holder = ''.join(email_info_holder)
    # email_info_holder = email_info_holder.split(' None')
    # print(type(email_info_holder))
    email_info_holder = [x for x in email_info_holder if x is not None]
    imap.close()

    
    return email_info_holder



def send_message(from1, subject1, message1, to1, password1):
    import smtplib 
    from email.message import EmailMessage
    def email_alert(subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        user = from1
        msg['from'] = user
        password = password1
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
    email_alert(subject1, message1, to1)




import requests
url = 'https://httpbin.org/post'
data = {'user':'kilroy.jofam@gmail.com', 'password':'xidtydgphdecozny', 'imap_server':'imap.gmail.com'}

response = requests.post(url, data=data)
# print(response)  # <Response [200]>

result = response.json()

user = result['form']['user']
password = result['form']['password']
imap_server = result['form']['imap_server']

print(read_messages('html', user, imap_server, password))