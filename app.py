# 202020V Blockchain created March 2021

import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="202020V Blockchain 3/27/21. Remember this! Peace and Light!", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Orion", '100 BTC') 
t2 = blockchain.new_transaction("Orion", "Micah", '99 BTC')
t3 = blockchain.new_transaction("Micah", "Nypie", '33 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Satoshi", "Peer3", '80 BTC') 
t5 = blockchain.new_transaction("Satoshi", "Peer2", '36 BTC')
t6 = blockchain.new_transaction("Satoshi", "Peer3", '72 BTC')
blockchain.new_block(6789)

t7 = blockchain.new_transaction("Facebook", "Orion", '30 BTC')
t8 = blockchain.new_transaction("Peer2", "Peer7", '0.5 BTC')
t9 = blockchain.new_transaction("Khufu", "Community", '10 BTC')
blockchain.new_block(1120)

t10 = blockchain.new_transaction("202020V", "JaiiEliasAri", '21 BTC')
t11 = blockchain.new_transaction("JaiiEliasAri", "Micah", '4.3 BTC')
t12 = blockchain.new_transaction("Nintendo", "202020V", '32 BTC')
blockchain.new_block(13014)

t10 = blockchain.new_transaction("Sega", "Nypie", '28 BTC')
t11 = blockchain.new_transaction("Disney", "Nypie", '19 BTC')
t12 = blockchain.new_transaction("Nintendo", "Orion", '32 BTC')
blockchain.new_block(121515)


print("Zion block: ", blockchain.chain) # name of the first block typically called Genesis. I rather call it Zion. LOL.