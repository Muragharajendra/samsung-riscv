import cv2
import face_recognition
import requests
#import speech_recognition as sr
import pickle
# print("[INFO] Script started...")


ESP8266_URL = "http://[ip address of ESP8266]/control"                    #NOTE:IP ADDRESS
# print(f"[INFO] Trying to connect to ESP8266 at {ESP8266_URL}...")

MAX_FLOOR = 10  # Maximum allowed floor number

def load_known_faces():
    print("[INFO] Loading known faces...")
    try:
        with open("faces.pkl", "rb") as f:
            data = pickle.load(f)
            print(f"[INFO] {len(data)} known faces loaded.")
            return data
    except FileNotFoundError:
        print("[WARNING] faces.pkl file not found. No registered users yet.")
        return {}

def save_known_faces(data):
    print("[INFO] Saving known faces...")
    with open("faces.pkl", "wb") as f:
        pickle.dump(data, f)
    print("[INFO] Faces saved successfully.")

def register_user(name, floor):
    if floor < 1 or floor > MAX_FLOOR:
        print(f"[ERROR] Invalid floor number! Floor must be between 1 and {MAX_FLOOR}.")
        return

    print(f"[INFO] Registering user: {name}, Floor: {floor}")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Camera not working.")
            break

        cv2.imshow("Registering... Press 's' to save", frame)
        key = cv2.waitKey(1)
        
        if key == ord('s'):
            print("[INFO] Capturing face encoding...")
            face_encodings = face_recognition.face_encodings(frame)
            if face_encodings:
                known_faces = load_known_faces()
                known_faces[name] = {'encoding': face_encodings[0], 'floor': floor}
                save_known_faces(known_faces)
                print(f"[SUCCESS] {name} registered successfully!")
                break
            else:
                print("[ERROR] No face detected. Try again.")
    
    cap.release()
    cv2.destroyAllWindows()

def send_floor_command(name, floor):
    if floor < 1 or floor > MAX_FLOOR:
        print(f"[ERROR] Floor {floor} is out of range! Allowed range: 1-{MAX_FLOOR}.")
        return

    print(f"[INFO] Sending floor {floor} for {name} to ESP8266...")
    try:
        response = requests.get(f"{ESP8266_URL}?name={name}&floor={floor}&command=call")
        print(f"[SUCCESS] ESP8266 Response: {response.text}")
    except Exception as e:
        print("[ERROR] Failed to send floor command:", e)

def send_info_to_esp(name, floor):
    if floor < 1 or floor > MAX_FLOOR:
        print(f"[ERROR] Floor {floor} is out of range! Allowed range: 1-{MAX_FLOOR}.")
        return

    print(f"[INFO] Sending floor {floor} for {name} to ESP8266...")
    try:
        response = requests.get(f"{ESP8266_URL}?name={name}&floor={floor}&command=call")
        if response.status_code == 200:
            print(f"[SUCCESS] ESP8266 Response: {response.text}")
        else:
            print(f"[ERROR] ESP8266 Response: {response.status_code} - {response.text}")
    except Exception as e:
        print("[ERROR] Failed to send floor command:", e)

def recognize_user():
    print("[INFO] Starting face recognition...")
    known_faces = load_known_faces()
    if not known_faces:
        print("[ERROR] No registered users found!")
        return
    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Camera not working.")
            break
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for encoding in face_encodings:
            for name, data in known_faces.items():
                match = face_recognition.compare_faces([data['encoding']], encoding, tolerance=0.5)
                if match[0]:
                    floor = data['floor']
                    send_floor_command(name, floor)
                    cap.release()
                    cv2.destroyAllWindows()
                    return
        
        cv2.imshow("Recognizing... Press 'q' to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


def main():
    print("[INFO] Main function started.")
    # Uncomment one of the following lines to test the functionality:
    register_user("Muragharajendra", 8)
    recognize_user()
    recognize_speech()
    send_info_to_esp("Muragharajendra", 8)
    print("[INFO] Main function ended.")

if __name__ == "__main__":
    print("[INFO] Script started.")
    main()
    print("[INFO] Script ended.")
