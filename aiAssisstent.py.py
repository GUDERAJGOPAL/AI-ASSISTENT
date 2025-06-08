import speech_recognition as ai
import pyttsx3 as tts
import pywhatkit as yw
import datetime as dt

listener = ai.Recognizer()
machine = tts.init()

def talk(text):
    """Convert text to speech."""
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    """Capture and return the user's voice command."""
    try:
        with ai.Microphone() as origin:
            print('Listening...')
            listen = listener.listen(origin)
            instruction = listener.recognize_google(listen)
            instruction = instruction.lower()
            if 'raj' in instruction:
                instruction = instruction.replace('raj', "").strip()
            return instruction
    except ai.UnknownValueError:
        talk("Sorry, I didn't catch that. Please try again.")
        return None
    except ai.RequestError:
        talk("Sorry, there was an error with the speech recognition service.")
        return None

def play_raj():
    """Process the voice command and perform actions accordingly."""
    instruction = input_instruction()
    if instruction is None:
        return  # Exit if there's an issue with input

    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play', '').strip()
        talk(f'Playing {song}')
        yw.playonyt(song)
    elif 'time' in instruction:
        time = dt.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
    elif 'date' in instruction:
        date = dt.datetime.now().strftime('%d/%m/%y')
        talk(f"Today's date is {date}")
    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
    elif 'what is your name' in instruction:
        talk('I am Raj, thank you.')
    elif 'i love you' in instruction:
        talk('I am an AI, I don’t have emotions, but you are kind.')
    elif 'who is' in instruction or 'tell me about' in instruction:
        human = instruction.replace('who is', '').strip()
        try:
            info = yw.wikipedia.summary(human,1)
            print(info)
            talk(info)
        except Exception as e:
            talk("Sorry, I couldn't find any information on that.")
            print(f"Error: {e}")
    elif instruction == 'raj':
        talk('Hello, I am Raj, an AI assistant. How can I help you?')
    elif 'your age' in instruction:
        talk('I was created in 1960, so I am currently 64 years old.')
    elif instruction == 'stop':
        talk('Thank you, Raj is going to sleep.')
    else:
        talk("I couldn't understand that. Could you please repeat it?")

play_raj()
