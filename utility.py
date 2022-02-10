
from blockchain import Blockchain
from block import Block

def generate_dummy_user_data(num):
  '''
  Generates data to be used in the mining
  '''
  output = []
  for i in range(1,num+1):
    text = "Dummy Transaction " + str(i) + " created by normal USER!!!"
    output.append(text)
  return output
 

def print_blockchain(blockchain:Blockchain):
  '''
  Pretty-prints the blockchain.
  '''
  temp = []
  tail = blockchain.chain_front
  while tail and blockchain.chain:
    temp.append(tail)
    # print(tail)
    tail = tail.previous_block

  for i in range(len(temp)-1,-1,-1):
    print(temp[i])

def generate_dummy_Attacker_data(num):
  '''
  Generates attacker data to be used in mining.
  '''
  output = []
  for i in range(1,num+1):
    text = "Fake Transaction " + str(i) + " created by ATTACKER!!!"
    output.append(text)
  return output

def attack(blockchain:Blockchain, after:Block, data:list,num:int):
  '''
  Perform an attack after a certain block in the blockchain
  '''
  local_head = after
  for i in data:
    temp_block = Block(i,num)
    blockchain.inject(temp_block,local_head)
    local_head = temp_block
    num += 1 
  return num , local_head

