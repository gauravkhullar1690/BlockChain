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
<<<<<<< HEAD
        self.difficulty = 4
        self.pendingTransactions = []
        self.miningReward = 100
        
=======
        self.difficulty = 5
>>>>>>> parent of f6e1caf... Adding mining reward
    
    def createGenesisBlock(self):
        return Block(0,"01/01/2018","Genesis Block","0000")
    
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
<<<<<<< HEAD
    def minPendingTransactions(self,miningRewardAddress):
        block = Block(str(datetime.now()),self.pendingTransactions)
        block.mineBlock(self.difficulty)
        
        print("Block mined successfully!")
        self.chain.append(block)
        
        self.pendingTransactions = [
                Transaction(None,miningRewardAddress,self.miningReward)
                ]
    
    def createTransaction(self,transaction):
        self.pendingTransactions.append(transaction)
        
    def getBalanceOfAddress(self,address):
        balance = 0
        for block in self.chain[1:]:
            for transaction in block.transactions:
                if transaction.fromAddress == address:
                    balance -=  transaction.amount
                elif transaction.toAddress == address:
                    balance +=  transaction.amount                
        return balance
=======
    def addBlock(self,newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)
>>>>>>> parent of f6e1caf... Adding mining reward
        
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


<<<<<<< HEAD
gauravCoin.createTransaction(Transaction("gaurav","address4",50))
gauravCoin.minPendingTransactions("address4")

print(gauravCoin.getBalanceOfAddress("gaurav"))
=======
>>>>>>> parent of f6e1caf... Adding mining reward


coinList= []
for coin in gauravCoin.chain:
    coinList.append(coin.__dict__)
   
jsondata=json.dumps(coinList,sort_keys=False, indent=2)
#print ("chain: " + jsondata)
    
    