from requests_html import HTMLSession

class Scraper():

    def scrapequotes(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        qlist = []

        quotes = r.html.find('div.quote')
        for q in quotes:
            item = {
                'text' : q.find('span.text', first=True).text.strip(),
                'Author' : q.find('small.author', first=True).text.strip()
            }
            
            qlist.append(item)

        return qlist

    def scrapeecommerce(self, tag):
        url = f'https://webscraper.io/test-sites/e-commerce/allinone/computers/{tag}'
        s = HTMLSession()
        r = s.get(url)

        plist = []

        products = r.html.find('div.col-sm-4')
        
        for product in products:
            item  = {
                'product' : product.find('a.title', first=True).text.strip(),
                'price': product.find('h4.pull-right', first=True).text.strip(),
                'description': product.find('p.description', first=True).text.strip(),
                'reviews': product.find('p.pull-right', first=True).text.strip(),    
            }
            
            plist.append(item)
        return plist


product = Scraper()

product.scrapeecommerce('tablets')
