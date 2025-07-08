from collections import defaultdict
import hashlib

class Block:
    def __init__(self, vendor_code, amount, previous_hash):
        block_string = str(vendor_code) + str(amount) + str(previous_hash)
        self.amount = amount
        self.hash = hashlib.sha256(block_string.encode('utf-8')).hexdigest()
    
class TransactionGroup:
    def __init__(self): 
        self.structure = {}
        self.sources = defaultdict(int)
        self.block = {}
        
    def create_source(self, source_code, amount):
        self.structure[source_code] = set()
        self.sources[source_code] = amount
        self.block[source_code] = Block("0", amount, "0")
        
    def create_transaction(self, vendor_code, source_code, amount, leaf = False):
        if leaf: 
            self.leaf_end(vendor_code, source_code, amount)
            return
        
        self.sources[vendor_code] -= amount
        self.sources[source_code] += amount
        
        vendor_block = self.block[vendor_code]
        source_block = Block(vendor_code, amount, vendor_block.hash)
        self.block[source_code] = source_block
        
        self.structure[vendor_code].add(source_code)
        self.structure[source_code] = set()
        
    def leaf_end(self, vendor_code, source_code, amount):
        self.sources[vendor_code] -= amount
        self.structure[vendor_code].add(source_code)
        
    def balance(self):
        return "Balanced" if sum(self.sources.values()) == 0 else "Anamoly"
        
        
group = TransactionGroup()
group.create_source(1234, 100)
print(group.structure, group.sources, group.block)
group.create_transaction(1234, 1243, 10)
print(group.structure, group.sources, group.block)
print(group.balance())
group.create_transaction(1234, 13, 90)
group.create_transaction(13, 14, 90, True)
print(group.balance())
group.create_transaction(1243, 14, 10, True)
print(group.balance())
