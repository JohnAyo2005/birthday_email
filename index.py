import pandas as pd
import time
from datetime import datetime
import smtplib

EMAIL = "Your_Email"
PassWD = "Your_Email_Password"


def SendEmailFunc(send_to,email_subject,wish_msg):
    #Setup gmail with SMTP

    smtp_email = smtplib.SMTP("smtp.gmail.com",587)

    #initialize the smtp session
    smtp_email.starttls()

    #login with the credentials
    smtp_email.login(EMAIL,PassWD)
    print(smtp_email)
    #Setup Email template to sent email with arguments
    smtp_email.sendmail(EMAIL,send_to, f"Subject: {email_subject}\n\n{wish_msg}")

    #Ending the session
    smtp_email.quit()

    print("Birthday Email successfully sent to" + str(send_to) + "\n The subject is: " + str(email_subject) + "\nThe message is:" + str(wish_msg))


def MainCode():
   
    #Read CSV file using pandas
   
    dataframe = pd.read_csv(r"birthday_list.csv")
    print(dataframe)
    #check todays Time and date
    today = datetime.now().strftime("%d-%m")

    #check Year format

    currentYear = datetime.now().strftime("%Y")

    #index where we store which friends birthday are wished
    friend= []

    for index,item in dataframe.iterrows():
        msg = "Happy Birthday To My Dear " + str(item['name']+ "Wish you many many happy returns of the day")
        #getting the birthdate from the excel sheet
        bday = datetime.strptime(item['birthday'], "%Y-%d-%m")

        bday = bday.strftime("%d-%m")
        #if conditions for  matching and sending the birthday message
        if (today == bday) and currentYear not in str(item['year']):
            #call the functions
            SendEmailFunc(item['email'], "Happy Birthday", msg)
            friend.append(index)
    for i in friend:
       
        yr = dataframe.loc[i, 'year']
        dataframe.loc[i, 'year'] = str(yr) + ',' + str(currentYear)



if __name__ == "__main__":
    MainCode()
