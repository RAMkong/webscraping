from booking.pythonProject import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.close_sing_in_option()
    bot.change_currency(currency="USD")