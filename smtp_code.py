import smtplib

# Use smtp.gamil.com for gmail
# use smtp.live.com for hotmail
# Use smtp.mail.yahoo.com for yahoo

my_email = "mohit20064321@gmail.com"
password = "kqde lbhg zxoi kque"       # This is the generated app password from your google account for gmail.com

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()                     # TLS -> Transport Layer Security
    connection.login(user=my_email, password=password)

    # connection.sendmail(from_addr=my_email, to_addrs="abcxyz12327@myyahoo.com", msg="Hello abc xyz bro!")  # This will sent msg int he spam folder of the reciever. 
    connection.sendmail(from_addr=my_email, to_addrs="abcxyz12327@myyahoo.com", msg="Subject:Hello abc xyz bro!\n\nThis is the body!!!")

    # connection. close()
    # Using "with" to avoid closing the connection

# We can use "pythonanywhere" webiste to host our programme online and it will run daily on schedule we give there.