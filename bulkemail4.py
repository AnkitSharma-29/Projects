import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up the email server
smtp_server = 'smtp.gmail.com'
port = 587  # for TLS
sender_email = 'csvtustudent@gmail.com'
password = 'bbcw tenc tqkx qjbb'

# Create the message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = 'part 4'

# Add body with placeholders for names
body_template = 'Dear {},\n\nYour email body here.\n\nBest regards,\nCSVTU Student'

# List of names and email addresses
recipients = [
    ('The HOD', 'thehosterworld@gmail.com'),
    ('Praveen', 'trendyhoodyt@gmail.com'),
]

# Create the SMTP session and send the emails
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    
    for name, email in recipients:
        # Create a new message container for each recipient
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = 'part 4'
        
        # Replace placeholders with actual names
        body = body_template.format(name)
        msg.attach(MIMEText(body, 'plain'))
        
        text = msg.as_string()
        server.sendmail(sender_email, email, text)
    
    print('Emails sent successfully')
except Exception as e:
    print(f'Error: {e}')
finally:
    if 'server' in locals():
        server.quit()
