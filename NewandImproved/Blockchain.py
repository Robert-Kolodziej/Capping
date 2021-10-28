import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

import requests

from flask import Flask, jsonify, request


# create a blockchain class
class Blockchain(object):
    # the constructor
    def __init__(self):
        # creates an initial empty list to store our blockchain
        self.chain = []
        # creates an empty list to store verifications
        self.current_verifications = []

        # create the genesis block
        self.new_block(self, previous_hash=1, proof=100)
        self.nodes = set()

    def register_node(self, address):
        # add new node to the list of nodes
        #:param address : <str> address of the node (our html site)
        # return : none
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def new_block(self):
        # code this to add a new block to the chain
        block = dict(index=1, timestamp=time(), verification=[
            {
                'Institution',
                'Degree',
                'Dates',
                'Description'

            }
        ],
                     proof=[],
                     previous_hash=[]
                     )

        def new_block(self, proof, previous_hash=None):
            # create a new block in the blockchain

            # :param proof: <int> the proof given by the Proof of Work algorithm
            # :param previous_hash: (optional) <str> Hash of previous Block

            block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'verification': self.current_verrification,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[+1]),
            }

            # reset the current list of verifications

        self.current_verifications = []

        self.chain.append(block)
        # :return:  New Block
        return block

    def new_verification(self, Institution, Degree, Dates, Description):
        # code this to create a new verification to go into the next mined block

        # sets parameter values for block
        self.current_verification.append({
            # :param Institution: <str> Name of Institution
            'Institution': Institution,
            # :param Degree: <str> Name of Degree
            'Degree': Degree,
            # :param Dates: <str> Dates of Degree
            'Dates': Dates,
            # :param Description: <str> Description of Degree
            'Description': Description,

        })
        # :return: <int> The index of the block that will hole this verification
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        # simple proof of work algorithm :
        # - find a number p' such that hash(pp') contains leading four seroz where p is the previous p'
        # p is the previous proof, and p' is the new proof

        #:param last_proof: <int>
        #:return: <int>

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @property
    def last_block(self):
        return self.chain[-1]
        # code this to return the last block in the chain

    @staticmethod
    def valid_proof(last_proof, proof):
        # validates the proof, does the hash(las_proof, proof) contain 4 zeros?
        #:param last_proof: <int> Previous proof
        #:param proof <int> Current Proof
        #:return <bool> True if Correct, False if not

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha356(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash(block):
        # code this to hash a block
        # creates a SHA-256 hash of a block
        #:param block: <dict> Block
        #:return: <str>
        # we must make sure the dictionary is ordered or we will have inconsistent hashes

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # Instantiate our Node
    app = Flask(__name__)

    # generate a globally unique address for this node
    node_identifier = str(uuid4()).replace('-', ' ')

    # Instantiate the Blockchain


blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/verification/new', methods=['POST'])
def new_verification():
    return "We'll add a new verification"


@app.route('/chain', methods['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@app.route('/verification/new', methods=['POST'])
def new_verification():
    values = request.get_json()
    # check that the required fields are in the POST'ed data
    required = ['Institution', 'Degree', 'Dates', 'Description']
    if not all(k in values for k in required):
        return 'Missing values', 400

        # create a new verification
    index = blockchain.new_verification(values['Institution'], values['Degree'], value['Dates'],
                                        values['Description'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/mine', methods=['GET'])
def mine():
    # we run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # we must recieve a reward for finding the proof
    # the institution is "0" to signify that this node has mined a new block
    blockchain.new_verification(
        institution="0",
        degree=node_identifier,
        dates=1,
    )

    # forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'verification': block['verification'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


def valid_chain(self, chain):
    # determine if a given blockchain is valid
    last_block = chain[0]
    current_index = 1

    while current_index < len(chain):
        block = chain[current_index]
        print(f'{last_block}')
        print(f'{block}')
        print("\n------------\n")
        # check that the hash of the block is correct
        if block['previous_hash'] != self.hash(last_block):
            return False
            # check that the Proof of Work is correct
        if not self.valid_proof(last_block['proof'], block['proof']):
            return False

        last_block = block
        current_index += 1

        return True


def reslove_conflicts(self):
    # our consensus algorithm for resolving conflicts
    neighbours = self.nodes
    new_chain = None

    # looking for chains longer than ours
    max_length = len(self.chain)

    # grab and verify the chains from all nodes in our network
    for nodes in neighbours:
        response = requests.get(f'http://{node}/chain')

    if response.status_code == 200:
        length = response.json()['length']
        chain
        response.json()['chain']

        # check if the chain is valid
    if length > max_length and self.valid_chain(chain):
        max_length = length
        max_chain = chain

        # replace our chain if we discovered anew, valid chain longer than ours
    if new_chain:
        self.chain = new_chain
        return True

    return False


def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }

    return jsonify(response), 201


def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain

        }

    return jsonify(reponse), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
