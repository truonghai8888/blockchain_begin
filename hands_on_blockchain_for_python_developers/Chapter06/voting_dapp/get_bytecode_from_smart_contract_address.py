from web3 import IPCProvider, Web3

w3 = Web3(IPCProvider(ipc_path="/tmp/geth.ipc"))

with open("address.txt", "r") as f:
    content = f.read().rstrip("\n")

address = content
