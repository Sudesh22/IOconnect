from random import randint
import smtplib, datetime, time, os
from email.mime.text import MIMEText
from dotenv import load_dotenv, find_dotenv
from email.mime.multipart import MIMEMultipart

load_dotenv(find_dotenv())
Sender_Password = os.environ.get("EMAIL_PWD")
Sender_Email = os.environ.get("SENDER_EMAIL")
Receiver_Email = "receiver-email"

tls_Port = 587
smtp_server = 'smtp.gmail.com'

verification_token = randint(000000, 999999)
while len(str(verification_token))<5:
    print(verification_token)
    verification_token = randint(000000, 999999)
    print(verification_token)

def send_mail():
    try: 
        smtp = smtplib.SMTP(smtp_server, tls_Port) 
        smtp.starttls() 
        smtp.login(Sender_Email,Sender_Password)
        content = '''
                    <!DOCTYPE html>

                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <title>OTP for Login</title>
                </head>

                <body
                    style="width:80%; height:100%; margin:0; padding:32px; font: normal normal normal 10px/15px Arial,sans-serif; color:#333; background-color:#f1f1f1; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;">
                    <table class="email-wrapper"
                        style="width:100%; height:100%; margin:auto; padding:0; text-align:center; vertical-align:middle; border-spacing:0; border-collapse:collapse;">
                        <tr>
                            <td>

                                <table class="email-layout"
                                    style="width:350px; height:200px; margin:auto; padding:0; vertical-align:middle; border-spacing:0; border-collapse:collapse;">
                                    <thead class="email-header" style="text-align:center;">
                                        <th bgcolor="#00A4BD" align="center" style="color: white;">
                                            <h1> Welcome aboard!</h1>
                                        </th>
                                    </thead>

                                    <tbody class="email-body">
                                        <tr>
                                            <td style="text-align:left;">
                                                <div
                                                    style="padding:21px 32px; background-color:#fff; border-bottom:2px solid #e1e1e1; border-radius:3px;">
                                                    <h1 style="font-size:16px; line-height:30px; font-weight:bold;">Almost there! Just confirm your email 📬!</h1>
                                                    <p>
                                                        Dear customer,<br>
                                                        <h1>''' + str(verification_token) + '''</h1> is your one time password (OTP). Please do not share the OTP with others<br>
                                                        Regards,<br>
                                                        Team Manjrekar
                                                    </p>
                                                    <p style="padding:11px 0; text-align:left;">
                                                        <a href="" target="_blank"
                                                            style="padding:11px 21px; text-decoration:none; color:#fff !important; background-color:#42af5b; border:1px solid #358d49; border-radius:3px;">Confirm
                                                            email</a>
                                                    </p>
                                                    <p>
                                                        Cheers,<br>
                                                        The Manjrekar Team
                                                    </p>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>

                                    <tfoot class="email-footer" style="text-align:center; font-weight:normal;">
                                        <tr>
                                            <td style="padding-top:32px;">
                                                <div style="color:#999;">
                                                    <a href="" target="_blank"
                                                        style="text-decoration:none; color:#446cb3 !important;">Get in touch</a> |
                                                    <a href="" target="_blank"
                                                        style="text-decoration:none; color:#446cb3 !important;">Knowledge Center</a> |
                                                    <a href="" target="_blank"
                                                        style="text-decoration:none; color:#446cb3 !important;">Log in</a>
                                                </div>
                                                <small style="font-size:12px; color:#999;">© 2023 Manjrekar's, Inc. Andheri - 69<small>
                                            </td>
                                        </tr>
                                    </tfoot>
                                </table>

                            </td>
                        </tr>
                    </table>
                </body>

                </html>
                '''

        message = MIMEMultipart("alternative")
        message["Subject"] = "OTP for Login - " + str(verification_token)
        message["From"] = Sender_Email
        message["To"] = Receiver_Email

        part1 = MIMEText(content, "html")

        message.attach(part1)

        smtp.sendmail(Sender_Email, Receiver_Email, str(message)) 

        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as excp:   
        print("Something went wrong....",excp)

# send_mail()