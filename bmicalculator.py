import requests
from bs4 import BeautifulSoup

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


provide_recs(15)
