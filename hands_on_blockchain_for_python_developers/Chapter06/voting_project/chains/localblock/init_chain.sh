#!/bin/sh
geth --rpc --rpcaddr 127.0.0.1 --rpcport 8545 --rpcapi admin,debug,eth,miner,net,personal,shh,txpool,web3,ws --ws --wsaddr 127.0.0.1 --wsport 8546 --wsapi admin,debug,eth,miner,net,personal,shh,txpool,web3,ws --datadir /home/arjuna/Documents/WritingBook/hands-on-blockchain-for-python-developers/chapter_06/voting_project/chains/localblock/chain_data --maxpeers 0 --networkid 1234 --port 30303 --ipcpath /tmp/tmpvnbzbt29/geth.ipc --nodiscover --mine --minerthreads 1 init /home/arjuna/Documents/WritingBook/hands-on-blockchain-for-python-developers/chapter_06/voting_project/chains/localblock/genesis.json