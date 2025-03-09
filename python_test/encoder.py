import base64
import sys

def str_to_base64(x):
    return base64.b64encode(x.encode('utf-8'))

print(str_to_base64(sys.argv[1]))

# sys.argvはpython3コマンド以降の値を要素に持つリスト
# ※つまりターミナル上では「python3 sys.argv[0] sys.argv[0]」という意味。

# print(sys.argv)
