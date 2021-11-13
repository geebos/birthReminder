import os
import smtplib
import sys
from datetime import date
from email.mime.text import MIMEText

import sxtwl

import utils

if __name__ == '__main__':
    data = []
    with open('birthdays.txt', 'r') as f:
        for line in f:
            data.append(line.split(' '))
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        sys.exit(-1)
    private_key = private_key.replace('\\n', '\n')

    today = date.today()
    lunar = sxtwl.Day_fromSolar(today.year, today.month, today.day)
    lunar_month = lunar.getLunarMonth()
    lunar_day = lunar.getLunarDay()
    solar_month = today.month
    solar_day = today.day

    send_list = []
    for birthday, date_type, email in data:
        if len(birthday) != 4:
            continue

        if not birthday.isdigit():
            continue

        month, day = int(birthday[:2]), int(birthday[2:])
        try:
            if date_type == '1' and month == lunar_month and day == lunar_day:
                send_list.append((month, day, '阴历', utils.decode(email, private_key)))
            elif date_type == '2' and month == solar_month and day == lunar_day:
                send_list.append((month, day, '阳历', utils.decode(email, private_key)))
            else:
                pass
        except:
            continue

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(username, password)
    subject = 'birthday reminder'

    for month, day, date_type, email in send_list:
        content = '今天是%s%d月%d号，您订阅的生日提醒邮件已送达。' % (date_type, month, day)
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = email
        try:
            s.sendmail(username, email, msg.as_string())
        except smtplib.SMTPException as e:
            continue
