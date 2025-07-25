import imaplib
import email
import os
from dotenv import load_dotenv

load_dotenv()

imap_server = "imap.gmail.com"
email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("INBOX")

_, msgnums = imap.search(None,"ALL")

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
