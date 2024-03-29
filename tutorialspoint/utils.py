# import libraries
import hashlib


def display_transactions(transaction):
    # for transaction in transactions:
    dict = transaction.to_dict()
    print("sender: " + dict["sender"])
    print("-----")
    print("recipient: " + dict["recipient"])
    print("-----")
    print("value: " + str(dict["value"]))
    print("-----")
    print("time: " + str(dict["time"]))
    print("-----")


def dump_blockchain(TPCoins: list):
    print("Number of blocks in the chain: " + str(len(TPCoins)))
    for x in range(len(TPCoins)):
        block_temp = TPCoins[x]
        print("block # " + str(x))
        for transaction in block_temp.verified_transactions:
            display_transactions(transaction)
            print("--------------")
        print("=====================================")


def sha256(message):
    return hashlib.sha256(message.encode("ascii")).hexdigest()


def mine(message, difficulty=1):
    assert difficulty >= 1
    prefix = "1" * difficulty
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print("after " + str(i) + " iterations found nonce: " + digest)
            return digest
