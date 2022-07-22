# client.py
from socket import *
from blockchain import BlockChain
import pickle
import io

# GLOBALS
clientSocket = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 1234
clientSocket.connect((host, port))

# Send an instruction block to the server
def send_instruction(instruction_block):
    requestSend = pickle.dumps(instruction_block)
    clientSocket.send(requestSend)

    output = ''
    while 1:
        data = clientSocket.recv(1024)
        if not data: break
        output += data.decode()
    return output

if __name__ == "__main__":
    print("--- DRONE CONTROLLER CLIENT ---")
    with open('initial_instructions.txt', 'r') as file:
        initial_instructions = '\n'.join(file.readlines())
    
    instruction_chain = BlockChain()
    genesis_block = instruction_chain.create_block(initial_instructions)
    print("Loaded initial instruction: ", instruction_chain.add_block(genesis_block))

    next_instruction = "return to warehouse"
    next_block = instruction_chain.create_block(next_instruction)
    print("Creating block for instruction: " + next_instruction)
    print("Sending instruction block: " + next_block.__repr__())
    print(send_instruction(next_block))