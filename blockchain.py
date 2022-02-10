
from block import Block


class Blockchain:
  '''
  A list of Block objects that represents the blockchain.
  '''
  length = 0

  def __init__(self, chain:list=[],level:int=4):
    self.chain = chain
    self.chain_front = None
    self.chain_root = None
    self.level = level # The number of zeroes at the start of an accepted block


  def add(self, block:Block):
    '''
    Appends a new block to the blockchain
    '''
    if self.chain == []: # first item in the chain
      self.chain_front = block
      self.chain_root = block
      block.position_in_chain = 1
      self.chain.append(block)

    else:
      longest_chain = self.get_longest_chain_head()
      block.previous_block = longest_chain
      longest_chain.next_block = block
      self.chain_front = block
      block.position_in_chain = self.length + 1
      self.chain.append(block)
    
    self.length += 1

  def remove(self,block):
    '''
    Removes a block from the blockchain.
    '''
    self.chain.remove(block)
    
  def mine(self, block:Block):
    '''
    Attempt to generate the next block in the chain.
    '''
    try:
      # Set the previous_hash of the block to the last block in the chain
      # This could raise an IndexError if the chain is an empty list
      block.previous_hash = self.chain_front.hash()
    except:
      pass

    while True: # generate hashes until we get the right hash

      if block.hash()[:self.level] == '0' * self.level: # A valid block
        self.add(block)
        break
      else: # increase the nonce and try again
        block.nonce += 1

  def is_valid(self):
    '''
    Checks whether the blockchain is still valid or got somehow corrupted.
    The chain is valid if:
      1. The first N bits = 0 (depending on the difficulty level) 
      2. The previous hash of each block matches the hash of the previous block.
    '''
    for index in range(1,len(self.chain)):

      _previous = self.chain[index].previous_hash
      _current = self.chain[index-1].hash() # We recalculate the hash to make sure that none of the parameters
      # that it depends on has changed

      if _current[:self.level] != '0' * self.level or _previous != _current:
        return False
    return True

  def get_longest_chain_head(self):
    '''
    Returns the last block in the longest chain.
    '''
    try:
      if self.chain != []:
        head = self.chain_root
        for block in self.chain:
          if block.position_in_chain > head.position_in_chain:
            head = block
      return head
    except:
      return None    

  def inject(self, block: Block, index_block:Block):
    '''
    Simulates an attack where the attacker tries to inject blocks in the middle of the chain
    and grow their branch as fast as possible.
    '''
    block.previous_hash = index_block.hash()
    while True:
      if block.hash()[:self.level] == '0' * self.level: # A valid block
        
        block.previous_block = index_block
        block.position_in_chain = index_block.position_in_chain + 1
        
        self.chain.append(block)
        if block.position_in_chain >= self.length:
          self.chain_front = block
        # print(block.hash())
        
        break
      else: # increase the nonce and try again
        block.nonce += 1


