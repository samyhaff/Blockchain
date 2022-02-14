import hashlib
from time import time
import json

DIFFICULTY = 4

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.hash()

    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"FROM: {self.sender} TO: {self.recipient} AMOUNT: {self.amount}"


class Blockchain:
    def __init__(self):
        self.blocks = []
        self.blocks.append(self.create_first_block())
        self.transactions = []

    def create_first_block(self):
        return Block(0, time(), None, None, None)

    def new_transaction(self, transaction):
        self.transactions.append(transaction)

    def new_block(self, block):
        self.transactions = []
        self.blocks.append(block)

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(proof, last_proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(proof, last_proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:DIFFICULTY] == "0" * DIFFICULTY
