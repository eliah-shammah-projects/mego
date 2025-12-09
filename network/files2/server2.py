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
    # עוזר במקרה שהפורט נשאר בסטייט "in use" לזמן קצר אחרי סגירה
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except Exception:
        pass

    try:
        sock.bind((SERVER_IP, SERVER_PORT))
    except OSError as e:
        print("Failed to bind socket:", e)
        sock.close()
        return

    print("SERVER READY... (press Ctrl+C to stop)")

    try:
        while True:
            try:
                # ממתינים לבקשת שם הקובץ (חסום, אין timeout)
                sock.settimeout(None)
                print("Waiting for request...")
                request, client = sock.recvfrom(65536)
                if not request:
                    continue

                print("Got request from", client, "raw:", request)
                filename = request.decode().strip()
                print(f"Client requested: {filename}")

                # בדיקה אם הקובץ קיים
                path = os.path.join(FILE_DIR, filename)
                if not os.path.exists(path):
                    sock.sendto(b"NOT FOUND 404", client)
                    print("File not found, replied 404")
                    continue

                # שולחים OK ונכנסים למצב העברה עם timeout ל־ACKs
                sock.sendto(b"OK", client)
                with open(path, "rb") as f:
                    data = f.read()

                packets = [data[i:i + PACKET_SIZE] for i in range(0, len(data), PACKET_SIZE)]

                window = 1
                next_seq = 0
                base = 0
                acked = set()

                print("Starting RUDP transfer... total packets:", len(packets))

                # עכשיו ההעברה — חשוב: יש timeout כדי לאפשר retransmit
                sock.settimeout(TIMEOUT)

                while base < len(packets):
                    # שליחת כל החבילות בחלון
                    for seq in range(next_seq, min(base + window, len(packets))):
                        try:
                            sock.sendto(make_packet(seq, packets[seq]), client)
                            print(f"Sent seq={seq} window={window}")
                        except Exception as send_err:
                            print("Send error:", send_err)

                    next_seq = min(base + window, len(packets))

                    try:
                        ack_raw, _ = sock.recvfrom(65536)
                        # ודא שזה תקין לפני המרה ל־int
                        try:
                            ack = int(ack_raw.decode().strip())
                        except Exception:
                            print("Received malformed ACK:", ack_raw)
                            continue

                        print(f"ACK received: {ack}")

                        if ack not in acked:
                            acked.add(ack)
                            # קידום בסיס
                            if ack == base:
                                while base in acked:
                                    base += 1

                            # הגדלת חלון (simple AIMD-ish)
                            if window < THRESHOLD:
                                window *= 2
                            else:
                                window += 1

                    except socket.timeout:
                        # אין ACK — אפס חלון וחזור על שליחה מה־base
                        print("Timeout → window reset to 1, retransmit from base", base)
                        THRESHOLD = max(1, window // 2)
                        window = 1
                        next_seq = base
                        # המשך הלולאה ישלח שוב את מה שבחלון
                        continue
                    except Exception as ack_err:
                        print("ACK parse error:", ack_err)
                        continue

                # סיימנו להחזיר את כל החבילות
                sock.sendto(b"DONE", client)
                print("Finished sending file!")

                # ניקוי פקטות מאוחרות (flush) כדי שלא ייכנסו לבקשה הבאה
                sock.settimeout(0.01)
                while True:
                    try:
                        sock.recvfrom(65536)
                    except Exception:
                        break
                # נחזיר לבלוקינג למצב המתנה
                sock.settimeout(None)

            except Exception as e:
                print("Session ERROR:", e)
                # במקרה של שגיאה סשן מתאפס ונמשיך לקבל בקשה חדשה
                continue

    except KeyboardInterrupt:
        print("\nServer stopping (KeyboardInterrupt)")
    finally:
        sock.close()
        print("Socket closed.")

if __name__ == "__main__":
    run_server()
