import re
import speech_recognition as sr
import requests

ESP8266_URL = "http://[ip address of ESP8266]/control"  # Updated endpoint
MAX_FLOOR = 10  # Maximum allowed floor number
DEFAULT_NAME = "Muragharajendra"

def extract_number(sentence):
    ordinal_words = {
        "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
        "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10,
        "eleventh": 11, "twelfth": 12,
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
    }
    
    for word, num in ordinal_words.items():
        if re.search(rf'\b{word}\b', sentence, re.IGNORECASE):
            return num
    
    numbers = re.findall(r'\b\d+\b', sentence)
    if numbers:
        return int(numbers[0])
    
    return "No number found"

def send_floor_command(floor, name=DEFAULT_NAME):
    if floor < 1 or floor > MAX_FLOOR:
        print(f"[ERROR] Floor {floor} is out of range! Allowed range: 1-{MAX_FLOOR}.")
        return
    
    print(f"[INFO] Sending floor {floor} for {name} to ESP8266...")
    try:
        response = requests.get(f"{ESP8266_URL}?name={name}&floor={floor}&command=call")
        print(f"[SUCCESS] ESP8266 Response: {response.text}")
    except Exception as e:
        print("[ERROR] Failed to send floor command:", e)

def recognize_speech():
    print("[INFO] Listening for voice command (30 seconds max)...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=5)
            sentence = recognizer.recognize_google(audio)
            print(f"[INFO] Recognized: {sentence}")
            number = extract_number(sentence)
            if isinstance(number, int):
                send_floor_command(number)
            else:
                print("[ERROR] Invalid floor number.")
        except sr.UnknownValueError:
            print("[ERROR] Sorry, I couldn't understand.")
        except sr.RequestError:
            print("[ERROR] Could not request results.")
        except sr.WaitTimeoutError:
            print("[INFO] No speech detected. Terminating.")

def main():
    print("[INFO] Main function started.")
    recognize_speech()
    print("[INFO] Main function ended.")

if __name__ == "__main__":
    print("[INFO] Script started.")
    main()
    print("[INFO] Script ended.")
