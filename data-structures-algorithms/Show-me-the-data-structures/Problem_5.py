#!/usr/bin/env python
# coding: utf-8



import datetime
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)
            self.last.previous_hash = temp_data


def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


# blocks
block_zero = Block(get_timestamp(), "Information X", 0)
block_one = Block(get_timestamp(), "Information Y", block_zero)
block_two = Block(get_timestamp(), "Information Z", block_one)

# Block chain
block_chain = BlockChain()
block_chain.append(get_timestamp(), "Information A")
block_chain.append(get_timestamp(), "Information B")

# tests
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Block Chain last data : ", block_chain.last.data)
print("Block Chain last's previous hash data : ", block_chain.last.previous_hash.data)



#Test case 2
# blocks
timeStamp=get_timestamp()
block_zero = Block(timeStamp, "Information X", 0)
block_one = Block(timeStamp, "Information Y", block_zero)
block_two = Block(timeStamp, "Information Z", block_one)

# Block chain
block_chain = BlockChain()
block_chain.append(timeStamp, "Information A")
block_chain.append(timeStamp, "Information B")

# tests
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block One timestamp : ", block_one.timestamp)
print("Block Two timestamp : ", block_two.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Block Chain last data : ", block_chain.last.data)
print("Block Chain last's previous hash data : ", block_chain.last.previous_hash.data)


#Test case 3

# Block chain
block_chain = BlockChain()

# tests
print("Block Chain last data : ", block_chain.last)
print("Block Chain last's previous hash data : ", block_chain.head)


