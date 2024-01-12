import sys

from scripts.conf import Conf
from scripts.bitcoin_core import Client

def parse(conf_file):
    conf = Conf(conf_file)
    params = conf.params()

    client = Client(params)
    client.analyze()

def main():
    if len(sys.argv) < 2:
        print('Usage: ')
    else:
        parse(sys.argv[1])

if __name__ == '__main__':
    main()
