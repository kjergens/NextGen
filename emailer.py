import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.mail.yahoo.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'kjergens'
password = 'slaughter5'
sender = 'ME@EXAMPLE.COM'
targets = ['kjergens@yahoo.com', 'katie.jergens@gmail.com']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP(host=smtp_ssl_host, port=smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
