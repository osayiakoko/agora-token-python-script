import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rtc_token_builder import RtcTokenBuilder, Role_Attendee, Role_Publisher
from rtm_token_builder import RtmTokenBuilder, Role_Rtm_User


appID = "your-app-id"
appCertificate = "your-app-certificate"
expirationTimeInSeconds = 60 * 60
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expirationTimeInSeconds

# below varables are used for the same purpose
uid = 83
userAccount = "83"

def get_rtc_token():
    channelName = "testroom"
    print(channelName)

    #IMPORTANT! Build token with either the uid or with the user account. Comment out the option you do not want to use below.

    # Build token with uid
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Publisher, privilegeExpiredTs)
    print("Rct Token (int uid): {}".format(token))

    # Build token with user account
    token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Publisher, privilegeExpiredTs)
    print("Rtc Token (string uid): {}".format(token))


def get_rtm_token():
    token = RtmTokenBuilder.buildToken(appID, appCertificate, userAccount, Role_Rtm_User, privilegeExpiredTs)
    print("Rtm Token: {}".format(token))


get_rtm_token()
get_rtc_token()
