# list of coursera courses
from bs4 import BeautifulSoup
import pandas as pd
import requests

# function for converting K,M,B words to numeric
def value_to_float(input):
    input = str(input).upper()
    if('K' in input):
        return int(float(input.replace('K',''))*1000)
    elif('M' in input):
        return int(float(input.replace('M',''))*100000)
    elif('B' in input):
        return int(float(input.replace('B',''))*1000000000)
    else: return int(input)

try:
    # base url
    base_url = "https://www.coursera.org/courses"
    html_data = BeautifulSoup(requests.get(base_url).content,"html.parser")
    
    # finding page count from pagination
    page_count = html_data.find("div",class_="pagination").find("button",{"aria-label":"Go to last page"}).text
    table_columns = ["Course Title","Course Partner","Course Difficulty","Course Certification Type","Course Duration","Course Rating","Course Review Count"]
    # creating a pandas dataframe
    df = pd.DataFrame(columns=table_columns)

    for i in range(1,int(page_count)+1):
        # pagination url
        url = base_url+"?page="+str(i)
        response = requests.get(url)
        
        html_soup = BeautifulSoup(response.content,"html.parser")
        courses = html_soup.find("ul",class_="cds-9 css-18msmec cds-10")
        
        # iterating on individual items
        for course in courses:
            course_title = getattr(course.find("div",class_="cds-ProductCard-header").find("h3",class_="cds-119 cds-CommonCard-title css-e7lgfl cds-121"),"text","").strip(':')
            course_partner = getattr(course.find("div",class_="cds-ProductCard-header").find("div",class_="cds-ProductCard-partnerInfo").find("p",class_="cds-119 cds-ProductCard-partnerNames css-dmxkm1 cds-121"),"text","").strip()
            course_difficulty = getattr(course.find("div",class_="cds-ProductCard-footer").find("div",class_="cds-CommonCard-metadata").find("p",class_="cds-119 css-dmxkm1 cds-121"),"text","").split("·")[0].strip()
            course_certificate_type = getattr(course.find("div",class_="cds-ProductCard-footer").find("div",class_="cds-CommonCard-metadata").find("p",class_="cds-119 css-dmxkm1 cds-121"),"text","").split("·")[1].strip()
            course_duration = getattr(course.find("div",class_="cds-ProductCard-footer").find("div",class_="cds-CommonCard-metadata").find("p",class_="cds-119 css-dmxkm1 cds-121"),"text","").split("·")[2].strip()
            course_rating = getattr(course.find("div",class_="cds-ProductCard-footer").find("div",class_="cds-CommonCard-ratings").find("p",class_="cds-119 css-11uuo4b cds-121"),"text","0.0").strip()
            course_review_count = getattr(course.find("div",class_="cds-ProductCard-footer").find("div",class_="cds-CommonCard-ratings").find("p",class_="cds-119 css-dmxkm1 cds-121"),"text","0").strip("()").strip(" reviews")
            
            table_rows = [str(course_title),str(course_partner),str(course_difficulty),str(course_certificate_type),str(course_duration),float(course_rating),value_to_float(course_review_count)]
            length = len(df)
            # inserting rows into dataframe
            df.loc[length]=table_rows
            print("inserted page ",i,":",len(df))
    
    # saving to excel file
    df.to_excel("./coursera_website/coursera_courses.xlsx",index=False)

except Exception as e:
    print(e)