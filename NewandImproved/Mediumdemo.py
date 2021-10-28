
# create a blockchain class
class Blockchain(object):
    # the constructor
    def __init__(self):
        # creates an initial empty list to store our blockchain
        self.chain = []
        # creates an empty list to store verifications
        self.current_verifications = []

    def new_block(self):
        # code this to add a new block to the chain

        pass

    def new_verification(self):
        # code this to create a new verification to go into the next mined block
        pass

    @staticmethod
    def hash(block):
        # code this to hash a block
        pass

    @property
    def last_block(self):
        # code this to return the last block in the chain
        pass
