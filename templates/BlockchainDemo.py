import hashlib
import json
import random
from random import randint

input("What do you want to hash?: ")
nonce = random.randint
previous_hash = 0
block = 1
print(nonce)
class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(input, nonce, previous_hash)

    def create_block(self, input, nonce, previous_hash):
        block = dict(index=len(input.chain) + 1, nonce=nonce, previous_hash=previous_hash)
        input.chain.append(block)
        return block

    def get_previous_block(input):
        return input.chain[-1]

    def proof_of_work(input, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce ** 2 - previous_nonce ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(input, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(input, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce ** 2 - previous_nonce ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


# Creating our Blockchain
blockchain = Blockchain();


# Mining a new block
class JsonResponse(object):
    pass


def mine_block(request):
    if request.method == 'GET':
        previous_block = blockchain.get_previous_block()
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(nonce, previous_hash)
        response = {'message': 'Congratulations, you just mined a block!',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'nonce': block['nonce'],
                    'previous_hash': block['previous_hash']}
    return JsonResponse(response)


# Getting the full Blockchain
def get_chain(request):
    if request.method == 'GET':
        response = {'chain': blockchain.chain,
                    'length': len(blockchain.chain)}
    return JsonResponse(response)


# Checking if the Blockchain is valid
def is_valid(request):
    if request.method == 'GET':
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {'message': 'All good. The Blockchain is valid.'}
        else:
            response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return JsonResponse(response)
