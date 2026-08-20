import cowsay
cowsay.cow("GoodMooorning!")
# for cool ASCII art, you can also use other animals like:
from art import tprint
tprint("Hello World!")

#for colored terminal
from termcolor import colored
print(colored("Hello, World!", "green"))
print(colored("Hello, World!", "red", attrs=["bold"]))

#for emojis
from emoji import emojize
print(emojize("Python is :thumbs_up:"))
print(emojize("Python is :cat::computer:"))

#for fetching online data
import wikipedia
result = wikipedia.summary("Python programming language", sentences=1)
print(result)