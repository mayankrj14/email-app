import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


args = {
    'From'  : 'assassinvineet@gmail.com',
    'Password'  : input('Password: '),
    'To'  : ['vineetmahajan2000@gmail.com', '19bcs086@smvdu.ac.in'],
    'CC'  : ['assassinvineet@gmail.com', 'notybinod@gmail.com'],
    'BCC'  : ['emailsender.smvdu@gmail.com'],
    'Subject'  : 'Subject',
    'Text'  : '<h1>Hello World</h1>',

}
args['html'] = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

def send_mail(args):
    #print('mail')
    from_addr   = args['From']
    password    = args['Password']

    to_addr     = args['To']
    cc_addr     = args['CC']
    bcc_addr    = args['BCC']
        
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_addr, password)

        SUBJECT = args['Subject']  
        TEXT = args['Text']  
        
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        message     = "From: %s\r\n" % from_addr
        message    += "To: %s\r\n" % to_addr
        message    += "CC: %s\r\n" % ",".join(cc_addr)
        message    += "Subject: %s\r\n" % SUBJECT
        message    += "\r\n" 
        message    += TEXT

        to_addr    = to_addr + cc_addr + bcc_addr

        print('message_compiled')
        print(message)
        server.sendmail(from_addr, to_addr, message)
        print('sent')

def send_mail_(args):
    #print('mail')
    from_addr   = args['From']
    password    = args['Password']

    to_addr     = args['To']
    cc_addr     = args['CC']
    bcc_addr    = args['BCC']
        
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_addr, password)

        SUBJECT = args['Subject']  
        TEXT = args['Text']  
        
        #message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        message     = "From: %s\r\n" % from_addr
        message    += "To: %s\r\n" % ",".join(to_addr)
        message    += "CC: %s\r\n" % ",".join(cc_addr)
        message    += "Subject: %s\r\n" % SUBJECT
        message    += "\r\n" 
        message    += TEXT

        to_addr    = to_addr + cc_addr + bcc_addr

        #print('message_compiled')
        #print(message)
        server.sendmail(from_addr, to_addr, message)
        #print('sent')



send_mail_(args)