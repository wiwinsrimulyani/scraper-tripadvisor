import scrapy


class UrlwisataSpider(scrapy.Spider):
    name = 'urlWisata'
    allowed_domains = ['tripadvisor.co.id']
    #start_urls = ['https://www.tripadvisor.co.id/Attractions-g293920-Activities-a_allAttractions.true-Phuket.html']
    start_urls = ['https://www.tripadvisor.co.id/Attractions-g294230-Activities-c58-Yogyakarta_Region_Java.html']

    def parse(self, response):
        results = response.css('._25PvF8uO').css('._1MKm6PFo')
        for result in results:
            print('URL: ' + "https://www.tripadvisor.co.id" + result.css('._6sUF3jUd').css('a::attr(href)').extract()[0])
            print('title: ' + result.css('._6sUF3jUd').css('._1QKQOve4').xpath('./h2/text()').extract()[0])
            #print('count_review: ' + result.css('._2-JBovPw').xpath('./span/span/text()').extract_first())

            yield{
                'URL' : "https://www.tripadvisor.co.id" + result.css('._6sUF3jUd').css('a::attr(href)').extract()[0],
                'title' : result.css('._6sUF3jUd').xpath('./a/h2/text()').extract()[0],
                'count_review' : result.css('._2-JBovPw').xpath('./span/span/text()').extract_first()
            }

        #next = response.css('.ui_pagination.is-centered')
        #next_url = next.css('a::attr(href)').extract_first()
        #print(next_url)

        
        next = response.css('.ui_button.nav.next.primary')
        #print(next)
           
        next_url = next.css("a::attr(href)").extract_first()
        print(next_url)

        if next_url is not None:
            next_url = "https://www.tripadvisor.co.id" + next_url
            yield scrapy.Request(url = next_url, callback= self.parse)
            
        
         
        
        
                

        #if next_url is not None:
        #    for i in range(30, 960, 30):
                #https://www.tripadvisor.co.id/Attractions-g294230-Activities-oa30-a_allAttractions.true-Yogyakarta_Region_Java.html
        #        next_url = "https://www.tripadvisor.co.id/Attractions-g294230-Activities-oa" + str(i) + "-a_allAttractions.true-Yogyakarta_Region_Java.html"
        #        print(next_url)
        #        yield scrapy.Request(url= next_url, callback=self.parse)
        
        
