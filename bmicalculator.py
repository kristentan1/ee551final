import requests
from bs4 import BeautifulSoup
from tkinter import font
import tkinter as tk

# Constants
HEIGHT = 500
WIDTH = 600

# Utility Functions
def calculate_bmi(measurements):
    valid_feet = True 
    valid_inches = True
    valid_weight = True

    try:
        feet = int(measurements[0])
    except:
        valid_feet = False
    try:
        inches = int(measurements[1])
    except:
        valid_inches = False
    try:
        weight = int(measurements[2])
    except:
        valid_weight = False
    # return round((weight_kilograms / (total_height_meters**2)), 1)
    
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
        label['text'] = str(round((weight_kilograms / (total_height_meters**2)), 1))

def provide_recs(bmi):
    if (bmi < 18.5):
        page = requests.get('https://www.healthline.com/nutrition/18-foods-to-gain-weight')
        soup = BeautifulSoup(page.content, 'lxml')
        match = soup.find('div', class_='__chrome').find('div', id = '__next').find_all('h2')
        for elem in match:
            if elem.div:
                if str.isdigit(elem.div.a.text[0]):
                    print(''.join([i for i in elem.div.a.text if not i.isdigit()])[2:] )
    elif(18.5 <= bmi < 25):
        print('Healthy Weight')
    else:
        page = requests.get('https://www.healthline.com/nutrition/20-most-weight-loss-friendly-foods')
        soup = BeautifulSoup(page.content,'lxml')
        match = soup.find('div', class_='__chrome').find('div', id = '__next').find_all('h2')
        for elem in match:
             if elem.div:
                if str.isdigit(elem.div.a.text[0]):
                    # print(''.join([i for i in elem.div.a.text if not i.isdigit())])
                    print(''.join([i for i in elem.div.a.text if not i.isdigit()])[2:] )

# Display
root = tk.Tk('')
root.title("BMI Calculator")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.2, anchor='n')

feet_entry = tk.Entry(frame, font=('Courier', 18),borderwidth=2)
feet_entry.place(relx=0, rely=0, relwidth=0.3, relheight=0.45)

inches_entry = tk.Entry(frame, font=('Courier', 18),borderwidth=2)
inches_entry.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.45)

weight_entry = tk.Entry(frame, font=('Courier', 18), borderwidth=2)
weight_entry.place(rely=0.5, relwidth=0.65, relheight=0.45)

button = tk.Button(frame, text='Calculate', font=('Courier', 12), command=lambda: calculate_bmi([feet_entry.get(), inches_entry.get(), weight_entry.get()]))
button.place(relx=0.7, rely=0.2, relwidth=0.3, relheight=0.6)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth = 0.75, relheight=0.65, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12))
label.place(relwidth=1, relheight=1)

root.mainloop()
