# 7.9.2020
# define eine class "Adresse"
# generiere Fake-Daten
# schreibe die Class mit 'pickle' in eine Datei
# generiere ein umfassendes LogFile

import logging
from faker import Faker
import sys

f = Faker("de_DE")

class adresse:
    def __init__(adr, Name, Adresse, Info):
        adr.Adresse = Adresse
        adr.Name = Name
        adr.Info = Info  
        
 
def initAdress():
    i = 0
    al = [] # Adressliste 
    while i < 10:
        al.append(adresse(f.name(), f.address(), f.text()))
        i = i + 1
    #https://github.com/joke2k/faker
    
def writeData():
    i = 0
    while i < 10:
    
        i = i + 1     

def main():
    # Logging
    logFormatter = '%(asctime)s - %(levelname)s - %(message)s' 
    # ! apple kennt keinen User
    LOG_FILE = "ueben.log"
    logging.basicConfig(format=logFormatter, level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(LOG_FILE)
    logger.addHandler(handler)
    logger.info("Log gestartet")
    logger.info("Main aufgerufen")
    logger.info("InitAdress aufgerufen")
    initAdress()    # class Adress + Fake Daten schreiben 
    writeData()     # in pickle    
    logger.info("Log beendet")
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
    
