import utils
from models.Block import Block
from models.Client import Client
from models.Transaction import Transaction

# global variable
last_block_hash = ""
TPCoins = []
last_transaction_index = 0

Dinesh = Client()
t0 = Transaction("Genesis", Dinesh.identity, 500.0)
block0 = Block()
block0.previous_block_hash = None
Nonce = None
block0.verified_transactions.append(t0)
digest = hash(block0)
last_block_hash = digest
TPCoins.append(block0)
utils.dump_blockchain(TPCoins)
