# IMDB website scraping

I have written a python program which will access the IMDB website and then fetch the top rated movies present in the IMDB website and then load this data into an excel file.

### The website is: [IMDB Website](https://www.imdb.com/chart/top/)

### The libraries used in this project is:
* **BeautifulSoup:** To parse the HTML content and then provides multiple methods which can be used to extract the data from any HTML tags.
* **requests:** To access the desired websites.
* **openpyxl:** To create a new excel file and then rename the sheet name and then load data into an excel file.

### The python code is:
https://github.com/arunsacharyadev/web_scraping_projects/blob/d0c8871fb81820fa727b6106383be1e7d251e369/IMDB_website/scrape_IMDB.py#L1-L52

### The generated excel file is:
<a href="IMDB_Top_250_Movies.xlsx"><img src="https://camo.githubusercontent.com/bbde5a2f6da9c1190fd175a0e92beb67acfe3137d333f95f4d656ed34a856251/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6963726f736f6674253230457863656c2d3231373334362e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d4d6963726f736f66742d457863656c266c6f676f436f6c6f723d7768697465" /></a>
