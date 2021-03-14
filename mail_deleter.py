from imaplib import IMAP4, IMAP4_SSL
import pprint
import email

class Mail():

    def __init__(self, host, user, password, inbox):
        self.host = host
        self.user = user
        self.password = password
        self.inbox = inbox

    def connect_to_account(self):
        imap =  IMAP4_SSL(self.host)
        imap.login(self.user, self.password)
        self.imap = imap


    def show_available_inboxes(self):
        for i in self.imap.list()[1]:
            print(i)


    def delete_mails(self):
        self.imap.select(self.inbox)

        tmp, data = self.imap.search(None, 'ALL')
        for i, num in enumerate(data[0].split()):
            self.imap.store(num, '+FLAGS', '\\Deleted')
            print(f"Message Nr. {i} deleted")

        self.imap.expunge()
        self.imap.close()



if __name__ == '__main__':
    mail = Mail("IMAP_SERVER", "USERNAME", "PASSWORD", "INBOX")
    mail.connect_to_account()
    mail.show_available_inboxes()
    mail.delete_mails()