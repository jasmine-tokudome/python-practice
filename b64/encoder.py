import base64
import sys

def str_to_base64(x):
    return base64.b64encode(x.encode('utf-8'))

def main():
    print(str_to_base64(sys.argv[1]))

if __name__ == '__main__':
    main()

__all__ = ['str_to_base64']
