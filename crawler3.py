# -*- coding: utf-8 -*-
# ! git push https://github.com/junker-joerg/pythonworks [jeden Abend]
# !
# !
# ToDO: Die Umlaute umcodieren und in eine txt.datei speichern - Dateiname aus Kalenderwoche + Jahr zusammensetzen
# ToDO: Weitere RSS Quellen durch intere MA identifieren lassen - keine Programmierkenntnisse notwendig
# ToDO:     
# ToDO:
import feedparser
#import pandas
#import scrapy
import time






# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url )
    
# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])   
    return headlines




# A list to hold all headlines
allheadlines = []
# List of RSS feeds that we will fetch and combine
newsurls = {
    'CIO_1':            'https://www.cio.de/feed/at/1',                                     # CIO Managzin Nachrichten
    'CIO_2':            'https://www.cio.de/feed/p/3932',                                   # CIO Managzin Nachrichten
    'vs_foren_it':      'https://www.versicherungsforen.net/portal/de/system/rss/news.rss', # Versicherungsforen
    'CompWoche':        'https://www.computerwoche.de/feed/all'                             # Computerwoche
                        
}
# Iterate over the feed urls
for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )
if __name__ == "__main__":
    # Iterate over the allheadlines list and print each headline
    zeile = 0
    fname=time.strftime("CIO_STRATEGIE_IT_Trends_%Y-%m-%d-%H_%M"+".txt") # ! CIO_STRATEGIE_IT_Trends_2019-02-27-11_04.txt als Beispielausgabe
    
    trendsfile = open(fname, "w")
    trendsfile.write("Nr"+"\t"+"Inhalt\n")
    for hl in allheadlines:
        recode = str(hl).encode().decode("cp1252") # für Windows
        trendsfile.write(str(zeile))
        trendsfile.write("\t")
        trendsfile.write(recode+"\n")
        #print(recode)
        zeile = zeile + 1
    trendsfile.close()
    # ! hier dann den ersten Crawler einer relevanten deutsche IT-Strategie Seite (zB ein Blog) mit Scrapy aufrufen
    # https://www.dinotools.de/2015/11/10/mit-scrapy-zum-eigenen-webcrawler/ .. hier oder woanders
