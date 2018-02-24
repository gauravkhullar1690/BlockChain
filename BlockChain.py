# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:06:39 2018

@author: Gaurav.khullar
"""
import hashlib
import json

class Block:
    
    def __init__(self, index,timestamp,data,previousHash=''):   
        self.nounce = 0 
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()
               
    
    def calculateHash(self):
        hash = hashlib.new('sha256')
        msg = str(self.nounce) + str(self.index) + self.timestamp + json.dumps(self.data) + self.previousHash
        hash.update(msg.encode('utf-8'))        
        return hash.hexdigest()
    
    def mineBlock(self,difficulty):
        prefix = "0"
        for i in range(1,difficulty):
            prefix = prefix + "0"
        while self.hash[:difficulty] != prefix:
            self.nounce +=  1
            self.hash = self.calculateHash()
        print("Block mined : " + self.hash)
            
    
    
class BlockChain:
    
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 5
    
    def createGenesisBlock(self):
        return Block(0,"01/01/2018","Genesis Block","0000")
    
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
    def addBlock(self,newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
        
    def isChainValid(self):
        for i in range(1,len(self.chain)):            
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            
            if(currentBlock.hash != currentBlock.calculateHash()):
                return False
            if(currentBlock.previousHash != previousBlock.hash):
                return False
        return True
        


gauravCoin = BlockChain()
print("Mining block 1")
gauravCoin.addBlock(Block(1,"10/01/2018",{'amount' : 4 }))
print("Mining block 2")
gauravCoin.addBlock(Block(2,"13/01/2018",{'amount' : 8 }))




coinList= []
for coin in gauravCoin.chain:
    coinList.append(coin.__dict__)
   
jsondata=json.dumps(coinList,sort_keys=False, indent=2)
#print ("chain: " + jsondata)
    
    