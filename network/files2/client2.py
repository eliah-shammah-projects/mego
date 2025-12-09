import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234
PACKET_SIZE = 8192
RECV_TIMEOUT = 10.0  # כמה זמן לחכות לפני שניחש שבסיס ההעברה הסתיים בטעות

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        filename = input("Enter filename: ").strip()
        if not filename:
            print("No filename given.")
            return

        sock.sendto(filename.encode(), (SERVER_IP, SERVER_PORT))

        # נחכה לתשובת השרת (OK / NOT FOUND)
        sock.settimeout(5.0)
        try:
            response, _ = sock.recvfrom(65536)
        except socket.timeout:
            print("No response from server (timeout).")
            return

        if response == b"NOT FOUND 404":
            print("File not found (404)")
            return
        else:
            print("Server accepted file request")

        received = {}
        sock.settimeout(RECV_TIMEOUT)

        while True:
            try:
                packet, server = sock.recvfrom(65536)
            except socket.timeout:
                print("Receiving timeout — no data from server. Aborting.")
                return

            if packet == b"DONE":
                print("Received DONE from server")
                break

            # ודא שהחבילה תקינה לפני split
            if b"|" not in packet:
                print("Malformed packet (no header):", packet[:50])
                continue

            try:
                header, data = packet.split(b"|", 1)
                seq = int(header.decode().strip())
            except Exception as e:
                print("Failed to parse packet header:", e)
                continue

            print(f"Got packet seq={seq}, {len(data)} bytes")
            # אחסן
            if seq not in received:
                received[seq] = data
            else:
                print("Duplicate packet", seq)

            # שליחת ACK
            try:
                sock.sendto(str(seq).encode(), server)
            except Exception as e:
                print("Failed to send ACK:", e)

        # הרכב רצף נכון
        output = b""
        i = 0
        while i in received:
            output += received[i]
            i += 1

        out_name = "received_" + filename
        with open(out_name, "wb") as f:
            f.write(output)

        print(f"File saved as: {out_name}")

        # פתח אוטומטית את הקובץ ב־Windows
        try:
            os.startfile(out_name)
            print("Opening file automatically...")
        except Exception as err:
            print("Could not open automatically:", err)

    finally:
        sock.close()

if __name__ == "__main__":
    run_client()
