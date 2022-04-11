import tweepy
import os
import pprint

CONSUMER_API_KEY = os.environ.get('CONSUMER_API_KEY')
CONSUMER_API_SECRET = os.environ.get('CONSUMER_API_SECRET')
ACCESS_API_KEY = os.environ.get('ACCESS_API_KEY')
ACCESS_API_SECRET = os.environ.get('ACCESS_API_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
auth.set_access_token(ACCESS_API_KEY, ACCESS_API_SECRET)
pprint = pprint.PrettyPrinter()

list_low_price = []
last_sold = ""

def send_t(message):
    if CONSUMER_API_SECRET and CONSUMER_API_KEY and ACCESS_API_SECRET and ACCESS_API_KEY:
        auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
        auth.set_access_token(ACCESS_API_KEY, ACCESS_API_SECRET)
        api = tweepy.API(auth)
        api.update_status(message)
    else:
        print('message not sent')
    print(f'--------------- message messaged send: {message}---------------')


def send_message(listingId, initialCost, ownerPercent, borrowerPercent, otherPercent, gotchiBRS, gotchiName, timeLend):
    global  list_low_price
    global last_sold
    if gotchiName == "":
        gotchiName = "Unnamed"
    message = f"""
Gotchi "{gotchiName}" with {gotchiBRS} BRS is available for lending !

Initial cost: {initialCost:.3f} $GHST for {timeLend} HRS

Details: owner takes {ownerPercent}%, borrower takes {borrowerPercent}%, and other takes {otherPercent}%
 
👻 https://app.aavegotchi.com/lending/{listingId} 👻
#AaveGotchi #Polygon
"""
    send_t(message)