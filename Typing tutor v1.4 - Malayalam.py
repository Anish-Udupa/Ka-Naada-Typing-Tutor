from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

"""
Title: Ka-Naada Typing Tutor
Description: A Kannada Typing Tutor App created for Ka-Naada Phonetics Ltd.
Author: Anish Udupa H <udupa.anish@gmail.com>
Date of creation: 11th April, 2021.
Version: 1.4
Fixes: v1.1: Fixed the sa, ha key problems.
       v1.2: Fixed ha problem.
       v1.3: Removed ha.
       v1.4: Fixed the 'same characters being displayed multiple times' bug.
"""

class ScoreManager:
    def __init__(self, initial_score=0):
        self.score = initial_score
        self.correct_attempts = 0
        self.total_attempts = 0

    def correct_key_pressed(self):
        self.score += 10
        self.correct_attempts += 1
        self.total_attempts += 1

    def wrong_key_pressed(self):
        self.score -= 5
        self.total_attempts += 1

    def get_score(self):
        return self.score

    def compute_percentage(self):
        _perc = self.correct_attempts / self.total_attempts * 100
        return round(_perc, 2)

class Letter:

    def __init__(self):
        self.next_display = []
        # In the dictionary's values, [probability, no_of_correct_attempts, total_number_of_attempts]
        self.letter_prob = {"ക": [0.3, 0, 0], "ച": [0.3, 0, 0], "ട": [0.3, 0, 0], "ത": [0.3, 0, 0], "പ": [0.3, 0, 0], "ഗ": [0.3, 0, 0], "ജ": [0.3, 0, 0],
                            "ഡ": [0.3, 0, 0], "ദ": [0.3, 0, 0], "ബ": [0.3, 0, 0], "അ": [0.35, 0, 0], "ആ": [0.35, 0, 0], "ഇ": [0.35, 0, 0], "ഈ": [0.35, 0, 0],
                            "ഉ": [0.35, 0, 0], "ഊ": [0.35, 0, 0], "ഋ": [0.35, 0, 0], "ഌ": [0.35, 0, 0], "എ": [0.35, 0, 0], "ഏ": [0.35, 0, 0],
                            "ഐ": [0.35, 0, 0], "ഒ": [0.35, 0, 0], "ഓ": [0.35, 0, 0], "ഔ": [0.35, 0, 0], "൧": [0.5, 0, 0], "൨": [0.5, 0, 0], "൩": [0.5, 0, 0],
                            "൪": [0.5, 0, 0], "൫": [0.5, 0, 0], "൬": [0.5, 0, 0], "൭": [0.5, 0, 0], "൮": [0.5, 0, 0], "൯": [0.5, 0, 0], "೦": [0.5, 0, 0],
                            "ഖ": [0.3, 0, 0], "ഛ": [0.3, 0, 0], "ഠ": [0.3, 0, 0], "ഥ": [0.3, 0, 0], "ഫ": [0.3, 0, 0], "ഘ": [0.3, 0, 0], "ഝ": [0.3, 0, 0],
                            "ഢ": [0.3, 0, 0], "ധ": [0.3, 0, 0], "ഭ": [0.3, 0, 0], "ങ": [0.3, 0, 0], "ഞ": [0.3, 0, 0], "ണ": [0.3, 0, 0], "ന": [0.3, 0, 0],
                            "മ": [0.3, 0, 0], "യ": [0.3, 0, 0], "ര": [0.3, 0, 0], "ല": [0.3, 0, 0], "വ": [0.3, 0, 0], "ശ": [0.3, 0, 0], "ഷ": [0.3, 0, 0],
                            "സ": [0.3, 0, 0], "ള": [0.3, 0, 0]}  # "ഹ": [0.3, 0, 0],
        self.initial_set_next_display()

    def initial_set_next_display(self):
        letters = [key for key in self.letter_prob]
        for i in range(9):
            char = letters[randint(0, len(letters)-1)]
            self.next_display.append(char)

    def get_char(self):
        # Computing the minimum value
        min = 1  # Assumption
        for key in self.letter_prob:
            if (self.letter_prob[key][0] < min) and (key not in self.next_display):
                min = self.letter_prob[key][0]
        min_value = [key for key in self.letter_prob if ((self.letter_prob[key][0] == min) and (key not in self.next_display))]
        char = min_value[randint(0, len(min_value)-1)]
        self.next_display.append(char)  # Adding a new character to the list.
        # Returns the first element of the next_display list and also removes the element from that list.
        return self.next_display.pop(0)

    def get_remaining_char(self):
        # Returns the remaining characters of the list next_display.
        remaining = " ".join(self.next_display)
        return remaining

    def is_correct(self, key):
        self.letter_prob[key][1] += 1  # Increments the no_of_correct attempts
        self.letter_prob[key][2] += 1  # Increments the total_no_of_attempts as the character will be displayed.
        try:
            perc = self.letter_prob[key][1]/self.letter_prob[key][2]  # Calculates the percentage.
        except ZeroDivisionError:
            perc = 1
        self.letter_prob[key][0] = perc

    def is_wrong(self, key):
        self.letter_prob[key][2] += 1  # Increments the total_no_of_attempts as the character will be displayed.
        try:
            perc = self.letter_prob[key][1]/self.letter_prob[key][2]  # Calculates the percentage.
        except ZeroDivisionError:
            perc = 1
        self.letter_prob[key][0] = perc


normal_key_value = {"q": 3349, 'w': 3354, 'e': 3359, 'r': 3364, 't': 3370, "y": 3351, 'u': 3356, 'i': 3361, 'o': 3366,
                    'p': 3372, 'a': 3333, 's': 3334, 'd': 3335, 'f': 3336, 'g': 3337, 'h': 3338, 'j': 3339, 'k': 3340,
                    'l': 3342, 'z': 3343, 'x': 3344, 'c': 3346, 'v': 3347, 'b': 3348, '1': 3431, '2': 3432, '3': 3433,
                    '4': 3434, '5': 3435, '6': 3436, '7': 3437, '8': 3438, '9': 3439, '0': 3302, 'Q': 3350, "W": 3355,
                    "E": 3360, 'R': 3365, "T": 3371, "Y": 3352, "U": 3357, "I": 3362, "O": 3367, "P": 3373}

alt_gr_key_value = {"q": 3353, "w": 3358, "e": 3363, "r": 3368, "t": 3374, "y": 3375, "u": 3376, "i": 3378, "o": 3381,
                    "p": 3382, "bracketleft": 3383, "bracketright": 3384, "semicolon": 3379}  # No "ഹ-3385"


def check_letter(pressed_letter, expected_letter, alt_gr_pressed=False):
    global score, letter_obj

    # Checks if the letters match or not.
    try:
        if alt_gr_pressed is False:
            if ord(expected_letter) == normal_key_value[pressed_letter]:
                score.correct_key_pressed()
                letter_obj.is_correct(expected_letter)
            else:
                score.wrong_key_pressed()
                letter_obj.is_wrong(expected_letter)

        elif alt_gr_pressed is True:
            if ord(expected_letter) == alt_gr_key_value[pressed_letter]:
                score.correct_key_pressed()
                letter_obj.is_correct(expected_letter)
            else:
                score.wrong_key_pressed()
                letter_obj.is_wrong(expected_letter)
    except KeyError:
        # If the key pressed is not a part of the dictionaries, take it as a wrong key pressed.
        score.wrong_key_pressed()
        letter_obj.is_wrong(expected_letter)

def set_letters():
    global letter_obj, display_current_letter, display_remaining_text
    display_current_letter["text"] = letter_obj.get_char()
    display_remaining_text["text"] = letter_obj.get_remaining_char()

def update_stats():
    global score, score_label, percentage_label, stats_label
    stats_label["text"] = " STATISTICS "
    score_label["text"] = "SCORE:  {}".format(score.get_score())
    percentage_label["text"] = "CORRECT ANSWER PERCENTAGE:  {}%".format(round(score.compute_percentage(), 2))

def pause_screen():
    global score_label, percentage_label, stats_label
    stats_label["text"] = " STEPS "
    score_label["text"] = "1. Click on resume button to continue."
    percentage_label["text"] = "2. Type the letter present in the left box above."

def on_key_press(event):
    # Called when a key is pressed.
    global hasStarted, alt_r_pressed
    ignore_these_keys = ["Alt_L", "Win_L", "space", "Alt_R", "Return", "Escape", "Caps_Lock", "Shift_L", "Shift_R", "Tab", "Control_L"]
    # Control_L + Alt_R = Alt Gr

    if hasStarted:  # If user has clicked the start button, accept the keyboard input.
                    # Doesnt accept keyboard input if the application is in 'reset' mode.
        key_pressed = event.keysym  # Stores the english character pressed
        current_letter = display_current_letter["text"].strip()
        if key_pressed not in ignore_these_keys:
            check_letter(key_pressed, current_letter, alt_r_pressed)
            # print("Key pressed", key_pressed)
            update_stats()
            alt_r_pressed = False
            set_letters()
        elif key_pressed == "Alt_R":
            alt_r_pressed = True

def on_key_release(event):
    # If the Alt_R key is released.
    global alt_r_pressed
    key_released = event.keysym
    if key_released == "Alt_R":
        alt_r_pressed = False

def start_button_pressed():
    global hasStarted, startButton, display_remaining_text, display_current_letter
    if hasStarted is False:
        hasStarted = True
        startButton["text"] = "CLICK HERE TO PAUSE"
        display_current_letter["width"] = 5
        display_current_letter["borderwidth"] = 2
        display_current_letter["relief"] = "ridge"
        display_remaining_text.grid(sticky="W")
        set_letters()

    elif hasStarted is True:
        hasStarted = False
        display_current_letter["text"] = str()
        display_remaining_text["text"] = str()
        display_current_letter["borderwidth"] = 0
        startButton["text"] = "CLICK HERE TO RESUME"
        pause_screen()


# Main
root = Tk()
background_color = "#FDE5B4"  # A variable that stores the hex code of the background color.
root.title("Ka-Naada typing tutor")
root.configure(bg=background_color)
root.geometry('580x360')
root.resizable(0, 0)

title = Label(root, text="WELCOME TO MALAYALAM TYPING TUTOR", font=("Times New Roman", 20), bg=background_color)
title.grid(row=0, column=0, padx=10, pady=20, columnspan=2)

kannada_text_font = ("Times New Roman", 25)
display_current_letter = Label(root, font=kannada_text_font, bg=background_color)
display_remaining_text = Label(root, font=kannada_text_font, bg=background_color)
display_current_letter.grid(row=1, column=0, padx=10)
display_remaining_text.grid(row=1, column=1, padx=10)

alt_r_pressed = False  # A flag to determine if Alt_R was pressed in the previous keypress.
hasStarted = False  # A flag used to determine if the application is running or not.
score = ScoreManager()  # Object that keeps track of the score.
letter_obj = Letter()  # Object of class Letter.

text_font = ("Times New Roman", 20)
line_label = Label(root, text="-"*50, font=text_font, bg=background_color)
line_label.grid(row=4, column=0, sticky="n", columnspan=2)

stats_label = Label(root, text=" STEPS ", font=("Times New Roman", 20, "underline"), bg=background_color)
stats_label.grid(row=5, column=0, columnspan=2)

statistics_font = ("Roboto", 15)
score_label = Label(root, text="1. Click on start to begin.", font=statistics_font, bg=background_color)
score_label.grid(row=6, column=0, columnspan=2, padx=10, sticky="w")

percentage_label = Label(root, text="2. Type the letter present in the left box above.", font=statistics_font, bg=background_color)
percentage_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="w")

startButton = Button(root, text="CLICK HERE TO START", font=("Roboto", 20), command=start_button_pressed, bg=background_color)
startButton.grid(row=8, column=0, pady=15, columnspan=2, sticky="s")
root.bind("<Key>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

root.mainloop()