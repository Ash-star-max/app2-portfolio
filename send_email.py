import smtplib, ssl

host = "smtp.gmail.com"
port = 465

user_name = "apal16408@gmail.com"
password = "lpwzmbdnhavlousm"

reciever = "apal16408@gmail.com"
context = ssl.create_default_context()

message = """
subject - hi!
How are you Ashish
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, reciever, message)