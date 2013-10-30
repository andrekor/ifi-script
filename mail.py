import smtplib
import string
import getpass

def mail():
    f = raw_input("your username: ")
    FROM = f if "@" in f else (f + "@ulrik.uio.no")
    t = raw_input("receiver's username: ") 
    TO = t if "@" in t else (t + "@ulrik.uio.no")
    SUBJECT = raw_input("Subject: ")
    text = raw_input("message: ")
    s = smtplib.SMTP()
    BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT ,
            "",
            text
            ), "\r\n")
    try:
        s.connect('smtp.uio.no', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        pa = getpass.getpass()
        s.login(FROM, pa)
        s.sendmail(FROM, [TO], BODY)
    except:
        print "Mail was not sent, make sure you typed correct password"

if __name__ == "__main__":
    mail()
