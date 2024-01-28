from web3 import IPCProvider, Web3

w3 = Web3(IPCProvider(ipc_path="/tmp/geth.ipc"))

print(w3.fromWei(w3.eth.getBalance(w3.eth.coinbase), "ether"))
