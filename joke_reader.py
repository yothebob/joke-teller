import pyttsx3
import random
engine = pyttsx3.init()


def read_joke(filename):
    file = open(filename, "r")
    lines = file.read().splitlines()
    myline = random.choice(lines)
    print(myline)
    engine.say(myline)
    engine.runAndWait()
    return
