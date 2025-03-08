import base64

def str_to_base64(x):
    return base64.b64encode(x.encode('utf-8'))
