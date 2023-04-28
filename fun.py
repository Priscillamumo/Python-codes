def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("""Hi, I am priscilla and I don't know how to smile""")
    print(greeting)
greet(shout)
greet(whisper)

