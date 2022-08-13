import pandas as pd
import smtplib


# Path must be like: "/Users/xfarooqi/Desktop/100Days/Day5/Day6/coree.csv"
df =pd.read_csv("Path of File/coree.csv", index_col = False)

name_col = df["Full Name"]  #Renmae it to names and delete the Column Below

names = name_col.iloc[0:1]
print(names)
email_col = df["Email"]
emails = email_col.iloc[0:1]
print(emails)


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
# Setting the Login Access
server.login("Enter You Email", "Enter App Password")

import smtplib

# Email Generation
for name in names:
    
    # Subject of the Email
    subject = "GDSC Core Team Selection"
    
    # Body of the Email
    body = f'Hello {name},'+ """
    
This is the meeting for the selection of Core Team. Camera and Mic must be turned on. There will be few questions regarding the application, be ready for an interactive session.

Book a Meeting Slot Link: ABC.XYZ
 
 
Abdul Raheem
Microsoft Learn Student Ambassador
Mobile: +xx xxxxx xxx
Abdul.Raheem@studentambassadors.com
     """  
    
    msg = f'Subject: {subject}\n\n{body}'
    
    for email in emails:
        print("Hello", email + "\n")
        server.sendmail("Enter You Email Id", email,
                    msg)  # Sending the Email
    