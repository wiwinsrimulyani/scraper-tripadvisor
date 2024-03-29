import csv
from selenium import webdriver
from time import sleep
from random import randint
import multiprocessing
multiprocessing.set_start_method('spawn')


driver = webdriver.Chrome(executable_path= 'D:\SCRAPER\z - ChromeDriver\chromedriver.exe')

urls = []
with open('url_bali_resto_noduplicates.csv', 'r', encoding = 'ISO-8859-1') as oj:
    oj_reader = csv.reader(oj, delimiter = ',')
    for row in oj_reader:
        urls.append(row[0])
urls.pop(0)


##we need looping here
nameLength = len(urls)
f = open('HASIL/hasil_bali_resto.csv', 'w', newline='', encoding="utf-8")
with f:
    writer = csv.writer(f)
    writer.writerow(['name', 'title', 'date', 'review_text' ])
    place_count = 0

    for l in range(0, nameLength):
        review_count = 0
        place_count = place_count +1
        try:
            driver.get(urls[l])
        except:
            try: 
                print('failed to load webpage')
            except:
                "tidak ada"
        sleep(randint(2,3))

        try:
            radio_bttn = driver.find_element_by_xpath('//*[@id="filters_detail_language_filterLang_ALL"]')
            driver.execute_script('arguments[0].click();', radio_bttn)
            sleep(2)
            try:
                print('page is ready')
            except:
                "tidak ada"
        except:
            try:
                print('failed to click radio button')
            except:
                "tidak ada"
            
        try:
            selengkapnya_bttn = driver.find_element_by_xpath("//span[contains(@class,'taLnk ulBlueLinks')]")
            driver.execute_script('arguments[0].click();', selengkapnya_bttn)
            sleep(2)
            try:
                print("'selengkapnya' bttn has been clicked!")
            except:
                "tidak ada"
        except:
            try:
                print("tidak ada selengkapnya/ atau failed to click")
            except:
                "tidak ada"
        
        try:
            pagenum = driver.find_elements_by_class_name('pageNum ')
            #return a list
            try:
                numiter = int(pagenum[len(pagenum)-1].text)
                
            except:
                try:
                    pagenum = 0
                    #print("[~~~~~~~~~~no contains page number~~~~~~~~~~]")
                except:
                    "tidak ada"
                
        except:
            "page num tidak ada"
        if (pagenum == 0):
            numiter = 1
            
        while True:
            try:
                next_page_bttn = driver.find_element_by_xpath('//a[@class = "nav next ui_button primary"]')
            except:
                "tidak ada"
            
            sleep(randint(1,2))
            try:
                listings = driver.find_elements_by_class_name('review-container')
            except:
                "tidak ada"
            #get all review in that page
            for listing in listings:                    
                try:
                    name_place =  driver.find_element_by_class_name('eTnlN._W.w.O').text
                    #print(name_place)
                except:
                    "tidak ada"
                
                try:
                    name_place =  driver.find_element_by_class_name('_3QHreJVJ').text
                    #print(name_place)
                except:
                    "tidak ada"


                try:
                    name_place =  driver.find_element_by_class_name('_1mTlpMC3').text
                    #print(name_place)
                except:
                    "tidak ada"

                try:
                    name_place =  driver.find_element_by_class_name('_3a1XQ88S').text
                    print(name_place)
                except:
                    "tidak ada"   

                try:
                    name_place =  driver.find_element_by_class_name('ui_header.h1').text
                    #print(name_place)
                except :
                    "tidak ada"
                
                try:
                    title = listing.find_element_by_class_name('noQuotes').text
                    print(title)
                except:
                    "tidak ada"
                    
                try:
                    date1 = listing.find_element_by_class_name('ratingDate').get_attribute("title")
                    date = date1.split(': ')[1]
                    print(date1)
                except:
                    "tidak ada"
                    
                try:
                    review_text = listing.find_element_by_class_name('partial_entry').text
                    print(review_text)
                except:
                    "tidak ada"
     
                
                
                
                detail = []
                detail.append(name_place)
                detail.append(title)
                detail.append(date1)
                detail.append(review_text)

                writer.writerow(detail)

            
            review_count = review_count +  len(listings)
            print("place count : " + str(place_count))
            print("review count : " + str(review_count))
                
            try:
                next_page_bttn.click()
                sleep(randint(1,2))
                if(next_page_bttn is not None):
                    try:
                        print('<------------------next page ------------------>')
                        #print('/n')
                        #print('/n')
                    except:
                        "tidak ada"
            except:
                
                if(pagenum == 0):
                    try:
                        print('only 1 page')
                        break
                    except:
                        "tidak ada"
                else:
                    try:
                        print('the end of pagination')
                        break
                    except:
                        "tidak ada"

            try:
                selengkapnya_bttn = driver.find_element_by_xpath("//span[contains(@class,'taLnk ulBlueLinks')]")
                driver.execute_script('arguments[0].click();', selengkapnya_bttn)
                sleep(2)
                try:
                    print("'selengkapnya' bttn has been clicked!")
                except:
                    "tidak ada"
            except:
                try:
                    print("tidak ada selengkapnya/ atau failed to click")
                except:
                    "tidak ada"


                               

