from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Connect to the Bitcoin Core RPC server
rpc_user = 'localbitcoinuser'
rpc_password = 'localbitcoinpassword'
rpc_port = 8332  # Default RPC port for Bitcoin Core
rpc_url = f"http://{rpc_user}:{rpc_password}@localhost:{rpc_port}"
rpc_connection = AuthServiceProxy(rpc_url)

# Function to get transaction details using txid
def get_transaction_details(txid):
    try:
        return rpc_connection.getrawtransaction(txid, 1)
    except JSONRPCException as e:
        print(f"Error: {e.error['message']}")
        return None

# Example usage
txid = 'da917699942e4a96272401b534381a75512eeebe8403084500bd637bd47168b3'
transaction = get_transaction_details(txid)
if transaction:
    # Access and print required details from the transaction
    print(f"Transaction ID: {transaction['txid']}")
    print(f"Block Height: {transaction['height']}")
    print(f"Confirmations: {transaction['confirmations']}")
    print(f"Total Input Value: {transaction['vin'][0]['value']}")
    print(f"Total Output Value: {transaction['vout'][0]['value']}")
    # Access input and output details as needed
    # For example: transaction['vin'][0]['addr'] to get sender's address
else:
    print('csca')
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

"""
    test
"""
import requests
import json

response = requests.get('https://blockchair.com/bitcoin/transaction/da917699942e4a96272401b534381a75512eeebe8403084500bd637bd47168b3')
print(response.text)

json_data = response.json()

# Parse and process the JSON data
if response.status_code == 200:
    # Successful response
    # Access the JSON data as a Python dictionary
    print(json_data)
else:
    # Failed response
    print("Error:", response.status_code)
