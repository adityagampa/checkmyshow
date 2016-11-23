from lxml import html
import requests
import os
import time

while True:
    page = requests.get('https://in.bookmyshow.com/buytickets/kabali-telugu-hyderabad/movie-hyd-ET00041490-MT/20160808')
    tree = html.fromstring(page.content)
    theatres = tree.xpath('//strong/text()')
    requiredtheatre="pvr"
    print theatres
    for i in theatres:
        if requiredtheatre in i.lower():
            print "Book Tickets.."
            os.startfile('C://Users//Aditya//Music//Kaththi (Original Motion Picture Soundtrack)//Kaththi Theme.mp3')
            break
    else:
        time.sleep(180)
        print "Again started"
        continue
    break