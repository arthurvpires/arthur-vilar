import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = '<HOST_URL'>
port = 587
user = 'a'
password = '<SENHA>'
server = smtplib.SMTP(host, port)