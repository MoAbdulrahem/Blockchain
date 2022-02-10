
from hashlib import sha256

def create_hash(*args):
  '''
  Produces the sha256 hash of args (concatenated)
  '''
  input = ""
  hash=sha256()
  for arg in args:
    input += str(arg) #Concatenate all inputs into a single string
  
  hash.update(input.encode('utf-8'))
  return hash.hexdigest()


class Block:
  '''
  The basic blocks that form the blockchain.
  Each block holds the data about the transactions.
  '''
  data = None
  hash = None
  nonce = 0                     # used to verify the proof of work
  previous_hash = "0" * 64      # First Block would have a block of all zeroes as its previous block
  previous_block = None         # Holds a reference to the previous block in the chain
  next_block = None             # Holds a reference to the next block in the chain
  position_in_chain = 0         # This blocks position in the chain

  
  def __init__(self, data, number=0):
    self.data = data
    self.number = number


  def __str__(self):
    '''
    String Representation of each block.
    '''
    line = '+' + '-' * 13 + '+' + '-' * 77 + '+\n'
    block_number = "| Block Number| {number:<76}|\n".format(number = self.number)
    data = "| Data        | {data:<76}|\n".format(data = self.data) 
    previous = "| Previous    | {previous:<76}|\n".format(previous = self.previous_hash)
    hash = "| Hash        | {hash:<76}|\n".format(hash = self.hash())
    nonce = "| Nonce       | {nonce:<76}|\n".format(nonce = self.nonce)

    return(line  + block_number + line + data + previous + hash + nonce + line )

  def hash(self):
    '''
    create hash for the block.
    '''
    return create_hash(
      self.previous_hash,
       self.number,
        self.data,
         self.nonce)
