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
        # file = open('testfile.txt', 'w')
        # file.write(str(match))
        for elem in match:
            if elem.div:
                if str.isdigit(elem.div.a.text[0]):
                    print(elem.div.a.text)
    elif(18.5 <= bmi < 25):
        print('Healthy Weight')
    else:
        page = requests.get('https://www.eatthis.com/healthy-weight-loss-foods/')
        soup = BeautifulSoup(page.content,'lxml')
        # match = soup.find('div', class_ = 'main-content').find('div', class_='content').find('div', class_='number-head-mod number-head-mod-standalone').find('div', class_='header-mod').h2.text
        match = soup.find('div', class_ = 'main-content').find('div', class_='content').find_all('h2', class_='title')
        for elem in match:
            print(elem.text)


provide_recs(14)
