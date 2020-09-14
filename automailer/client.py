import click
from automailer.app import main
from pathlib import Path

DATA_DIR = Path('data')
EMAIL_LIST_PATH =  DATA_DIR/ 'email_list.csv'
MESSAGE_PATH = DATA_DIR/ 'message.md'

@click.command()
@click.option('--email_list_path', type=click.Path(exists=True), default=EMAIL_LIST_PATH, help='Path to Email List.')
@click.option('--message_path', type=click.Path(exists=True), default=MESSAGE_PATH, help='Path to message.')
def mail(email_list_path, message_path):
    click.echo(click.style('Sending Message!', blink=True, fg='yellow'))
    main(email_list_path, message_path)
    click.echo(click.style('Messages Sent!', fg='green'))
