import socket
import os  # 🔹 Para abrir vídeos automaticamente

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)  # 🔹 Timeout para pacotes que somem

    choice = input("Video (v) or Text (t)? ").strip().lower()
    if choice not in ("v", "t"):
        print("Invalid option")
        return

    sock.sendto(choice.encode(), (SERVER_IP, SERVER_PORT))

    PACKET_SIZE = int(sock.recvfrom(1024)[0].decode())
    print(f"Using packet size: {PACKET_SIZE}")

    filename = input("Enter filename: ")
    sock.sendto(filename.encode(), (SERVER_IP, SERVER_PORT))

    response, _ = sock.recvfrom(65536)
    if response == b"NOT FOUND 404":
        print("File not found.")
        return

    print("Server accepted file request")

    received = {}

    while True:
        try:
            packet, server = sock.recvfrom(65536)
        except socket.timeout:
            print("Timeout waiting for packet, retrying...")
            continue

        if packet == b"DONE":
            break

        header, data = packet.split(b"|", 1)
        seq = int(header.decode())

        print(f"Got packet seq={seq}")
        received[seq] = data

        sock.sendto(str(seq).encode(), server)  # ACK

    # Reconstrói arquivo
    output = b""
    i = 0
    while i in received:
        output += received[i]
        i += 1

    out_name = "received_" + filename
    with open(out_name, "wb") as f:
        f.write(output)

    print(f"Saved file as: {out_name}")

    # 🔹 Abrir vídeo automaticamente
    if choice == "v":
        print("Opening video...")
        os.startfile(out_name)

if __name__ == "__main__":
    run_client()
