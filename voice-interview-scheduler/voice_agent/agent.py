# from adapt.engine import IntentDeterminationEngine
# from adapt.intent import IntentBuilder
# import queue
# import sounddevice as sd
# import json
# import vosk

# # Load Vosk model (download from https://alphacephei.com/vosk/models)
# model = vosk.Model("models/vosk-model-small-en-us-0.15")
# q = queue.Queue()

# def callback(indata, frames, time, status):
#     q.put(bytes(indata))

# # Setup Adapt Intent Engine
# engine = IntentDeterminationEngine()

# # Register Intents
# engine.register_intent_parser(
#     IntentBuilder("InterestedIntent").require("interested").build()
# )
# engine.register_intent_parser(
#     IntentBuilder("NoticePeriodIntent").require("notice").require("period").build()
# )
# engine.register_intent_parser(
#     IntentBuilder("CTCIntent").require("ctc").require("amount").build()
# )
# engine.register_intent_parser(
#     IntentBuilder("AvailabilityIntent").require("available").require("day").build()
# )

# # Define keywords
# keywords = {
#     "interested": ["yes", "interested", "sure"],
#     "notice": ["notice", "serving"],
#     "period": ["weeks", "months", "days"],
#     "ctc": ["ctc", "salary", "package"],
#     "amount": ["lpa", "lakhs", "k", "crore"],
#     "available": ["available", "free", "can attend"],
#     "day": ["monday", "tuesday", "wednesday", "thursday", "friday"]
# }

# # Register keywords
# for key, values in keywords.items():
#     for value in values:
#         engine.register_entity(value, key)

# # def listen_and_parse():
# #     print("🎤 Listening... (speak clearly)")
# #     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
# #                            channels=1, callback=callback):
# #         rec = vosk.KaldiRecognizer(model, 16000)
# #         while True:
# #             data = q.get()
# #             if rec.AcceptWaveform(data):
# #                 text = json.loads(rec.Result())["text"]
# #                 print(f"🗣 You said: {text}")
# #                 for intent in engine.determine_intent(text):
# #                     if intent["confidence"] > 0:
# #                         print(f"✅ Intent: {intent['intent_type']}")
# #                         print(f"📦 Full: {intent}")
# #                         return intent
# #                 print("⚠️ Sorry, I didn't understand. Try again.")

# # def listen_and_parse(expected_intents):
# #     print("🎤 Listening... (speak clearly)")
# #     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
# #                            channels=1, callback=callback):
# #         rec = vosk.KaldiRecognizer(model, 16000)
# #         while True:
# #             data = q.get()
# #             if rec.AcceptWaveform(data):
# #                 text = json.loads(rec.Result())["text"]
# #                 print(f"🗣 You said: {text}")
# #                 for intent in engine.determine_intent(text):
# #                     if intent["confidence"] > 0 and intent["intent_type"] in expected_intents:
# #                         print(f"✅ Intent: {intent['intent_type']}")
# #                         print(f"📦 Full: {intent}")
# #                         return intent
# #                 print("⚠️ Sorry, I didn't understand. Try again.")

# def listen_and_parse(expected_intents):
#     rec = vosk.KaldiRecognizer(model, 16000)

#     while True:
#         data = q.get()
#         if rec.AcceptWaveform(data):
#             text = json.loads(rec.Result())["text"]
#             print(f"🗣 You said: {text}")
#             for intent in engine.determine_intent(text):
#                 if intent["confidence"] > 0 and intent["intent_type"] in expected_intents:
#                     print(f"✅ Intent: {intent['intent_type']}")
#                     print(f"📦 Full: {intent}")
#                     return intent
#             print("⚠️ Sorry, I didn't understand. Try again.")
# if __name__ == "__main__":
#     print("👋 Hello! This is HR bot calling for your job interview.")

#     # Open stream only once
#     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
#                            channels=1, callback=callback):
#         print("\n👂 Are you interested in the job?")
#         listen_and_parse(["InterestedIntent"])

#         print("\n📅 What is your notice period?")
#         listen_and_parse(["NoticePeriodIntent"])

#         print("\n💰 What is your current and expected CTC?")
#         listen_and_parse(["CTCIntent"])

#         print("\n📆 When are you available for interview next week?")
#         listen_and_parse(["AvailabilityIntent"])

#     print("\n✅ Thank you! We'll confirm your interview schedule shortly.")









# # if __name__ == "__main__":
# #     print("👋 Hello! This is HR bot calling for your job interview.")
    
# #     print("\n👂 Are you interested in the job?")
# #     listen_and_parse()

# #     print("\n📅 What is your notice period?")
# #     listen_and_parse()

# #     print("\n💰 What is your current and expected CTC?")
# #     listen_and_parse()

# #     print("\n📆 When are you available for interview next week?")
# #     listen_and_parse()

# #     print("\n✅ Thank you! We'll confirm your interview schedule shortly.")

# # if __name__ == "__main__":
# #     print("👋 Hello! This is HR bot calling for your job interview.")
    
# #     print("\n👂 Are you interested in the job?")
# #     listen_and_parse(["InterestedIntent"])

# #     print("\n📅 What is your notice period?")
# #     listen_and_parse(["NoticePeriodIntent"])

# #     print("\n💰 What is your current and expected CTC?")
# #     listen_and_parse(["CTCIntent"])

# #     print("\n📆 When are you available for interview next week?")
# #     listen_and_parse(["AvailabilityIntent"])

# #     print("\n✅ Thank you! We'll confirm your interview schedule shortly.")



# from adapt.engine import IntentDeterminationEngine
# from adapt.intent import IntentBuilder
# import queue
# import sounddevice as sd
# import json
# import vosk
# import time

# # Initialize model and audio queue
# model = vosk.Model("models/vosk-model-small-en-us-0.15")
# q = queue.Queue()

# # Callback to fill queue
# def callback(indata, frames, time, status):
#     q.put(bytes(indata))

# # Setup Adapt Intent Engine
# engine = IntentDeterminationEngine()

# # Register Intents
# engine.register_intent_parser(
#     IntentBuilder("InterestedIntent").require("interested").build()
# )
# engine.register_intent_parser(
#     IntentBuilder("NoticePeriodIntent").require("notice").require("period").build()
# )
# engine.register_intent_parser(
#     IntentBuilder("CTCIntent").require("ctc").require("amount").build()
# )
# engine.register_intent_parser(
#     IntentBuilder("AvailabilityIntent").require("available").require("day").build()
# )

# # Define and register keywords
# keywords = {
#     "interested": ["yes", "interested", "sure"],
#     "notice": ["notice", "serving"],
#     "period": ["weeks", "months", "days"],
#     "ctc": ["ctc", "salary", "package"],
#     "amount": ["lpa", "lakhs", "k", "crore"],
#     "available": ["available", "free", "can attend"],
#     "day": ["monday", "tuesday", "wednesday", "thursday", "friday"]
# }
# for key, values in keywords.items():
#     for value in values:
#         engine.register_entity(value, key)

# # Use a shared recognizer instance
# recognizer = vosk.KaldiRecognizer(model, 16000)

# Unified listen method
# def listen_for_intent(expected_intents):
#     print("🎤 Listening for intent:", expected_intents)
#     while True:
#         data = q.get()
#         if recognizer.AcceptWaveform(data):
#             result = json.loads(recognizer.Result())
#             text = result.get("text", "")
#             print(f"🗣 You said: {text}")
#             for intent in engine.determine_intent(text):
#                 if intent["confidence"] > 0 and intent["intent_type"] in expected_intents:
#                     print(f"✅ Intent Detected: {intent['intent_type']}")
#                     return intent
#             print("⚠️ Could not determine intent, please try again.")

# def listen_for_intent(expected_intents, timeout=20):
#     print("🎤 Listening for intent:", expected_intents)
#     recognizer = vosk.KaldiRecognizer(model, 16000)  # Re-create for each listen
#     start_time = time.time()
#     while True:
#         try:
#             data = q.get(timeout=timeout)
#         except Exception:
#             print("⚠️ No speech detected (timeout).")
#             return None
#         if recognizer.AcceptWaveform(data):
#             result = json.loads(recognizer.Result())
#             text = result.get("text", "")
#             print(f"🗣 You said: {text}")
#             for intent in engine.determine_intent(text):
#                 if intent["confidence"] > 0 and intent["intent_type"] in expected_intents:
#                     print(f"✅ Intent Detected: {intent['intent_type']}")
#                     return intent
#             print("⚠️ Could not determine intent, please try again.")
#         if time.time() - start_time > timeout:
#             print("⚠️ Listening timed out.")
#             return None

# def clear_queue(q):
#     while not q.empty():
#         try:
#             q.get_nowait()
#         except Exception:
#             break
# Main interaction flow
# def main():
#     print("👋 Hello! This is HR bot calling for your job interview.")

#     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
#                            channels=1, callback=callback):
#         print("\n👂 Are you interested in the job?")
#         listen_for_intent(["InterestedIntent"])

#         print("\n📅 What is your notice period?")
#         listen_for_intent(["NoticePeriodIntent"])

#         print("\n💰 What is your current and expected CTC?")
#         listen_for_intent(["CTCIntent"])

#         print("\n📆 When are you available for interview next week?")
#         listen_for_intent(["AvailabilityIntent"])

#     print("\n✅ Thank you! We'll confirm your interview schedule shortly.")

# def main():
#     print("👋 Hello! This is HR bot calling for your job interview.")

#     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
#                            channels=1, callback=callback):
#         print("\n👂 Are you interested in the job?")
#         clear_queue(q)
#         listen_for_intent(["InterestedIntent"])

#         print("\n📅 What is your notice period?")
#         clear_queue(q)
#         listen_for_intent(["NoticePeriodIntent"])

#         print("\n💰 What is your current and expected CTC?")
#         clear_queue(q)
#         listen_for_intent(["CTCIntent"])

#         print("\n📆 When are you available for interview next week?")
#         clear_queue(q)
#         listen_for_intent(["AvailabilityIntent"])

#     print("\n✅ Thank you! We'll confirm your interview schedule shortly.")
# if __name__ == "__main__":
#     main()


# import requests

# def main():
#     print("👋 Hello! This is HR bot calling for your job interview.")

#     with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
#                            channels=1, callback=callback):
#         print("\n👂 Are you interested in the job?")
#         clear_queue(q)
#         intent = listen_for_intent(["InterestedIntent"])
#         if intent:
#             requests.post("http://localhost:5000/api/response", json={"question": "Are you interested in the job?", "intent": intent})

#         print("\n📅 What is your notice period?")
#         clear_queue(q)
#         intent = listen_for_intent(["NoticePeriodIntent"])
#         if intent:
#             requests.post("http://localhost:5000/api/response", json={"question": "What is your notice period?", "intent": intent})

#         print("\n💰 What is your current and expected CTC?")
#         clear_queue(q)
#         intent = listen_for_intent(["CTCIntent"])
#         if intent:
#             requests.post("http://localhost:5000/api/response", json={"question": "What is your current and expected CTC?", "intent": intent})

#         print("\n📆 When are you available for interview next week?")
#         clear_queue(q)
#         intent = listen_for_intent(["AvailabilityIntent"])
#         if intent:
#             requests.post("http://localhost:5000/api/response", json={"question": "When are you available for interview next week?", "intent": intent})

#     print("\n✅ Thank you! We'll confirm your interview schedule shortly.")










import queue
import sounddevice as sd
import json
import vosk
import time
import pyttsx3
from adapt.engine import IntentDeterminationEngine
from adapt.intent import IntentBuilder

# Text-to-speech setup
engine_tts = pyttsx3.init()
def speak(text):
    print(f"🔊 Bot says: {text}")
    engine_tts.say(text)
    engine_tts.runAndWait()

# Load Vosk model
model = vosk.Model("models/vosk-model-small-en-us-0.15")
recognizer = vosk.KaldiRecognizer(model, 16000)
q = queue.Queue()

def callback(indata, frames, time_info, status):
    if status:
        print("⚠️ Audio status:", status)
    q.put(bytes(indata))

def start_audio_stream():
    stream = sd.RawInputStream(
        samplerate=16000, blocksize=8000,
        dtype='int16', channels=1, callback=callback)
    stream.start()
    return stream

def clear_audio_queue():
    while not q.empty():
        try:
            q.get_nowait()
        except queue.Empty:
            pass

# Set up Adapt engine
engine = IntentDeterminationEngine()
engine.register_intent_parser(IntentBuilder("InterestedIntent").require("interested").build())
engine.register_intent_parser(IntentBuilder("NoticeIntent").require("notice").require("period").build())
engine.register_intent_parser(IntentBuilder("CTCIntent").require("ctc").require("salary").build())

entities = {
    "interested": ["yes", "interested", "sure", "definitely", "yeah"],
    "notice": ["notice", "serving", "working"],
    "period": ["days", "weeks", "months", "1", "2", "3", "4"],
    "ctc": ["ctc", "salary", "package", "current", "expected"],
    "salary": ["lpa", "lakhs", "thousand", "k", "crore", "rupees"]
}

for key, values in entities.items():
    for value in values:
        engine.register_entity(value, key)

def listen_for_intent(expected_intent, timeout=15):
    recognizer.Reset()
    clear_audio_queue()
    print(f"🎤 Listening for {expected_intent}...")

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            data = q.get(timeout=timeout)
        except queue.Empty:
            continue

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            print(f"🗣 You said: {text}")
            for intent in engine.determine_intent(text):
                if intent["confidence"] > 0 and intent["intent_type"] == expected_intent:
                    print(f"✅ Detected: {intent['intent_type']}")
                    return True
            print("⚠️ Didn't match expected intent.")
            return False
    print("⏱️ Timed out.")
    return False

def main():
    print("🤖 Hello! I'm your HR bot.")
    stream = start_audio_stream()
    time.sleep(1)

    try:
        speak("Hello! I'm your HR bot. Let's begin your job interview.")

        # Question 1
        speak("Are you interested in the job?")
        if not listen_for_intent("InterestedIntent"):
            # speak("Sorry, I couldn't understand your response. Ending the call.")
            speak("Great ! lets take this talk forward")
            # return

        # Question 2
        speak("What is your notice period?")
        if not listen_for_intent("NoticeIntent"):
            # speak("Sorry, I couldn't understand your notice period. Ending the call.")
            # return
            speak("Great ! looks good")

        # Question 3
        speak("What is your current and expected CTC?")
        if not listen_for_intent("CTCIntent"):
            # speak("Sorry, I couldn't understand your CTC details. Ending the call.")
            # return
            speak("Fine")

        speak("Thank you! All your information is received. I will schedule your intervie , soon and notify we once the interview is scheduled")

    finally:
        stream.stop()
        stream.close()

if __name__ == "__main__":
    main()
