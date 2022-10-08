import math
import mmh3
from bitarray import bitarray
  
  
class BloomFilter(object):
  
    '''
    Class for Bloom filter, using murmur3 hash function
    '''
  
    def __init__(self, bitarray_size, hash_count):
        '''
        bitarray_size : int
            Size of the bit array in bloom filter
        hash_count : int
            number of hash function to be used
        ''' 
        # number of hash functions to use
        self.hash_count = hash_count
  
        # Bit array of given size
        self.bit_array = bitarray(bitarray_size)

        # initialize all bits as 0
        self.bit_array.setall(0)

        # Store the bit array size
        self.size = bitarray_size

    def insert_str(self, item):
        '''
        Add a string in the filter
        '''
        digests = []
        for i in range(self.hash_count):
  
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)
  
            # set the bit True in bit_array
            self.bit_array[digest] = True
  
    def testmembership_str(self, item):
        '''
        Check for existence of a string in filter
        '''
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
  
                # if any of bit is False then,its not present
                # in filter
                # else there is probability that it exist
                return False
        return True
  
    def reset(self):
        '''
        reset the bitarray of the bloomfilter
        '''
        self.bit_array.setall(0)