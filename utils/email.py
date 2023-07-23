import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

async def send_email(html_content, sender_email, sender_password, receiver_email):
    msg = MIMEText(html_content, 'html')
    
    msg['Subject'] = 'Weekly Commits'
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_email)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
