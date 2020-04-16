import requests
from bs4 import BeautifulSoup
import tkinter as tk

feet = 5
inches = 6
weight = 140

def calculate_bmi(feet, inches, weight):
    total_height_meters =((feet * 12) + inches) * 0.0254
    weight_kilograms = weight * 0.45359237
    return round((weight_kilograms / (total_height_meters**2)), 1)

temp_bmi = calculate_bmi(feet, inches, weight)

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


# provide_recs(15)

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry: ", entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Calculate', font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth = 0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
