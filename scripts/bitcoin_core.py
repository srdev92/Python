from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from bitcoinlib.wallets import wallet_create_or_open

from .mysql import MySQL
from pprint import pprint
import logging

class Client:
    def __init__(self, params):
        self.rpc_user       = params['Client']['user']        # rpc_user
        self.rpc_password   = params['Client']['password']    # rpc_password
        self.rpc_host       = params['Client']['host']        # rpc_host
        self.rpc_port       = params['Client']['port']        # rpc_port
        self.rpc_timeout    = params['Client']['timeout']     # rpc_timeout

        self.mysql_host     = params['Mysql']['host']         # mysql_host
        self.mysql_user     = params['Mysql']['user']         # mysql_user
        self.mysql_password = params['Mysql']['password']     # mysql_password
        self.mysql_database = params['Mysql']['database']     # mysql_database

        self.create_database()

    def create_database(self):
        print("1. Creating Database ...")
        db_uri = f"mysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}:3306/{self.mysql_database}"
        w = wallet_create_or_open('wallet_mysql', db_uri = db_uri)
        # w.info()
        print("\tcreated database!")

    def blocks(self):
        print("2. Connecting database ...")
        mysql = MySQL(self.mysql_host, self.mysql_user, self.mysql_password, self.mysql_database)
        mysql.connection()
        print("\tconnected database!")

        print("3. Connecting Client ...")
        rpc_client = AuthServiceProxy(f"http://{self.rpc_user}:{self.rpc_password}@{self.rpc_host}:{self.rpc_port}", timeout=int(self.rpc_timeout))
        print("\tconnected client!")

        print("4. Getting block of Client ...")
        block_count = rpc_client.getblockcount()
        print("\tBlock Count: ", block_count)

        blockhash = rpc_client.getblockhash(block_count)
        block = rpc_client.getblock(blockhash)
        nTx = block['nTx']

        print(block)

        print("\tBlock Hash: ", blockhash)
        print("\tMerkle Root: ", block['merkleroot'])
        print("\tBlock Size: ", block['size'])
        print("\tBlock Weight : ", block['weight'])
        print("\tNonce: ", block['nonce'])
        print("\tDifficulty: ", block['difficulty'])
        print("\tNumber of Tx: ", nTx)

        print("5. Analysing Blocks ...")
        i = 0
        while i < nTx:
            print(i, ":", block['tx'][i])
            i += 1
        print("Completed!")
