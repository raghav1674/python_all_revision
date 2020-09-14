import smtplib
from email.mime.text import MIMEText

body="hello how ae u"

msg=MIMEText(body)
msg["FROM"]="raghav.81-cse-17@mietjammu.in"
msg["To"]="raghav.81-cse-17@mietjammu.in"
msg["Subject"]="hello"
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("raghav.81-cse-17@mietjammu.in","raghav81")
s.send_message(msg)
s.quit()