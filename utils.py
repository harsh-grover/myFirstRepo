#usr/bin/env python

import smtplib
import traceback
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

import logging, logging.handlers
import nana
def initialize_logger(filename, level=''):
    file_name = "/var/www/blackbuck-web/app/logs/%s" % filename
    log = logging.getLogger(file_name)
    handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=10485760, backupCount=5)
    formatter = logging.Formatter('%(asctime)s.%(msecs)d: %(filename)s: %(lineno)d: %(funcName)s: %(levelname)s: %(message)s', "%Y%m%dT%H%M%S")
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    return log

def initialize_logger(filename, level=''):
    file_name = "/var/www/blackbuck-web/app/logs/%s" % filename
    log = logging.getLogger(file_name)
    handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=10485760, backupCount=5)
    formatter = logging.Formatter('%(asctime)s.%(msecs)d: %(filename)s: %(lineno)d: %(funcName)s: %(levelname)s: %(message)s', "%Y%m%dT%H%M%S")
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)

    return log

log = initialize_logger('utils.log')
print(jaka)
def send_mail(subject, message, server="localhost"):

    sender = "monitor@headrun.com"
    to = ['yatish@headrun.com']
    cc = []

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg['Cc'] = COMMASPACE.join(cc)
    msg.attach(MIMEText(message))

    addresses = []
    for x in to:
        addresses.append(x)
    for x in cc:
        addresses.append(x)

    try:
        smtp = smtplib.SMTP(server)
        smtp.sendmail(sender, addresses, msg.as_string())
        smtp.close()
        log.info("Mail Sent Successfully")
    except smtplib.SMTPException as e:
        log.error("%s", traceback.format_exc())

