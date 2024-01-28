from web3 import HTTPProvider, Web3

web3 = Web3(HTTPProvider("http://localhost:7545"))

nonce = web3.eth.getTransactionCount("0x6d3eBC3000d112B70aaCA8F770B06f961C852014")
print(nonce)
