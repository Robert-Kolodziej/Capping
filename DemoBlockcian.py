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

    def create_second_block(self):
        input("Input the school where the degree was achieved:  ")
        second_block = input
        second_block.hash = second_block.compute_hash()
        self.chain.append(second_block)
        print(second_block)

    def create_third_block(self):
        input("Input the year the degree was achieved:  ")
        third_block = input
        third_block.hash = third_block.compute.hash()
        self.chain.append(third_block)
        print(third_block)
