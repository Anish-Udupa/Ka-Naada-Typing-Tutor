from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

"""
Title: Ka-Naada Typing Tutor
Description: A Kannada Typing Tutor App created for Ka-Naada Phonetics Ltd.
Author: Anish Udupa H <udupa.anish@gmail.com>
Date of creation: 11th April, 2021.
Version: 1.1
Fixes: Fixed the sa, ha key problems.
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
        self.letter_prob = {"ಕ": [0.3, 0, 0], "ಚ": [0.3, 0, 0], "ಟ": [0.3, 0, 0], "ತ": [0.3, 0, 0], "ಪ": [0.3, 0, 0], "ಗ": [0.3, 0, 0], "ಜ": [0.3, 0, 0],
                            "ಡ": [0.3, 0, 0], "ದ": [0.3, 0, 0], "ಬ": [0.3, 0, 0], "ಅ": [0.35, 0, 0], "ಆ": [0.35, 0, 0], "ಇ": [0.35, 0, 0], "ಈ": [0.35, 0, 0],
                            "ಉ": [0.35, 0, 0], "ಊ": [0.35, 0, 0], "ಋ": [0.35, 0, 0], "ೠ": [0.35, 0, 0], "ಎ": [0.35, 0, 0], "ಏ": [0.35, 0, 0],
                            "ಐ": [0.35, 0, 0], "ಒ": [0.35, 0, 0], "ಓ": [0.35, 0, 0], "ಔ": [0.35, 0, 0], "೧": [0.5, 0, 0], "೨": [0.5, 0, 0], "೩": [0.5, 0, 0],
                            "೪": [0.5, 0, 0], "೫": [0.5, 0, 0], "೬": [0.5, 0, 0], "೭": [0.5, 0, 0], "೮": [0.5, 0, 0], "೯": [0.5, 0, 0], "೦": [0.5, 0, 0],
                            "ಖ": [0.3, 0, 0], "ಛ": [0.3, 0, 0], "ಠ": [0.3, 0, 0], "ಥ": [0.3, 0, 0], "ಫ": [0.3, 0, 0], "ಘ": [0.3, 0, 0], "ಝ": [0.3, 0, 0],
                            "ಢ": [0.3, 0, 0], "ಧ": [0.3, 0, 0], "ಭ": [0.3, 0, 0], "ಙ": [0.3, 0, 0], "ಞ": [0.3, 0, 0], "ಣ": [0.3, 0, 0], "ನ": [0.3, 0, 0],
                            "ಮ": [0.3, 0, 0], "ಯ": [0.3, 0, 0], "ರ": [0.3, 0, 0], "ಲ": [0.3, 0, 0], "ವ": [0.3, 0, 0], "ಶ": [0.3, 0, 0], "ಷ": [0.3, 0, 0],
                            "ಸ": [0.3, 0, 0], "ಹ": [0.3, 0, 0], "ಳ": [0.3, 0, 0]}
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
            if self.letter_prob[key][0] < min:
                min = self.letter_prob[key][0]
        min_value = [key for key in self.letter_prob if self.letter_prob[key][0] == min]
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


normal_key_value = {"q": 3221, 'w': 3226, 'e': 3231, 'r': 3236, 't': 3242, "y": 3223, 'u': 3228, 'i': 3233, 'o': 3238,
                    'p': 3244, 'a': 3205, 's': 3206, 'd': 3207, 'f': 3208, 'g': 3209, 'h': 3210, 'j': 3211, 'k': 3296,
                    'l': 3214, 'z': 3215, 'x': 3216, 'c': 3218, 'v': 3219, 'b': 3220, '1': 3303, '2': 3304, '3': 3305,
                    '4': 3306, '5': 3307, '6': 3308, '7': 3309, '8': 3310, '9': 3311, '0': 3302, 'Q': 3222, "W": 3227,
                    "E": 3232, 'R': 3237, "T": 3243, "Y": 3224, "U": 3229, "I": 3234, "O": 3239, "P": 3245}

alt_gr_key_value = {"q": 3225, "w": 3230, "e": 3235, "r": 3240, "t": 3246, "y": 3247, "u": 3248, "i": 3250, "o": 3253,
                    "p": 3254, "bracketleft": 3255, "bracketright": 3256, "quoteright": 3257, "semicolon": 3251}


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
root.title("ಕ- ನಾದ typing tutor")
root.configure(bg=background_color)
root.geometry('525x360')
root.resizable(0, 0)

title = Label(root, text="WELCOME TO ಕ- ನಾದ TYPING TUTOR", font=("Times New Roman", 20), bg=background_color)
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