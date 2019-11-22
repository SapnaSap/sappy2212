# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sapna.16cs@cmr.edu.in", "sappy2212") 
  
# message to be sent 
message = "Hiii sapna"
  
# sending the mail 
s.sendmail("sapna.16cs@cmr.edu.in", "sapnakumari2212@gmail.com", message) 
  
# terminating the session 
s.quit() 
