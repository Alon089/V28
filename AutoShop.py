import json
import random
import schedule
from threading import *
import time
from datetime import datetime, timedelta
from Logic.Player import Players
from Logic.Device import Device

from DataStream.OfferGenerator import OfferGenerator

class AutoShop:
    def update_offers(self):
	    self.device = Device(self.client)
	    self.player = Players(self.device)
    
	    with open('Logic/JSON/offers.json', 'r') as f:
	        data = json.load(f)
		
	    brawlers1337 = []
	    dudka = self.player.BrawlersUnlockedState
	    upgrades = self.player.Brawler_level
	    pps = self.player.brawlers_upgradium
	    for brawler in dudka:
	       if int(dudka[brawler]) == 1 and int(upgrades[brawler]) != 8:
		       brawlers1337.append(int(brawler))
		       
	       generated = []
	       generated.append(OfferGenerator.generateDailyGift(brawlers1337) )
	       offs = OfferGenerator.generateOffersList(brawlers1337)
	       for offer in offs:
		       generated.append(offer)
	       generated = str(generated).replace("'", "\"")
				
	       data['Offers'] = generated
	       with open('Logic/JSON/offers.json', 'w') as f:
		       json.dump(data, f)

	       # Магаз обновлён в консоси
	       now = datetime.now()
	       print(f"Магазин обновлен: {now.strftime('%Y-%m-%d %H:%M:%S')}")

	       schedule.every().day.at("20:32").do(AutoShop.update_offers(self))

# Инфинити цикл, чтобы не завершался.
while True:
    schedule.run_pending()
    time.sleep(1)
