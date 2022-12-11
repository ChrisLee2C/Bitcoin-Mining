from hashlib import sha256
import time
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number)+transactions+previous_hash+str(nonce)
        new_hash = SHA256(text)
        #Finish guess with number of zeros first to mine a bitcoin
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined Bitcoins with nonce value: {nonce}")
            return new_hash
    raise BaseException(f"Couldn't find a Bitcoin after trying {MAX_NONCE} times")

if __name__ == '__main__':
    transactions = """
    A->B->1,
    B->C->0.5 
    """
    difficulty = 6
    start = time.time()
    print("Start Mining")
    new_hash = mine(1,transactions,"8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4",difficulty)
    total_time = str(time.time()-start)
    print("End Mining")
    print(f"Took {total_time} seconds to mine a bitcoin")
    print(new_hash)
