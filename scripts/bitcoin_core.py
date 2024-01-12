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

        # self.create_wallet_table()
        self.create_mysql_connection()
        self.create_proxy()
        self.get_blocks()

    def create_wallet_table(self):
        print("1. Creating Database ...")
        db_uri = f"mysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}:3306/{self.mysql_database}"
        w = wallet_create_or_open('wallet_mysql', db_uri = db_uri)
        w.info()
        print("\tcreated database!")

    def create_mysql_connection(self):
        print("2. Connecting database ...")
        self.mysql = MySQL(self.mysql_host, self.mysql_user, self.mysql_password, self.mysql_database)
        self.mysql.connection()
        print("\tconnected database!")

    def create_proxy(self):
        print("3. Creating Proxy ...")
        self.rpc_client = AuthServiceProxy(f"http://{self.rpc_user}:{self.rpc_password}@{self.rpc_host}:{self.rpc_port}", timeout=int(self.rpc_timeout))
        print("\tcreated proxy!")

    def get_blocks(self):
        print("4. Getting block of Client ...")
        self.block_count = self.rpc_client.getblockcount()
        print("\tBlock Count: ", self.block_count)

    def analyze(self):
        print("5. Analysing Blocks ...")
        pos = 0
        bc = 0
        while bc < self.block_count:
            blockhash = self.rpc_client.getblockhash(self.block_count)
            block = self.rpc_client.getblock(blockhash)
            nTx = block['nTx']
            
            print("\tBlock Hash: ", blockhash)
            print("\tMerkle Root: ", block['merkleroot'])
            print("\tBlock Size: ", block['size'])
            print("\tBlock Weight : ", block['weight'])
            print("\tNonce: ", block['nonce'])
            print("\tDifficulty: ", block['difficulty'])
            print("\tNumber of Tx: ", nTx)

            txc = 0
            while txc < nTx:
                pos += 1
                print("\t", pos, ":", block['tx'][txc])

                #rpc_client.gettransaction(block['tx'][txc])

                txc += 1
            
            print(bc)
            bc += 1

        print("Completed!")
