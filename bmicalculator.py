import tkinter as tk
from tkinter import font
import webbrowser

import requests
from bs4 import BeautifulSoup

import customentry


# Utility Functions
def calculate_bmi(measurements):
    valid_feet = True 
    valid_inches = True
    valid_weight = True

    try:
        feet = float(measurements[0])
    except:
        valid_feet = False
    try:
        inches = float(measurements[1])
    except:
        valid_inches = False
    try:
        weight = float(measurements[2])
    except:
        valid_weight = False
    
    label_text = ''
    if (not valid_feet) or (not valid_inches) or (not valid_weight):
        if not valid_feet:
            label_text += 'Feet invalid.'
        if not valid_inches:
            label_text += '\nInches invalid.'
        if not valid_weight:
            label_text += '\nWeight invalid.'
        label['text'] = label_text + '\nVerify that all inputs are numerical.'
    else:
        total_height_meters =((feet * 12) + inches) * 0.0254
        weight_kilograms = weight * 0.45359237
        return (round((weight_kilograms / (total_height_meters**2)), 1))

def request_and_find(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'lxml')
    match = soup.find('div', class_='__chrome').find('div', id = '__next').find_all('div', class_='css-ps3vwz')
    headlines_string = ''
    count = 0
    for elem in match:
        if count < 5:
            headlines_string += '\n ' + elem.find('h2').text + '\n ' + elem.find('a', class_='css-2fdibo').text + '\n'
            count += 1
    return headlines_string

def open_link(url):
    webbrowser.open(url)


def provide_recs(measurements):
    result_bmi = calculate_bmi(measurements)
    if (result_bmi < 18.5):
        headlines_string= request_and_find('https://www.medicalnewstoday.com/categories/eating-disorders')
        label['text'] = 'BMI: ' + str(result_bmi) + '\n' + 'BMIs lower than 18.5 suggest you may have an eating disorder. The headlines below display recent articles relating to potential conditions.' '\n' + headlines_string
        underweight_link = tk.Label(label, text="Go to Medical News Today", fg='blue', cursor='hand2')
        underweight_link.place(relx=0.425, rely=0.9)
        underweight_link.bind('<Button-1>', lambda e: open_link('https://www.medicalnewstoday.com/categories/eating-disorders'))
    elif(18.5 <= result_bmi <= 24.9):
        label['text'] = 'BMI: ' + str(result_bmi) + '\n Your BMI is healthy!'
    else:
        headlines_string= request_and_find('https://www.medicalnewstoday.com/categories/fitness-obesity')
        label['text'] = 'BMI: ' + str(result_bmi) + '\n' + 'BMIs greater than 24.9 suggest you may be overweight. The headlines below display recent articles related to potential conditions.''\n' + headlines_string
        overweight_link = tk.Label(label, text="Go to Medical News Today", fg='blue', cursor='hand2')
        overweight_link.place(relx=0.425, rely=0.9)
        overweight_link.bind('<Button-1>', lambda e: open_link('https://www.medicalnewstoday.com/categories/fitness-obesity'))


# Display
root = tk.Tk('')
# Constants
win_height = root.winfo_screenheight()
win_width = root.winfo_screenwidth()
# root.attributes('-fullscreen', True)
root.title("BMI Calculator")
root.resizable(False, False)

canvas = tk.Canvas(root, height=win_height, width=win_width)
canvas.pack()

info_label = tk.Label(root, text='Welcome to BMI Calculator! Enter your height and weight below to compute your BMI and learn more.', font=('Arial', 16))
info_label.place(relx=0.185, rely=0.015)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

feet_entry = customentry.CustomEntry(frame, 'Feet')
feet_entry.place(relx=0, rely=0, relwidth=0.3, relheight=0.45)

inches_entry = customentry.CustomEntry(frame, 'Inches')
inches_entry.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.45)

weight_entry = customentry.CustomEntry(frame, 'Pounds')
weight_entry.place(rely=0.5, relwidth=0.65, relheight=0.45)

button = tk.Button(frame, text='Calculate', font=('Arial', 12), command=lambda: provide_recs([feet_entry.get(), inches_entry.get(), weight_entry.get()]))
button.place(relx=0.7, rely=0.2, relwidth=0.3, relheight=0.6)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth = 0.75, relheight=0.65, anchor='n')

label = tk.Label(lower_frame, font=('Arial', 12))
label.place(relwidth=1, relheight=1)

root.mainloop()
