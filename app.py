from time import time
from flask import Flask, request
import json
from uuid import uuid4
from blockchain import Blockchain, Transaction, Block

app = Flask(__name__)

node_identifier = str(uuid4()).replace("-", "")

blockchain = Blockchain()


@app.route("/mine", methods=["GET"])
def mine():
    last_block = blockchain.blocks[-1]
    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)

    transaction = Transaction("Network", node_identifier, 50)
    blockchain.new_transaction(transaction)
    block = Block(len(blockchain.blocks) + 1,
                  time(),
                  blockchain.transactions,
                  last_block.hash,
                  proof
                  )
    blockchain.new_block(block)

    return "New block forged!\n"

@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = request.get_json()
    transaction = Transaction(values["sender"], values["recipient"], values["amount"])
    blockchain.new_transaction(transaction)

    return "Transaction will be added to the blockchain\n"


@app.route("/chain", methods=["GET"])
def chain():
    return json.dumps([b.__dict__ for b in blockchain.blocks])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
