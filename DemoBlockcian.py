import json
from hashlib import sha256


class Block:
    def __init__(self, index, certificate, previous_hash, nonce=0):
        self.index = index
        self.certificate = certificate
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:

    def __init__(self):
        self.unconfirmed_certificate = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        input("Input the degree achievd:  ")
        genesis_block = input
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
        print(genesis_block)

    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        block.nonce =
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True


def main():



main()