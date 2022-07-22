# blockchain.py
import hashlib
import pickle

def hash_function(obj):
    return hashlib.md5(pickle.dumps(obj)).hexdigest()

class BlockChain():
    def __init__(self):
        self.blockchain = []

    def create_block(self, data):
        if len(self.blockchain) == 0:
            next_block = (data, None) # Genesis block
            return next_block
        else:
            genesis_block = self.blockchain[0]
            previous_block = self.blockchain[-1] # when blockchain length == 1, both blocks are the genesis block.
            next_block = (data, hash_function((genesis_block, previous_block))) # Hash the genesis block with the previous block
            return next_block
    
    def add_block(self, next_block):
        self.blockchain.append(next_block)
        if not self.verify():
            self.blockchain.pop()
            return False
        else:
            return True
    
    def verify(self):
        for i, block in list(enumerate(self.blockchain))[::-1]:
            _, lasthash = block
            if i == 0:
                return True
            actual_lasthash = hash_function((self.blockchain[0], self.blockchain[i-1]))
            if actual_lasthash != lasthash:
                return False
        return True # Edge case where no blocks exist yet

    def __repr__(self):
        r=""
        for (i, block) in enumerate(self.blockchain):
                data, lasthash = block
                r += f"\nINSTRUCTION: {i}\nLAST HASH: {lasthash}\n{data}\n"
        return r
