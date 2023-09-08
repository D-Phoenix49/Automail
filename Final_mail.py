
import smtplib
import csv
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime import application

email_receiver=[]

with open('emails.csv','r') as file:
    r = csv.reader(file)
    for i in r:
        email_receiver.extend(i)
        
email_sender = 'csaaunom@gmail.com'
email_password = '***********'
# email_receiver = '#'

subject = 'CSAA Alumni invitation!!'
body = '''Dear Alumni !,

Graduating is not the end to the college life, but a gateway into the world of alumni.

The Computer Science Alumni Association is elated to announce the Alumni Meet for the year 2022-2023, happening on 30th of October (Sunday). 

We request the alumni to register for the alumni meet. We also request everyone to follow our association's LinkedIn page to follow for more updates. 

LinkedIn Page : https://www.linkedin.com/company/csaa-unom/
Discord : https://discord.gg/uWrKCchsPT

To register click the below link
https://forms.gle/zr1bsZCqPUhcDi4SA

Date : 30/10/2022
Time : 1100 hours
Location : Chemical Sciences Auditorium, University of Madras - Guindy Campus, Chennai.

Regards,
Computer Science Alumni Association.'''

try:
    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = " ,".join (email_receiver)
    em['Subject'] = subject
    # em.set_content(body)
    em.attach(MIMEText(body,'plain'))
    # pdfname = 'invitation.pdf'
    binary_pdf = open('invitation.pdf','rb')
    payload=MIMEBase('application','octet-stream',Name='invitation.pdf')
    payload.set_payload((binary_pdf).read())

    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition','attachment',filename='invitation.pdf')
    em.attach(payload)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    
except Exception as e:
    print('Error',e)
    
