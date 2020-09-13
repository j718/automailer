import yagmail
import csv
from pathlib import Path
from markdown2 import Markdown
import frontmatter

with ((data_dir:= Path('data')) / 'email_list.csv').open(mode='r') as csv_file:
    for row in csv.DictReader(csv_file):
        message = frontmatter.load(data_dir / 'message.md')
        yagmail.SMTP(
                message['sender'],
                password = message['password']
            ).send(
                to= row['email'],
                subject=message['subject'],
                contents=Markdown().convert(message.content.format(**row)), 
        )