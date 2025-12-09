import socket
import os
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

# Pastas de arquivos
FILE_DIR_TEXT = r"C:\Users\eliah\Documents\mego\network\files3"
FILE_DIR_VIDEO = r"C:\Users\eliah\Documents\mego\network\files3"

TIMEOUT = 0.4
THRESHOLD = 8

def make_packet(seq, data):
    return f"{seq}|".encode() + data

def run_server():
    global THRESHOLD

    # Pergunta interativa sobre perda de pacotes
    SIMULATE_LOSS = False
    LOSS_PERCENTAGE = 0
    choice = input("Simular perda de pacotes? (s/n): ").strip().lower()
    if choice == "s":
        SIMULATE_LOSS = True
        while True:
            try:
                LOSS_PERCENTAGE = int(input("Qual % de perda? (0-100): ").strip())
                if 0 <= LOSS_PERCENTAGE <= 100:
                    break
            except:
                pass
        print(f"Perda de pacotes ativada: {LOSS_PERCENTAGE}%\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_IP, SERVER_PORT))
    print(f"SERVER READY on {SERVER_IP}:{SERVER_PORT}\n")

    try:
        while True:
            # Recebe tipo de arquivo
            filetype_data, client = sock.recvfrom(1024)
            filetype = filetype_data.decode().strip()

            if filetype == "v":
                PACKET_SIZE = 8192
                file_dir = FILE_DIR_VIDEO
            elif filetype == "t":
                PACKET_SIZE = 1024
                file_dir = FILE_DIR_TEXT
            else:
                continue

            # Recebe nome do arquivo
            request, client = sock.recvfrom(65536)
            filename = request.decode().strip()

            path = os.path.join(file_dir, filename)
            if not os.path.exists(path):
                sock.sendto(b"NOT FOUND 404", client)
                continue

            sock.sendto(b"OK", client)
            with open(path, "rb") as f:
                data = f.read()

            packets = [data[i:i + PACKET_SIZE] for i in range(0, len(data), PACKET_SIZE)]
            window = 1
            base = 0
            next_seq = 0
            acked = set()

            sock.settimeout(TIMEOUT)

            while base < len(packets):
                for seq in range(next_seq, min(base + window, len(packets))):
                    # Simulação de perda
                    if SIMULATE_LOSS and random.randint(1, 100) <= LOSS_PERCENTAGE:
                        print(f"⚠️ Simulated loss of packet seq={seq}")
                        continue

                    sock.sendto(make_packet(seq, packets[seq]), client)

                next_seq = min(base + window, len(packets))

                try:
                    ack_raw, _ = sock.recvfrom(65536)
                    ack = int(ack_raw.decode())
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
                    window = 1
                    next_seq = base
                    continue

            sock.sendto(b"DONE", client)

    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        sock.close()

if __name__ == "__main__":
    run_server()
