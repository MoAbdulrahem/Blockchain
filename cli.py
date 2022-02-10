import argparse
import tests
from blockchain import Blockchain
from block import Block
from utility import print_blockchain
from utility import attack
def main():
  try:
    parser = argparse.ArgumentParser()
    # parser.add_argument('torrent', help='path to the .torrent file')
    parser.add_argument('-l', '--level', type=int, help='Difficulty level (default 4)- Number of zeroes needed at the start of an acceptable hash.')
    parser.add_argument('-nob', '--no_of_blocks', type=int, help='Number of blocks to be mined by user')
    parser.add_argument('-a', '--attack', help='The block number to inject after.')
    parser.add_argument('-c', '--cycles', help='Number of cycles to generate blocks.')

    args = parser.parse_args()
    if not args.level:
      print("Use [python cli.py -h] to view help.")
    if args.level:
      blockchain=Blockchain(level = args.level)
    else:
      blockchain=Blockchain()

    if (args.level and args.no_of_blocks and args.attack and args.cycles):
      print('The initial chain is '+ str(args.no_of_blocks) + " blocks long.")
      print('Normal user tries to append to the longest chain.')
      print('Attacker appends after block '+ str(args.attack) + " with TRIPLE the CPU power of the normal user.")
      num = tests.generate_blockchain(blockchain, args.no_of_blocks, 0)
      # print_blockchain(blockchain)
      # print(num)
      local_head = blockchain.chain[int(args.attack)-1]
      for i in range(int(args.cycles)):
        if i%3 == 0:

          num += 1
          temp_string = "Dummy Transaction " + str(num) + " created by normal USER!!!"
          user_block = Block(temp_string,num)
          blockchain.mine(user_block)
          # print('user created a block')
          if local_head == blockchain.get_longest_chain_head():
            local_head = user_block
          

        # Attacker would have double the computation power of user
        num += 1 

        num, temp_block=tests.simulate_attack(blockchain, local_head,19,num)
        local_head = temp_block


      print_blockchain(blockchain)

    elif args.level and args.no_of_blocks:
      tests.generate_blockchain(blockchain, args.no_of_blocks, 0)
      print_blockchain(blockchain)

  except:
    print("Error, please try again")

main()