# Client–Server Chat Application (Python Sockets)

A simple two-way chat system built using Python sockets, demonstrating basic client–server communication over a local network.

This project supports:
- Same-computer communication (server ↔ client on the same device)
- Two-computer communication on the same WiFi network

---

## Features
- Real-time text messaging  
- Two-way communication  
- Works on LAN without internet  
- Minimal and easy-to-understand Python code  
- Can be extended to multi-client version later  

---

## Files
| File | Description |
|------|-------------|
| `server.py` | Runs the server that listens for incoming client connections |
| `client.py` | Connects to the server and enables chat |

---

## 💻 Running on the Same Computer

1. Open **two terminals** on the same machine.
2. In the first terminal:

   ```bash
   python server.py
   ```
3. In the second terminal:

   ```bash
   python client.py
   ```
4. Chat begins.
5. To end the chat client should type 'bye'.

---
## Running on Two Computers (Same WiFi)

### 1. On the server laptop:
Run the server:

```bash
python server.py
```

The terminal will show something like:

```
Server running on 172.xx.xx.xx:12345
```

This is the server’s IPv4 address.


### 2. On the client laptop:
Open `client.py` and replace:

```python
host = socket.gethostbyname(socket.gethostname())
```

with the server’s IPv4 address, for example:

```python
host = '172.20.10.5'
```

### 3. Then run the client:

```bash
python client.py
```
### 4. Chat begins.
### 5. To end the chat client should type 'bye'.

---

## Screenshots
Server running and accepting client



Successful chat between two laptops
(Sensitive information blurred intentionally)

---

## Requirements
- Python 3.x
- No external libraries

---

## Notes

- If using different computers, ensure both devices are on same WiFi.
- Avoid using VPN during connection.
- You may need to allow Python in Windows Firewall the first time you run it.

  
