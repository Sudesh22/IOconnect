import smtplib, os
from email.mime.text import MIMEText
from dotenv import load_dotenv, find_dotenv
from email.mime.multipart import MIMEMultipart
from Mail import Mail

load_dotenv(find_dotenv())
Sender_Password = os.environ.get("EMAIL_PWD")
Sender_Email = os.environ.get("SENDER_EMAIL")

tls_Port = 587
smtp_server = 'smtp.gmail.com'

def send_mail(name,Receiver_Email,context,token=None):
    aes_password = os.environ.get("AES_PWD")
    try: 
        smtp = smtplib.SMTP(smtp_server, tls_Port) 
        smtp.starttls() 
        smtp.login(Sender_Email,Sender_Password)
        
        message = MIMEMultipart("alternative")

        content = ""
        if context == "resetPass":
            content = Mail.changePassword["mailBody"].format(name=name,token=token)
            message["Subject"] = Mail.changePassword["subject"].format(token=token)
        elif context == "resetSuccess":
            content = Mail.passwordSuccess["mailBody"].format(name=name)
            message["Subject"] = Mail.passwordSuccess["subject"]
        elif context == "distress":
            content = Mail.distress["mailBody"].format(name=name)
            message["Subject"] = Mail.distress["subject"]

        message["From"] = Sender_Email
        message["To"] = Receiver_Email

        part1 = MIMEText(content, "html")

        message.attach(part1)

        smtp.sendmail(Sender_Email, Receiver_Email, str(message)) 

        smtp.quit() 
        print ("Email sent successfully!") 
        return token

    except Exception as excp:   
        print("Something went wrong....",excp)
        return "error"

# send_mail("sudesh", "manjrekarsudesh15@gmail.com", "resetPass", token=2682)