"""
This was a project from a book called:
Coding projects in Python.

The book is for students and I used it to
quickly pick up the basics of the Python language
with my Javascript background. :)
"""

from tkinter import Tk, simpledialog, messagebox

print('Countries and Capitals')
root = Tk()
root.withdraw()
world = {}

def fetchData():
    with open('data.txt') as data:
        for line in data:
            line = line.rstrip('\n')
            country, capital = line.split('/')
            world[country] = capital

def addData(country, capital):
    with open('data.txt', 'a') as data:
        data.write('\n' + country + '/' + capital)

fetchData()

while True:
    wantedCountry = simpledialog.askstring('Country', 'Give me the name of the country:')
    if wantedCountry in world:
        capital = world[wantedCountry]
        messagebox.showinfo('Answer', wantedCountry + '\'s capital is ' + capital + '!')
    else:
        newCapital = simpledialog.askstring('Teach me', 'I don\'t know what is the capital of ' + wantedCountry)
        world[wantedCountry] = newCapital
        addData(wantedCountry, newCapital)

root.mainloop()