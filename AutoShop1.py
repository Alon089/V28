import AutoShop
import schedule

class Shop:
    def op(self):
        schedule.every().day.at("20:39").do(AutoShop.update_offers(self))