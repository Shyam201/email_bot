import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('example@gmail.com', 'password')
server.sendmail('example@gmail.com',
               'receivermeil@gmail.com',
               'Text you want to send type here..')
                
               