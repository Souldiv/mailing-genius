import sendgrid
import os
from sendgrid.helpers.mail import *


class send_mails():
    def __init__(self, sgapi=None):
        if sgapi is None:
            raise ValueError(
                'Object must be initialized with sendgrid api key')
        self.sg = sendgrid.SendGridAPIClient(apikey=sgapi)

    def build_attachment(self, content, Type, filename, content_id, disposition='attachment'):
        attachment = Attachment()
        attachment.content = content
        attachment.type = Type
        attachment.filename = filename
        attachment.disposition = disposition
        attachment.content_id = content_id
        return attachment

    def send(self, from_email, to, subject, text='test', attachments=None, template_fn=None):
        if template_fn is not None:
            with open(template_fn) as x:
                st = x.read()
            content = Content("text/html", st)
        content = Content('text/plain', text)
        from_email = Email(from_email)
        to_email = Email(to)
        subject = subject
        mail = Mail(from_email, subject, to_email, content)

        if attachments is not None:
            if not isinstance(attachments, list):
                raise ValueError(
                    'Expected attachments to be a list of Attachments')
            for atch in attachments:
                mail.add_attachment(attachment)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)

    def show_attachment_settings(self):
        disposition = "Disposition: \n - inline results in the attached" \
            " file being displayed automatically within the message." \
            " \n - attachment results in the attached file requiring " \
            "some action todisplay(e.g. opening or downloading the file"

        content_id = """The content id for the attachment. \n
        \n This is used when the disposition is set to "inline" and the attachment
        \n is an image, allowing the file to be displayed within the email body.
        """

        Type = """
        can be image/png or application/pdf
        """
        print(disposition)
        print("Content ID: ", content_id)
        print("Type: ", Type)
