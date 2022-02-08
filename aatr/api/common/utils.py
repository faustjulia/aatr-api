import base64
import os


def gen_token(byte_length: int):
    return base64.urlsafe_b64encode(s=os.urandom(byte_length)).decode()


def gen_session_token():
    return gen_token(byte_length=64)
