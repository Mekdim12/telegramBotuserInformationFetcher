
from tkinter import EXCEPTION
import firebase_admin.messaging
from firebase_admin import credentials
from firebase_admin import db


credentialInformation = credentials.Certificate({

    "type": "service_account",
    "project_id": "informationfetherbot",
    "private_key_id": "383c9982d41d8f035b5b5ac2ddb599e5cc0544f0",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC61Vgs7GlDBnim\nxEQXMTSdj/2jhf6dDVTqnpKH0bEX/ZQIg8QAWyQIZFZr7bVLXzZpAei2ihHGp/lR\nmO/jVw+QmEdzLaeIAWBdwOL7861kmpljxNUCtWIRSHBy0iWH/BBlp4tN6qulW43S\nkL2gMy1AgzanqE/GiPLbiDfsIFzXlwx5vwRVPwBfmlb38olsES8quTt5GJbiVnIl\nQbI+r/6+UmuHHNV1GaTn6tCtKY9q2+H5HV/llOd6497PncDsA/xweY2zhxRESi0e\nVFYpTI/vGPNC7sqUDDJYmUyNKpTj6Fm38v4K1hW0d3qYA5okyza6fiP3zWJh4VZR\n6XpXOz0RAgMBAAECggEABfksVhbapHHCdZ/+ppBsXImCECpofh5TD8OBPzIIR8Jj\n60wFriZ70eAd3nphjorpMR0mUuA6EmQ0UZxadpX17Z89wRAljCDRozu3khs7yOSz\nuOOuFQWmMJPkovomqKjpoAtl1fhV064IPDJEGskqFib/zkdQgiImpBfQRGaSO1MH\nLkXxqLXBlq8R9Hu2CSXVIhEaU/YaV1btZxy6Estb0m9tP7/xo2QhPo4j/LOYd1bo\nWboz8H2jhAcR9WC1xsBrCLIu8gX0lLL32o8la6aRspFpDBtXKMTJQfokoOO0r7LW\nWtW8MHH6AoTa3/Kf7GVpllcia/7WCfyaVgqiFuEpIQKBgQDf2qByCJE/ue637Raa\nfAuqGPEAGr7ndqGjuhOw71km2BjPyARkfEhC1dHVux5Sd5UR1wasVUvcFFuRT2b+\neev1W5CZO7ZaxHD9Hf/lWocwakUQB/QIZ0NdB8h9uG2EV62akcpQGjNW2QGnUXsw\noF8hz19W+6PO3t7HAfGBf/7K4QKBgQDVqcGr4nDDxxL9Rd2mLtBgYAQBPBpvy9O/\nqyWNXGPVWeOafOPPzzjOF1WwjRHDAJBFnPwtGVIbl3Q6qUxjmEYCAzyFuC1C5k+l\nuzFTIsEGGUaBrV3blQgOj9VK7cZNfOK7848NuGnwQXTv7WWVnPgpBCuPI8MgTgVm\nMIzEqWtoMQKBgEHqfMhXYX3kYDjkpX1D/aNOyNiBB6ncsuglSNsW/6eChnvYqAJ2\n3khf8fP/r4QVFl40dRCV5Uqe6/+z494XRLXxCnk0rhO4OJUwGkQNDjXhdQitbtxy\nm9FvE0iB4C3SK5qSR4Ki1G9EY0pDogTFlH2+NJLGcovd8LelCNpbOEnBAoGBAMpR\nUWOaKt8nnXKYepaG06e+o2wr5nigECT5QbjGmH4I/P1nbyxy8z4rWGeyXPRCj1pr\nmVp3FImt81AsyXmxUfFL8T5JtQoZHag4Ri+LxC0rN9lJOYvYZeWsCvNFjbYIIIaK\nzZXXXvEyejFKoRt3pIDqQvjqizUGzBQEuvbp2huxAoGAQnCtdy9vPDSMzlPKdHMd\n4iIGPPRDZCVEPCLMUndMTy9fNjIOOTC919aHLMJ9Z9BaMvtYgvlHu56P7ipmp2hF\neVks1kVlLFvsS4/T2txHf2++qz4m6R2ke0bjaBAwWoFHnWkD2ZcBbb7+RNis3lN9\nU6WQYFQWzvFHxsilLBkkkIc=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-faie3@informationfetherbot.iam.gserviceaccount.com",
    "client_id": "101725108351172785850",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-faie3%40informationfetherbot.iam.gserviceaccount.com"

})  # used to create instance of the database specificaion like id  u get this by generating it in  Service Accounts In project Setting --> then hit genetrat a key with specified key


firebase_admin.initialize_app(credentialInformation, {
    "databaseURL": "https://informationfetherbot-default-rtdb.firebaseio.com/"})  # this is ur db instance with url


def profileInformationRetriver(telegramID):
    ref = db.reference("User").child(telegramID)

    try:

        if ref.get() is not None:
            return ref.get()
        else:
            return None

    except Exception as e:
        print(e)
        print("error  in profileInformationRetriver 846465")
        return None


def statusInformationUpater(telegramID):
    ref = db.reference("User").child(telegramID)

    try:

        if ref.get() is not None:

            currentStat = int(ref.get()['status'])+1
            ref.update({'status': str(currentStat)})

            return True

    except Exception as e:
        print("############## error at status information updatere ")
        print(e)

    return False


def inertingTheInformation(telegramID, keyvalue, valueToBeStored):

    ref = db.reference("User").child(telegramID)

    try:

        ref.update({keyvalue: valueToBeStored})
        return True

    except Exception as e:
        print("#################### Error in insertingTheInformation")
        print(e)

    return False


def stageForInformationFetcher(telegramID):
    ref = db.reference("User").child(telegramID)

    if ref.get() is not None:
        status = ref.get()['status']
        return status

    return None


def checkifUserAlreadRegisteredOrNot(telegramID):

    ref = db.reference("User").child(telegramID)

    if ref.get() is not None:
        # alrady have an accountc
        return True
    else:
        # no account before
        return False


def InitalizaeAuser(telegramId):

    if checkifUserAlreadRegisteredOrNot(telegramID=telegramId):

        db.reference('User').child(telegramId).delete()

    ref = db.reference('User')

    dataToBeStored = {
        "FullName": "",
        "PhoneNumberOne": "",
        "PhoneNumberTwo": "",
        "telegramUserName": "",
        "Email": "",
        "Location": "",
        "cv": "",
        "resume": "",
        "weblink": "",
        "status": "1"
    }

    try:
        ref.child(telegramId).set(dataToBeStored)
        return True
    except Exception as e:
        print("######## exception one in initlaizer a user method")
        return False
