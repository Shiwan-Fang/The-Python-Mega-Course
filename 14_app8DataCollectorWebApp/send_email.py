from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "fffshiwan@gmail.com" #用我们的账号给对方发邮件
    from_password="lkwfmvsbuhbfmhrw"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that is calculated out <strong>%s</strong> of people." % (height, average_height,count)
    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    gmail=smtplib.SMTP('smtp.gmail.com', 587)  #登录gmail的地方
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
