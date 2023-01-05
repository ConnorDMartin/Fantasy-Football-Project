# Note to all users: if when running you recieve the error message "AttributeError: 'NoneType' object has no attribute 'find'"
# That means that the website you are scraping from has discovered that the user agent you are using belongs to a scraper
# To fix, run the program again, program randomizes user agents with every request, so error is unlikely to reoccur

#import libraries
import pandas as py
import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent
import time

#bypass 403 error
ua = UserAgent()

#webscraper function
def scrape_webpage_week(year, week, repetitions):
    if repetitions==7:
        repetitions=0
        time.sleep(120)
    elif repetitions != 0:
        repetitions+=1
        time.sleep(10)
    #access html
    URL = "https://www.footballdb.com/fantasy-football/index.html?pos=OFF&yr=20"+str(year)+"&wk="+str(week)+"&key=48ca46aa7d721af4d58dccc0c249a1c4"
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    user_agent = ua.random
    page = requests.get(URL, headers={'User-Agent':user_agent})
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="statistics scrollable")

    '''
    # Code for testing with .HTML file
    HTMLFile = open("practice.html", "r")

    index = HTMLFile.read()

    soup = BeautifulSoup(index, "html.parser")

    results = soup.find(class_="statistics scrollable")
    '''

    #find title elements
    title_row=[]
    all_title_elements = results.find("thead")

    title_elements = all_title_elements.find_all("tr")

    i=0
    for element in title_elements:
        if i!=0:
            titles = element.find_all("th")
            for title in titles:
                if title.text != "Game":
                    title_row.append(title.text)
        i+=1


    #find player elements
    player_rows=[]

    all_player_elements = results.find("tbody")

    player_elements = all_player_elements.find_all("tr")

    for element in player_elements:
        player_row=[]

        player_name_element = element.find(class_="hidden-xs")
        player_name = player_name_element.find("a")
        player_row.append(player_name.text)

        '''
        # the following is an abandoned code to record the game played by the player
        # formatting issues with the resulting text and lack of use for final product made code obsolete

        game_elements = element.find(class_="center")
        for game in game_elements:
            player_row.append(game.text)
        '''

        i=0
        stat_elements = element.find_all("td")
        for stat in stat_elements:
            if i>1:
                player_row.append(stat.text)
            i+=1
        player_rows.append(player_row)


    #open csv file
    csv_file_address=str(year)+'-'+str(week)+'-stats.csv'
    with open(csv_file_address, 'w', newline='') as f:
        writer = csv.writer(f)

        # write rows to csv file
        first_row=["","","Passing","","","","","","Rushing","","","","Receiving","","","","Fumbles",""]
        writer.writerow(first_row)
        writer.writerow(title_row)

        for row in player_rows:
            writer.writerow(row)
    return repetitions

def scrape_webpage_year(year, repetitions):
    if repetitions==7:
        time.sleep(120)
        repetitions=0
    else:
        repetitions+=1
        time.sleep(10)
    #access html
    URL = "https://www.footballdb.com/fantasy-football/index.html?pos=OFF&yr=20"+str(year)+"&wk=all&key=48ca46aa7d721af4d58dccc0c249a1c4"
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    user_agent = ua.random
    page = requests.get(URL, headers={'User-Agent':user_agent})
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="statistics scrollable")

    '''
    # Code for testing with .HTML file
    HTMLFile = open("practice.html", "r")

    index = HTMLFile.read()

    soup = BeautifulSoup(index, "html.parser")

    results = soup.find(class_="statistics scrollable")
    '''

    #find title elements
    title_row=[]
    all_title_elements = results.find("thead")

    title_elements = all_title_elements.find_all("tr")

    i=0
    for element in title_elements:
        if i!=0:
            titles = element.find_all("th")
            for title in titles:
                if title.text != "Game":
                    title_row.append(title.text)
        i+=1


    #find player elements
    player_rows=[]

    all_player_elements = results.find("tbody")

    player_elements = all_player_elements.find_all("tr")

    for element in player_elements:
        player_row=[]

        player_name_element = element.find(class_="hidden-xs")
        player_name = player_name_element.find("a")
        player_row.append(player_name.text)

        '''
        # the following is an abandoned code to record the game played by the player
        # formatting issues with the resulting text and lack of use for final product made code obsolete

        game_elements = element.find(class_="center")
        for game in game_elements:
            player_row.append(game.text)
        '''

        i=0
        stat_elements = element.find_all("td")
        for stat in stat_elements:
            if i>1:
                player_row.append(stat.text)
            i+=1
        player_rows.append(player_row)


    #open csv file
    csv_file_address="overall-"+str(year)+'-stats.csv'
    with open(csv_file_address, 'w', newline='') as f:
        writer = csv.writer(f)

        # write rows to csv file
        first_row=["","","Passing","","","","","","Rushing","","","","Receiving","","","","Fumbles",""]
        writer.writerow(first_row)
        writer.writerow(title_row)

        for row in player_rows:
            writer.writerow(row)
    return repetitions

#select webpage
'''
year=10
week=1
rep=0
while year<=22:
    while week<=17:
        rep = scrape_webpage(year, week, rep)
        week+=1
    week=1
    year+=1
'''

decision=input("Collect data for Season Totals, Week Totals throughout multiple years, or individual weeks (s/w/i): ")
if decision=="s" or decision=="S":
    rep=0
    year=10
    while year <=22:
        rep = scrape_webpage_year(year, rep)
        year+=1
        week=1
elif decision=="w" or decision=="W":
    week=1
    rep=0
    year_range_beginning=int(input("Select year you would like to begin collecting data from: "))
    year_range_end=int(input("Select year you would like to stop collecting data at: "))
    year_range=year_range_end-year_range_beginning
    year=year_range_beginning-2000

    while year_range !=0:
        while week<=17:
            rep = scrape_webpage_week(year, week, rep)
            week+=1
        year_range-=1
        year+=1
        week=1
elif decision=="i" or decision=="I":
    year=int(input("Year: "))
    year-=2000
    week=int(input("Week: "))
    rep=0
    rep = scrape_webpage_week(year, week, rep)
