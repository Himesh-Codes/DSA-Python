"""
Hash Table: Keyset and Hash of keys give index to store value

Hash Collision:
1. Collision resolution by chaining : Linked list in each hash index
2. Open Addressing : 
    Linear Probing : h(k, i) = (h′(k) + i) mod m : If a collision occurs at h(k, 0), then h(k, 1) is checked. 
    In this way, the value of i is incremented linearly.
    Quadratic Probing : h(k, i) = (h′(k) + c1i + c2i2) mod m
    Double Hashing : h(k, i) = (h1(k) + ih2(k)) mod m: Hash is applied one more time is found value.
3. Good Hash Functions
    1. Division Method: h(k) = k mod m
    2. Multiplication Method : h(k) = ⌊m(kA mod 1)⌋
    3. Universal Hashing: Hashing on random library
    
Insertion - adds a new element 
Deletion - removes the existing elements

Complexity
--------------------
 	        Worst case	Average Case
Search	        O(1)	    O(1)
Insert	        O(1)	    O(1)
Deletion	    O(1)	    O(1)

Applications
--------------------
constant time lookup and insertion is required
cryptographic applications
indexing data is required
"""

from collections import OrderedDict
from operator import mod
from hashtype import HashTableInstanceArgs, hashTypes
DIVIDE_HASH_DIVISOR = 777
MULIPLY_HASH_VALUE = 52

class HashTableFactory():
    def __init__(self, **kwargs: HashTableInstanceArgs):
       self.__capacity = kwargs['capacity']
       self.__hashFunction: hashTypes = kwargs['hashType'] if 'hashType' in kwargs else hashTypes.simpleHash
       self.__hashTable = OrderedDict()
        
    def hashFuncion(self, value):
        if self.__hashFunction:
            if self.__hashFunction == hashTypes.simpleHash:
                return self.getHashValue(value)
            elif self.__hashFunction == hashTypes.division:
                return self.getDivideHashValue(value)
            elif self.__hashFunction == hashTypes.multiplication:
                return self.getMultiplyHashValue(value)
            else:
                return self.getHashValue(value)
                
    def getHashValue(self, value):
        # since hash on int will be same outoput we convert every input to string
        value = str(value)
        return str(hash(value))
    
    def getDivideHashValue(self, value):
        return mod(value, DIVIDE_HASH_DIVISOR)
    
    def getMultiplyHashValue(self, value):
        return MULIPLY_HASH_VALUE * int(self.getDivideHashValue(value))
    
    def addValue(self, key, data):
        index = self.hashFuncion(key)
        if len(self.__hashTable) <=  self.__capacity:
            if index not in self.__hashTable:
               self.__hashTable[index] = data
            # multiple hashing on hashed index until free index got
            else:
                index = self.hashFuncion(index)
                while(index in self.__hashTable):
                    index = self.hashFuncion(index)
                self.__hashTable[index] = data
            return index
        else:
            raise OverflowError('Capacity Exceeds')
        
    def removeItem(self, key):
        index = self.hashFuncion(key)
        self.__hashTable[index] = None
        
    def getItemByKey(self, key):
        index = self.hashFuncion(key)
        while index in self.__hashTable:
            yield self.__hashTable[index]
            index = self.hashFuncion(index)
    
# Testing 
hashFactory  = HashTableFactory(capacity=5)
print(hashFactory.addValue(12, 43))
print(hashFactory.addValue(32, 88))
print(hashFactory.addValue(32, 900))
for item in hashFactory.getItemByKey(12):
    print(item)
for item in hashFactory.getItemByKey(32):
    print(item)
    