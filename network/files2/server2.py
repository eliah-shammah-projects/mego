import socket
import os
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234
FILE_DIR = r"C:\Users\eliah\Documents\mego\network\files2"

PACKET_SIZE = 8192
TIMEOUT = 0.4
THRESHOLD = 8

def make_packet(seq, data):
    return f"{seq}|".encode() + data

def run_server():
    global THRESHOLD
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))
    sock.settimeout(None)
    #היה בשורה למעלה :
    #sock.settimeout(TIMEOUT)


    print("SERVER READY...")

    while True:
        try:
            print("Waiting for request...")
            request, client = sock.recvfrom(65536)
            print("Got request:", request)
            filename = request.decode().strip()
            print(f"Client requested: {filename}")

            # בדיקה אם הקובץ קיים
            path = os.path.join(FILE_DIR, filename)
            if not os.path.exists(path):
                sock.sendto(b"NOT FOUND 404", client)
                continue

            sock.sendto(b"OK", client)

            with open(path, "rb") as f:
                data = f.read()

            packets = [
                data[i:i + PACKET_SIZE]
                for i in range(0, len(data), PACKET_SIZE)
            ]

            window = 1
            next_seq = 0
            base = 0

            print("Starting RUDP transfer...")

            acked = set()

            while base < len(packets):
                for seq in range(next_seq, min(base + window, len(packets))):
                    print(f"Sending seq {seq} window={window}")
                    sock.sendto(make_packet(seq, packets[seq]), client)
                next_seq = min(base + window, len(packets))

                try:
                    ack_raw, _ = sock.recvfrom(65536)
                    ack = int(ack_raw.decode())
                    print(f"ACK received: {ack}")

                    if ack not in acked:
                        acked.add(ack)

                        if ack == base:
                            while base in acked:
                                base += 1

                        if window < THRESHOLD:
                            window *= 2
                        else:
                            window += 1

                except socket.timeout:
                    print("TIMEOUT → window reset to 1")
                    THRESHOLD = max(1, window // 2)
                    window = 1
                    next_seq = base

            sock.sendto(b"DONE", client)
            print("Finished sending file!")

        except Exception as e:
            print("ERROR:", e)

if __name__ == "__main__":
    run_server()