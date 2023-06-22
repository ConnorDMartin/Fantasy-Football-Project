# Fantasy-Football-Web-Scraper

This project was part of my initial dive into coding. As such, the coding is a bit rough, doesn't make much use of python's object oriented programming aspects, and is sparsley commented. However, the project was successful in fulfilling its purpose.
The purpose of this project is to collect footbal player and team data from a website that displays this data publically (www.footballdb.com/fantasy-football/). To do this, this program uses multiple python libraries (Requests, BeautifulSoup, and Fake User Agent) to scrape the desired information off of the target website's HTML code.

How it works / Usage:

Once run, this program uses the Requests library to establish a connection to the website and retrieving the page's HTML code. As part of this process, the Fake User Agent library is used to mask the user agent from the website. Since most websites have security measures to stop bots or webscrapers from accessing their website, a random user agent is used with each connection request. However, some agents in the list provided are detected as fake. When this occurs, the program must be rerun to continue collecting data.
Once the website's HTML code is successfully downloaded, the BeautifulSoup library is used to pull the desired data from the HTML code. Once the information is retrieved from the page's HTML code, the CSV library is used to format and store this data into a csv file.
CSV files were chosen as the method of data storage due to their wide use across multiple programs (like Matlab, Excel, etc.) where this data might be used.

Installation:
1. To run this code, you must first have python downloaded onto your computer (you can download the latest version of python [here](https://www.python.org/downloads/)).
2. Using your computer's terminal, you should then pip install the pandas, requests, bs4, csv, and fake_useragent libraries.
3. Once all the libraries have been installed, download the web-s.py program in this repository.
4. You can run this program using your computer's terminal or a program like VS Code.
5. Once you begin running the program, the CSV files with weekly data on player performance will be added to the same folder the web-s.py file is located in.
