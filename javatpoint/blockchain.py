# importing the required libraries
import hashlib
import json
from time import time


# creating the Blockchain class
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", the_proof=100
        )

    # Creating a new block listing key/value pairs of
    # block information in a JSON object.
    # Reset the list of pending transactions &
    # append the newest block to the chain.
    def new_block(self, the_proof, previous_hash=None):
        the_block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.pending_transactions,
            "proof": the_proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(the_block)

        return the_block

    # Searching the blockchain for the most recent block.
    @property
    def last_block(self):
        return self.chain[-1]

    # Adding a transaction with relevant info to the 'blockpool' - list of pending tx's.
    def new_transaction(self, the_sender, the_recipient, the_amount):
        the_transaction = {"sender": the_sender, "recipient": the_recipient, "amount": the_amount}
        self.pending_transactions.append(the_transaction)
        return self.last_block["index"] + 1

    # receiving one block. Turning it into a string, turning that into
    # Unicode (for hashing). Hashing with SHA256 encryption,
    # then translating the Unicode into a hexidecimal string.
    def hash(self, the_block):
        string_object = json.dumps(the_block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
transaction1 = blockchain.new_transaction("Satoshi", "Alex", "10 BTC")
transaction2 = blockchain.new_transaction("Alex", "Satoshi", "2 BTC")
transaction3 = blockchain.new_transaction("Satoshi", "James", "10 BTC")
blockchain.new_block(10123)

transaction4 = blockchain.new_transaction("Alex", "Lucy", "2 BTC")
transaction5 = blockchain.new_transaction("Lucy", "Justin", "1 BTC")
transaction6 = blockchain.new_transaction("Justin", "Alex", "1 BTC")
blockchain.new_block(10384)

print("Genesis block: ", blockchain.chain)
