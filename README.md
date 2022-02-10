# Blockchain
A blockchain implementation in python.
# Usage
```bash
python cli.py [-h] [--level] [--attack] [--cycles]
```
`-h` Show help.
`--level`  or `-l`  Difficulty level.
`--no_of_blocks` or `-noc` Number of initial blocks in the chain before the attack started.
`--attack` or `-a`  The block to start the attack after.
`--cycles` or `-c`  Number of cycles to perform the attack for.

### Example
```bash
python cli.py --level 3 --no_of_blocks 6 --attack 2 --cycles 200
```
