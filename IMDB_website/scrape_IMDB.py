# IMDB Top 250 Movies
from bs4 import BeautifulSoup
import requests, openpyxl

# function for converting K,M,B words to numeric
def value_to_float(input):
    input = input.upper()
    if('K' in input):
        return float(input.replace('K',''))*1000
    elif('M' in input):
        return float(input.replace('M',''))*100000
    elif('B' in input):
        return float(input.replace('B',''))*1000000000
    else: return float(input)

# excel initialization
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "IMDB Top 250 Movies"

try:
    # source url
    url = "https://www.imdb.com/chart/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
    response = requests.get(url,headers=headers)

    response.raise_for_status()

    soup = BeautifulSoup(response.content,"html.parser")

    movies = soup.find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base")
    
    table_columns = ["Movie Rank","Movie Title","Movie Release Year","Movie Duration","Movie Rating","Movie Rating Vote Count"]
    sheet.append(table_columns)
    index = 1
    for movie in movies:
        movie_rank = movie.find("h3",class_="ipc-title__text").text.split('.',1)[0]
        movie_title = movie.find("h3",class_="ipc-title__text").text.split('.',1)[1].strip()
        movie_year = movie.find_all("span",class_="sc-4dcdad14-8 cvucyi cli-title-metadata-item")[0].text
        movie_duration = movie.find_all("span",class_="sc-4dcdad14-8 cvucyi cli-title-metadata-item")[1].text
        movie_rating = movie.find("span",class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.split("\xa0")[0]
        movie_rating_vote_count = movie.find("span",class_="ipc-rating-star--voteCount").text.strip("\xa0").strip("()")
        
        table_rows = [int(movie_rank),str(movie_title),int(movie_year),str(movie_duration),float(movie_rating),value_to_float(movie_rating_vote_count)]
        sheet.append(table_rows)
    
    # saving to excel file
    excel.save('./IMDB_website/IMDB_Top_250_Movies.xlsx')
        
except Exception as e:
    print("Exception:",e)
