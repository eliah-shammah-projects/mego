import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234
RECV_TIMEOUT = 10.0

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        choice = input("Select file type: (t)ext or (v)ideo: ").strip().lower()
        if choice not in ["t", "v"]:
            print("Invalid choice")
            return
        sock.sendto(choice.encode(), (SERVER_IP, SERVER_PORT))

        filename = input("Enter filename: ").strip()
        sock.sendto(filename.encode(), (SERVER_IP, SERVER_PORT))

        sock.settimeout(5.0)
        try:
            response, _ = sock.recvfrom(65536)
        except socket.timeout:
            print("No response from server")
            return

        if response == b"NOT FOUND 404":
            print("File not found")
            return
        else:
            print("Server accepted file request")

        received = {}
        sock.settimeout(RECV_TIMEOUT)

        while True:
            try:
                packet, server = sock.recvfrom(65536)
            except socket.timeout:
                print("Receiving timeout")
                break

            if packet == b"DONE":
                break

            if b"|" not in packet:
                continue

            header, data = packet.split(b"|", 1)
            try:
                seq = int(header.decode())
            except:
                continue

            # Mostra pacote novo ou retransmissão
            if seq in received:
                print(f"🔄 Retransmission received seq={seq}")
            else:
                print(f"📦 Got packet seq={seq}")

            received[seq] = data
            sock.sendto(str(seq).encode(), server)

        output = b""
        i = 0
        while i in received:
            output += received[i]
            i += 1

        out_name = "received_" + filename
        with open(out_name, "wb") as f:
            f.write(output)

        print(f"File saved as: {out_name}")

        if choice == "v":
            try:
                os.startfile(out_name)
                print("Opening video...")
            except:
                print("Could not open video automatically.")
        else:
            print("Text file received.")

    finally:
        sock.close()

if __name__ == "__main__":
    run_client()
