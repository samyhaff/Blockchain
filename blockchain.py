import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode()
            + str(self.timestamp).encode()
            + str(self.data).encode()
            + str(self.previous_hash).encode()
        )
        return sha.hexdigest()

def create_first_block():
    return Block(0, datetime.now(), 'First Block', '0')

def create_next_block(last_block):
    index = last_block.index + 1
    timestamp = datetime.now()
    data = "Test" + str(index)
    hash = last_block.hash

    return Block(index, timestamp, data, hash)

if __name__ == '__main__':
    first_block = create_first_block()
    blockchain = [first_block]

    block = create_next_block(first_block)
    print(f"Block #{block.index} has been added to the blockchain")
    print(f"Hash: {block.hash}")
