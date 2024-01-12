from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

rpc_host = '127.0.0.1'
rpc_user = 'localbitcoinuser'
rpc_password = 'localbitcoinpassword'
rpc_port = 8332
rpc_timeout = 120

rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}", timeout=int(rpc_timeout))
#transaction_id = '35092b3889922e358155acac1bcd82c43d1d7286253fa07e018bd0f5d72836a5'
transaction_id = 'da917699942e4a96272401b534381a75512eeebe8403084500bd637bd47168b3'
transaction_details = rpc_client.gettransaction(transaction_id)
print(transaction_details)
transaction_json = json.dumps(transaction_details, indent=4)
print(transaction_json)

print('end')
