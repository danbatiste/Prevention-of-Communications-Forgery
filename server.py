# server.py
from socket import *
from blockchain import BlockChain
import pickle
import io

# GLOBALS
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1234

if __name__ == "__main__":
    print("--- DRONE SERVER ---")
    # Get initial instructions to create genesis block
    with open('initial_instructions.txt', 'r') as file:
        initial_instructions = '\n'.join(file.readlines())
    
    # Initialize the blockchain using the initial instructions as genesis block data
    instruction_chain = BlockChain()
    genesis_block = instruction_chain.create_block(initial_instructions)
    print("Loaded initial instruction: ", instruction_chain.add_block(genesis_block))

    # Start server
    serverSocket.bind(('127.0.0.1', serverPort))
    serverSocket.listen(1)

    while True:
        print('Waiting for instructions...')
        connectionSocket, addr = serverSocket.accept()

        # Get the next instruction from the client
        next_block = connectionSocket.recv(1024)#Fill in start #Fill in end
        next_block = pickle.loads(next_block, encoding='bytes')
        print("Received instructions block: ", next_block)

        accepted = instruction_chain.add_block(next_block) # Attempts to add the block into the blockchain. Will it succeed?
        response = "Block is valid: " + str(accepted)
        if not accepted:
            print("Invalid block, ignoring...")
            continue
        print(instruction_chain)
        print(response)
        connectionSocket.sendall(response.encode())
        connectionSocket.close()
