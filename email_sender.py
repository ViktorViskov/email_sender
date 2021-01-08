# Example for use
# $python3 email_sender.py email@address.com Title "email content"


# 
# Libs
# 
import email_credentials, sys
from smtplib import SMTP_SSL

# first argument is addres to send
address = sys.argv[1]

# second is email title
title = sys.argv[2]

# thirdth is mail content
body = sys.argv[3]


# adding address in array
arr_addresses = []
arr_addresses.append(address)

# sender and target adress
sent_from = email_credentials.email_user_name

# email text
email_text = """\
From: %s
To: %s
Subject: %s


%s


""" % (sent_from, ", ".join(arr_addresses), title, body)

# server config
server = SMTP_SSL('smtp.meta.ua', 465)

# request
server.ehlo()

# login
server.login(email_credentials.email_user_name, email_credentials.email_user_password)

# send
server.sendmail(sent_from, arr_addresses, email_text)

# clouse connection
server.close()



# print status in console
print("Email to %s was sendt" % address)

