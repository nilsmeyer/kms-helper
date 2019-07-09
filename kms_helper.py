import base64
import boto3
import click

from getpass import getpass

client = None


@click.group()
@click.option('-p', '--profile', help="profile from AWS config to "
                                      "use")
def cli(profile=None):
    global client

    if profile is not None:
        session = boto3.session.Session(profile_name=profile)
    else:
        session = boto3.session.Session()

    client = session.client('kms')


@cli.command()
@click.option('-s', '--string', help="String to encrypt, optional")
@click.option('-f', 'filename', type=click.File('r', encoding='utf-8'),
              help="Read plaintext from file, use '-' for stdin")
def decrypt(string=None, filename=None):
    """Decrypt a string with KMS"""
    if string is None and filename is None:
        string = input("Ciphertext: ")
    elif filename is not None:
        string = filename.read()

    print(client.decrypt(
          CiphertextBlob=base64.b64decode(string))['Plaintext']
          .decode('utf-8'))


@cli.command()
@click.option('-k', '--key-id', required=True, help="KMS key id or "
                                                    "alias")
@click.option('-s', '--string', help="String to encrypt, optional")
@click.option('-f', 'filename', type=click.File('r', encoding='utf-8'),
              help="Read plaintext from file, use '-' for stdin")
def encrypt(key_id="", string=None, filename=None):
    """Encrypt a string with KMS, either from the CLI or stdin"""

    if string is None and filename is None:
        string = getpass(prompt='Plaintext: ')
    elif filename is not None:
        string = filename.read()

    ciphertext = client.encrypt(KeyId=key_id, Plaintext=string)

    print(base64.b64encode(ciphertext['CiphertextBlob']).decode('utf-8'))
