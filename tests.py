from email import header
from blockchain import Blockchain
from block import Block
from utility import attack, generate_dummy_Attacker_data, generate_dummy_user_data, print_blockchain

#--------------------------------------------------------------------------#        
#----------------------Generate Normal Blockchain--------------------------#        
#--------------------------------------------------------------------------#        
def generate_blockchain(blockchain:Blockchain, number_of_blocks:int=10, num:int=0):
  dummy_data = generate_dummy_user_data(number_of_blocks)
  for data in dummy_data:
    num += 1
    blockchain.mine(Block(data,num))
  return num

  

#--------------------------------------------------------------------------#        
#--------------------------Simulate An Attack------------------------------#        
#--------------------------------------------------------------------------#        
def simulate_attack(blockchain:Blockchain, inject_after:Block, number_of_blocks:int=5, number:int=0):
  dummy_data = ["Fake Transaction " + str(number) + " created by ATTACKER!!!"]
  _, block = attack(blockchain, inject_after, dummy_data, number)
  return number , block

if __name__ == '__main__':
 
  blockchain = Blockchain(level=3)
  num = generate_blockchain(blockchain,3)
  num, local_head=simulate_attack(blockchain, blockchain.chain[0],19,num+1)
  # generate_blockchain(blockchain,1,num)
  num, local_head=simulate_attack(blockchain, local_head,19,num+1)
  num, local_head=simulate_attack(blockchain, local_head,19,num+1)
  temp = Block("TEST", num+1)
  blockchain.mine(temp)
  local_head = temp
  num, local_head=simulate_attack(blockchain, local_head,19,num+1)


  print_blockchain(blockchain)
  