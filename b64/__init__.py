from .encoder import *
from .decoder import *

print(f'init: {__name__}')

# >>> import b64
# init: b64
# >>> b64.str_to_base64('phtyon')
# b'cGh0eW9u'
# >>> dir(b64)
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'base64_to_str', 'decoder', 'encoder', 'str_to_base64']
