import csv
from selenium import webdriver
from time import sleep
from random import randint

import multiprocessing
multiprocessing.set_start_method('spawn')


driver = webdriver.Chrome(executable_path= 'D:\SCRAPER\z - ChromeDriver\chromedriver.exe')

urls = []
with open('url_bali_ow_all.csv', 'r', encoding = 'ISO-8859-1') as oj:
    oj_reader = csv.reader(oj, delimiter = ',')
    for row in oj_reader:
        urls.append(row[0])
urls.pop(0)

##we need looping here
nameLength = len(urls)
f = open('HASIL/hasil_bali_things.csv', 'w', newline='', encoding="utf-8")
with f:
    writer = csv.writer(f)
    writer.writerow(['name', 'date'])
    place_count = 0
    for l in range(0, nameLength):
        review_count = 0
        place_count = place_count + 1

        try:
            driver.get(urls[l])
        except:
            try: 
                print('failed to load webpage')
            except:
                "tidak ada"
        sleep(randint(2,3))

 #       try:
 #           radio_bttn = driver.find_element_by_id('LanguageFilter_0')
 #           driver.execute_script('arguments[0].click();', radio_bttn)
 ##          try:
   #             print('page is ready')
  #          except:
  #              "tidak ada"
   #     except:
  #          try:
   #             print('failed to click radio button')
   #         except:
    #            "tidak ada"
            

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
                next_page_bttn = driver.find_element_by_xpath('//a[@aria-label = "Next page"]')
            except:
                "tidak ada"
            
            try:
                listings_date = driver.find_elements_by_class_name('_3JxPDYSx')
            except:
                "tidak ada"

            try:
                listings_date = driver.find_elements_by_class_name('fEDvV')
            except:
                "tidak ada"

            sleep(randint(1,2))            
            for listing in listings_date:
                    
                try:
                    name_place =  driver.find_element_by_class_name('_3QHreJVJ').text
                    print(name_place)
                except:
                    "tidak ada"

                try:
                    name_place =  driver.find_element_by_class_name('DrjyGw-P._1SRa-qNz.qf3QTY0F').text
                    print(name_place)
                except:
                    "tidak ada"

                try:
                    name_place =  driver.find_element_by_class_name('WlYyy.cPsXC.GeSzT').text
                    print(name_place)
                except:
                    "tidak ada"

                            
                try:
                    date1 = listing.text
                    date = date1.split(' • ')[0]
                    
                    if(date is None):
                        date = date1
                    print(date)
                except:
                    "tidak ada"
                            
                            
                        
                        
                detail = []
                detail.append(name_place)
                detail.append(date)

                writer.writerow(detail)
            review_count = review_count +  len(listings_date)
            print("place count : " + str(place_count))
            print("review count : " + str(review_count))

                #click the next button in pagination
            try:
                sleep(randint(1,2))
                next_page_bttn.click()
                sleep(randint(1,2))

                try:
                    print('<---------------------next page ---------------->')
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

#driver.close()


                               

