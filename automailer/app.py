import yagmail
import csv
from pathlib import Path
from markdown2 import Markdown
import frontmatter

def main(email_list_path: Path, message_path: Path):
    assert email_list_path.exists()
    assert message_path.exists()
    with (email_list_path).open(mode='r') as csv_file:
        for row in csv.DictReader(csv_file):
            message = frontmatter.load(message_path)
            yagmail.SMTP(
                    message['sender'],
                    password = message['password']
                ).send(
                    to= row['email'],
                    subject=message['subject'],
                    contents=Markdown().convert(message.content.format(**row)), 
            )

if __name__ == "__main__":
    main()