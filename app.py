import speech_recognition as sr
from textblob import TextBlob
import pyttsx3

# Constants for the program
__AUTHOR__ = 'Aditya'
__GITHUB__ = 'https://github.com/adityaxanand'

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init('sapi5')
voices = tts_engine.getProperty('voices')
tts_engine.setProperty("voice", voices[0].id)

def take_sound():
    """
    Captures microphone input from the user and returns the recognized text.
    Returns:
        str: Recognized text from the user's speech.
    """
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 0.6
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        return query
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def get_sentiment(text):
    """
    Analyzes the sentiment of the provided text.
    Args:
        text (str): The text to analyze.
    Returns:
        str: The sentiment of the text ('Positive', 'Neutral', 'Negative').
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    print({'polarity': polarity, 'text': text})
    if polarity == 0:
        return "Neutral"
    elif polarity > 0:
        return "Positive"
    else:
        return "Negative"

def speak(audio):
    """
    Converts the provided text to speech.
    Args:
        audio (str): The text to be spoken.
    """
    tts_engine.say(audio)
    tts_engine.runAndWait()

def main():
    """
    The main function that runs the speech recognition, sentiment analysis,
    and text-to-speech feedback loop.
    """
    while True:
        text = take_sound()
        if text:
            sentiment = get_sentiment(text)
            response = f"I think you are speaking {sentiment} thoughts."
            print(f"Computer: {response}")
            speak(response)

if __name__ == "__main__":
    main()
