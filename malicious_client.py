# malicious_client.py
from socket import *
from blockchain import BlockChain
import pickle
import io
import hashlib

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
    print("--- MALICIOUS CLIENT ---")
    next_instruction = "send package to [hacker's address]"
    # Assuming they can monitor comms between server and client and have gathered the hash of the previous block
    previous_block = ('return to warehouse', 'cadab3c7d6213731e4be5f0a5c444083')
    next_block = (next_instruction, hashlib.md5(pickle.dumps(previous_block)).hexdigest())
    print("Sending forged instruction block:", next_block)
    print(send_instruction(next_block))