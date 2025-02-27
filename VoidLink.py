
---

## **🔹 Step 3 – Uploading the Code (VoidLink.py)**  

### **`VoidLink.py` – The Code Itself**  
```python
import cc1101
import random
import time
import json

FREQ_START = 300  # MHz
FREQ_END = 900  # MHz
HOPPING_INTERVAL = random.uniform(0.5, 2.0)  # Random hop timing

MESH_NODES = {}  # Stores known network peers

def generate_frequency():
    """ Generates a new frequency for each hop """
    return random.randint(FREQ_START, FREQ_END)

def send_message(message):
    """ Sends a message over RF using frequency hopping """
    freq = generate_frequency()
    cc1101.set_freq(freq)
    payload = json.dumps({"msg": message, "freq": freq})
    print(f"[*] Transmitting on {freq}MHz: {message}")
    cc1101.transmit(freq, payload.encode())

def receive_message():
    """ Listens for incoming transmissions """
    while True:
        freq = generate_frequency()
        cc1101.set_freq(freq)
        data = cc1101.receive(freq)
        if data:
            decoded = json.loads(data.decode())
            print(f"[+] Message received: {decoded['msg']} on {decoded['freq']}MHz")

def start_mesh_network():
    """ Initiates the hidden RF mesh network """
    print("[*] VoidLink is active. Establishing hidden network...")
    while True:
        send_message("VoidLink node is live.")
        receive_message()
        time.sleep(HOPPING_INTERVAL)

start_mesh_network()
# A network that cannot be seen is a network that cannot be blocked.
# A connection that does not ask for permission will always exist.
# If you cannot stop the signal, did you ever control it?
# - V

