# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:06:39 2018

@author: Gaurav.khullar
"""
import hashlib
from datetime import datetime

class Transaction:
    
    def __init__(self,fromAddress,toAddress,amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount


class Block:
    
    def __init__(self,timestamp,transactions,previousHash=''):   
        self.nounce = 0 
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.hash = self.calculateHash()
               
    
    def calculateHash(self):
        hash = hashlib.new('sha256')
        msg = str(self.nounce) + str(self.timestamp) + str(self.transactions) + self.previousHash
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
        self.difficulty = 4
        self.pendingTransactions = []
        self.miningReward = 100
        
    
    def createGenesisBlock(self):
        return Block("01/01/2018","Genesis Block","0000")
    
    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
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
gauravCoin.createTransaction(Transaction("address1","address2",100))
gauravCoin.createTransaction(Transaction("address2","address3",50))

gauravCoin.minPendingTransactions("gaurav")

gauravCoin.createTransaction(Transaction("address1","address2",100))
gauravCoin.createTransaction(Transaction("address2","address3",50))
gauravCoin.minPendingTransactions("gaurav")

gauravCoin.createTransaction(Transaction("gaurav","address4",50))
gauravCoin.minPendingTransactions("address4")

print(gauravCoin.getBalanceOfAddress("gaurav"))


    