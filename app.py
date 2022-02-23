#!/usr/bin/env python
"""Flask server to serve the block API."""

import json
from time import time
import argparse
from uuid import uuid4
from flask import Flask, request
from blockchain import Blockchain, Transaction, Block

parser = argparse.ArgumentParser(description="A blockchain simulation")
parser.add_argument("-p", "--port", type=int, help="Port number", default=80)

args = parser.parse_args()
port = args.port

app = Flask(__name__)

NODE_IDENTIFIER = str(uuid4()).replace("-", "")

blockchain = Blockchain()


@app.route("/mine", methods=["GET"])
def mine():
    """Mine Samycoin."""
    last_block = blockchain.blocks[-1]
    last_proof = last_block.proof
    proof = blockchain.proof_of_work(last_proof)

    transaction = Transaction("Network", NODE_IDENTIFIER, 50)
    blockchain.new_transaction(transaction)
    block = Block(
        len(blockchain.blocks) + 1,
        time(),
        blockchain.transactions,
        last_block.hash,
        proof,
    )
    blockchain.new_block(block)

    return "New block forged!\n"


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    """Submit a new transaction."""
    values = request.get_json()
    transaction = Transaction(values["sender"], values["recipient"], values["amount"])
    blockchain.new_transaction(transaction)

    return "Transaction will be added to the blockchain\n"


@app.route("/chain", methods=["GET"])
def chain():
    """Display the block chain."""
    return json.dumps([b.__dict__ for b in blockchain.blocks])


@app.route("/nodes", methods=["GET"])
def nodes():
    """List known nodes."""
    return json.dumps(list(blockchain.nodes))


@app.route("/register", methods=["POST"])
def register_nodes():
    """Register a new node."""
    json_values = request.get_json()
    for node in json_values["nodes"]:
        blockchain.register_node(node)

    return "New node has been added\n"


@app.route("/resolve", methods=["GET"])
def resolve():
    """Resolve the blockchain."""
    replaced = blockchain.resolve_conflicts()

    if replaced:
        return "Our chain was replaced!\n"

    return "Our chain was not replaced.\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
