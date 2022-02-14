from flask import Flask, request
import json
from uuid import uuid4
from blockchain import Blockchain, Transaction, Block

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "TODO\n"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "TODO\n"

@app.route('/chain', methods=['GET'])
def chain():
    return json.dumps([b.__dict__ for b in blockchain.blocks])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
