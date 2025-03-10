import base64
import sys

def str_to_base64(x):
    return base64.b64encode(x.encode('utf-8'))
