import os
import smtplib
import datetime
# import openpyxl
from email.encoders import encode_base64
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import csv

# with open("C:\startcoding\selenium\letter.txt", 'r', encoding="utf8") as file:
#     letter=file.read()
with open("C:/startcoding/selenium/email_address.csv", "r" , encoding="UTF-8") as file:
    mail_list=list(csv.reader(file))

my_mail="goodojb@naver.com"
pwd="result$0619"
# to_mail="goodojb@gmail.com"

for name, to_mail in mail_list:
    msg=MIMEMultipart()
    msg['Subject']="안녕하세요! 진단검사의학팀 위종빈입니다"
    msg['From']=my_mail
    msg['To']=to_mail

    files=list()
    files.append("1test.jpg")
    files.append("2test.jpg")
    files.append("3test.jpg")
    files.append("4test.jpg")
    files.append("5test.jpg")

    for f in files:
        part=MIMEBase('application', 'octect-stream')
        part.set_payload(open(f, 'rb').read())
        encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(f))
        msg.attach(part)

    # 본문 내용
    # content=letter.replace("[name]",name)
    # mail_text=MIMEMultipart(letter)
    msg.attach(MIMEText("안녕하세요!"+name+" 오늘 자 구글 이미지에 검색되는 첫 5개 병원 검색 결과입니다.", 'plain'))


# # 이미지 첨부
# image_path='test.jpg'
# with open("C:\startcoding\selenium\test.jpg", 'rb') as img_file:
#     img_data=img_file.read()
#     image=MIMEImage(img_data, name=os.path.basename(image_path))
#     for image in 5:
#         count=1
#         msg.attach(str(count)+image)
#         count=count+1

    print("화이팅")
    smtp=smtplib.SMTP_SSL("smtp.naver.com",465)
    # smtp.starttls() <= TLS암호화 시 사용 465는 SSL
    smtp.login(user=my_mail,password=pwd)
    smtp.sendmail(my_mail,to_mail,msg.as_string())
    smtp.close()
    print(name, "성공")