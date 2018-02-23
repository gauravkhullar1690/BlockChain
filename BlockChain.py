# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:06:39 2018

@author: Gaurav.khullar
"""
import hashlib
import json

class Block:
    
    def __init__(self, index,timestamp,data,previousHash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()
    
    def calculateHash(self):
        hash = hashlib.new('sha256')
        msg = str(self.index) + self.timestamp + json.dumps(self.data) + self.previousHash
        hash.update(msg.encode('utf-8'))        
        return hash.hexdigest()
    
    
class BlockChain:
    
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
    
    def createGenesisBlock(self):
        return Block(0,"01/01/2018","Genesis Block","0000")
    
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
    def addBlock(self,newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
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
        

print("Initialzing GauravCoin.......")
gauravCoin = BlockChain()
print("Created Genesis Block")
print("Adding Block 1")
gauravCoin.addBlock(Block(1,"10/01/2018",{'amount' : 4 }))
print("Adding Block 2")
gauravCoin.addBlock(Block(2,"13/01/2018",{'amount' : 8 }))

print("Is chain Valid " + str(gauravCoin.isChainValid()))
gauravCoin.chain[1].data = {'amount' : 16}
gauravCoin.chain[1].hash = gauravCoin.chain[1].calculateHash()
gauravCoin.chain[2].previousHash = gauravCoin.chain[1].calculateHash()
gauravCoin.chain[2].hash = gauravCoin.chain[2].calculateHash()
print("Is chain Valid " + str(gauravCoin.isChainValid()))




coinList= []
for coin in gauravCoin.chain:
    coinList.append(coin.__dict__)
   
jsondata=json.dumps(coinList,sort_keys=False, indent=2)
print ("chain: " + jsondata)
    
    