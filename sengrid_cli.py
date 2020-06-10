import sendgrid
import os
from sendgrid.helpers.mail import *
import base64
import pandas
import argparse
import sys
import config

def email(sender,to,message,subject,attach=False):
    sg = sendgrid.SendGridAPIClient(apikey=config.api_key)
    from_email = Email(sender)
    to_email = Email(to)
    content = Content("text/html",message)
    if(bool(attach)):
        with open(attach,'rb') as f:
            data = f.read()
            f.close()
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.content = encoded
        
        if attach.endswith('png'):
            attachment.type = 'image/png'
        else:
            attachment.type = 'document/pdf'
        attachment.filename = attach.split('/')[-1]
        attachment.disposition = 'inline'
        attachment.content_id = 'file'
        print(attachment.type,attachment.filename)
        try:
            mail = Mail(from_email, subject, to_email, content)
            mail.add_attachment(attachment)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("mail sent to",to)
            print(attach)
            print(response.status_code)
        except:
            print("mail not sent to ", to)
            pass

    else:
        try:
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("mail sent to",to)
            print(response.status_code)
        except:
            print("mail not sent to ", to)
            pass
        
        
def main():
    parser = argparse.ArgumentParser(description='Bulk Mailing App')
    parser.add_argument("-n", "--html", help="Give html file path", required=True)
    parser.add_argument("-f", "--file", help="give file of mail address", required=True)
    parser.add_argument("-a", "--attach", help="give attachment file path")
    
    results = vars(parser.parse_args())
    
    if results['html']:
        if results['file']:
            
            if results['file'].endswith('csv'):
                file_email = pandas.read_csv(results['file'])
            else:
                file_email = pandas.read_excel(results['file'])
                
            subject = input("Enter Subject:")
            print('Choose your mail column from these:', *file_email.columns, sep='\n')
            mail_col = input("Enter Mail column:")
            
            with open(results['html']) as file:
                message = file.read()
            
            if results['attach']:
                                    
                for i in file_email[mail_col]:   
                    email("dscvitvellore@gmail.com", i ,message,subject,results['attach'])
                    
            else:
                for i in file_email[mail_col]:   
                    email("dscvitvellore@gmail.com", i ,message,subject)
                    
        else:
            print('Give mail list file!!')
            sys.exit()
        
    else:
        print('Give content file!!')
        sys.exit()    
    


if __name__  == "__main__":
    main()
   

