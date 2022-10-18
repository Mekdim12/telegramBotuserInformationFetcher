

import profile
from telegram import *

from telegram.ext import *

from firebaseDbConnectivity import *


import os

key_token = os.getenv('BOTAPIKEY')



bot = Bot(key_token)

updater = Updater(key_token, use_context=True)
dispatcher = updater.dispatcher

Detail = '''
    This telegram bots is come up with the idea for a job seekers that intended to make closer conection among the job seeker and job recuritters  since this platforms are increasing in daily basis its better to separate different job types in different simpler platforms like telegram channels and bots where people can easly.
    ***
        so There are necessarily required by this bot all personal information and other education details 
        1.Full name (name  - father name - last name)
        2.email
        3.current location
        4.telegram using phone number
        5.telegram user name
        6.alternative phone number
        7.cv
        8.resume
        9.portfoli website/ lindin link
    ይህ የቴሌግራም ቦቶች ከስራ ፈላጊው እና ከስራ ፈላጊው ጋር ተቀራርበው እንዲገናኙ ለማድረግ ያሰበውን ሃሳብ ይዞ የመጣ ነው። እነዚህ መድረኮች በየቀኑ እየጨመሩ በመሆናቸው የተለያዩ የስራ ዓይነቶችን በተለያዩ ቀላል መንገዶች መለየት የተሻለ ነው። እንደ ቴሌግራም ቻናሎች እና ቦቶች ያሉ ሰዎች በቀላሉ የሚችሉባቸው መድረኮች።

    ስለዚህ በዚህ ቦት ሁሉም የግል መረጃዎች እና ሌሎች የትምህርት ዝርዝሮች የግድ አስፈላጊ ናቸው።
        1. ሙሉ ስም (ስም - የአባት ስም - የአያት ስም)
        2.ኢሜል
        3.የአሁኑ መኖሪያ ቦታ
        4.ቴሌግራም ስልክ ቁጥር በመጠቀም
        5.ቴሌግራም የተጠቃሚ ስም
        6.አማራጭ ስልክ ቁጥር
        7.ሲቪ
        8.ረዚዩም
        9. ፖርቶፎሊዮ ዌብሳይት / ሊንክዲን ኣድራሻ


    caution: Inserting all the infomation  without skipping will increase the chance u will reach a job recuritters
    
    ይጠንቀቁ፡   ሁሉንም መረጃዎች ሳይዘለሉ ማስገባት ወደ ስራ ፈላጊዎች የመድረስ እድልን ይጨምራል

     *****Choose How You Want To Proceed?****** 
'''

dumJobsLists = [

    """
    DMC CONSTRUCTION PLC ሰራተኞችን አወዳድሮ መቅጠር ይፈልጋል። 
        Position: -  Project Finance Head

        📚ትምህርት ዓይነት እና ደረጃ:- 
        BA degree in accounting and Finance 

        🇪🇹 የስራ ቦታ ፡ Seqela Adet, Amhara

        🧭የምዝገባ ጊዜ ፡ እስከ ጥቅምት 
        17  /2015 ዓ.ም

        🔔ስለ ስራው ሙሉ መረጃ ለማየት  እና ለማመልከት ቀጣዩን ሊንክ ይጠቀሙ
        https://tikusjobs.com/job/project-finance-head/
    """,
    
    """
        Defense Construction Design Enterprise ሰራተኞችን አወዳድሮ መቅጠር ይፈልጋል። 


            Postion:
            1:Laboratory Technician / Medical, 2:Druggist,
            3: Intermediate Communication Officer, 4:Senior Communications Officer, and More

            📚የትምህርት ዓይነት እና ደረጃ:
            Diploma or Degree in relevant field

            🇪🇹 የስራ ቦታ: Addis Ababa 

            🧭የምዝገባ ጊዜ ፡እስከ ጥቅምት
            12/2015 ዓ.ም    

            🔔ስለ ስራው ሙሉ መረጃ ለማየት  እና ለማመልከት ቀጣዩን ሊንክ ይጠቀሙ

            https://jobs.amazonethiopia.com/job/defense-construction-design-enterprise/
    """,
    """
        NGO Jobs
            Construction Solutions PLC በሚከተሉት  የስራ መደቦች  በዜሮ ዓመት በርካታ ሰራተኞችን አወዳድሮ መቅጠር ይፈልጋል። 

            Position:- 20 positions
            1:Internship:20

            📚የትምህርት ዓይነት እና ደረጃ:-
            MSc/MBA/MA/BSc/BA in Civil Engineering/ & Management/Project  Management/Architecture/Computer Science/Information Systems/Economics/Urban Planning.

            🧭የምዝገባ ጊዜ ፡እስከ መስከረም
            28/2015 ዓ.ም    

            🔔ስለ ስራው ሙሉ መረጃ ለማየት  እና ለማመልከት ቀጣዩን ሊንክ ይጠቀሙ
            https://jobs.amazonethiopia.com/job/construction-solutions-plc/

    """,
    """
        Plan International Ethiopia ሰራተኞችን አወዳድሮ መቅጠር ይፈልጋል። 

            Position: - Construction Supervisor

            📚ትምህርት ዓይነት እና ደረጃ:- 
            B.SC degree and above from a recognized University in Civil/Hydraulic Engineering, Construction Technology, Construction Management, Building Technology or related fields

            🇪🇹 የስራ ቦታ፡ Afar -different woreda

            🧭የምዝገባ ጊዜ ፡ እስከ  ሀምሌ 
            29   /2014 ዓ.ም

            🔔ስለ ስራው ሙሉ መረጃ ለማየት  እና ለማመልከት ቀጣዩን ሊንክ ይጠቀሙ
            https://tikusjobs.com/job/construction-supervisor-2/
        
        """
    

]
def documnetHandler(update: Update, context: CallbackContext):
    
    documnet = update.message.document

    BookDocumentFile = documnet.to_json()

    
    if inertingTheInformation(str(update.effective_user.id),"cv",BookDocumentFile):

        KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")],"Are You Sure Do You Want To Continue with these document")
          
    else:
        print("Vlaue can't be inserted ################ code 0254")




def locationAndUserNameHandler(update: Update, context: CallbackContext):
    cordiantesoFlocation = str(update.message.location)

    import json
    cordiantesoFlocation = json.dumps(cordiantesoFlocation)

    if cordiantesoFlocation is not None:
        if inertingTheInformation(str(update.effective_user.id),"Location",cordiantesoFlocation):
            if statusInformationUpater(str(update.effective_user.id)):
                    KeyBoardMaker(update, CallbackContext , [KeyboardButton( "Share username")] , "Insert current telegram using username for this account by pressing share button below?")
            else:
                print("Vlaue can't be udpated ################ code 49640")
        else:
            
            print("Vlaue can't be inserted ################ code 0254")
    else:
        KeyBoardMaker(update,CallbackContext, [KeyboardButton( "Share username", request_contact=True)], "Make Sure You Check The Visiblity of your username in ur setting otherwise this app wn't work/በአንተ ቅንብር ውስጥ የስልክ ቁጥርን ታይነት ማረጋገጥህን አረጋግጥ አለበለዚያ ይህ መተግበሪያ አይሰራም")
    



def KeyBoardMaker(update, context, listofKeys, message):
        menuKeyBorad = [
           listofKeys
        ]
        replymakrkup = ReplyKeyboardMarkup(menuKeyBorad, resize_keyboard=True)
        bot.send_message( update.effective_user.id, text = message, reply_markup = replymakrkup)


def PhoneNumberFetcherFromaAuser(update: Update, context: CallbackContext):
    Information = update.message.contact
    phoneNumber = Information["phone_number"]
    
    
    if phoneNumber is not None:
        if inertingTheInformation(str(update.effective_user.id),"PhoneNumberOne",phoneNumber):
            if statusInformationUpater(str(update.effective_user.id)):
                    replKbd = ReplyKeyboardRemove
                    KeyBoardMaker(update, CallbackContext ,[KeyboardButton("Skip")],"Enter your alternative phone number incase contarctur wants to contact you?")
            else:
                print("Vlaue can't be udpated ################ code 48000")
        else:
            
            print("Vlaue can't be inserted ################ code 5480")
    else:
        KeyBoardMaker(update,CallbackContext, [KeyboardButton( "Phone Number")], "Make Sure You Check The Visiblity of phone numbe in ur setting otherwise this app wn't work/በአንተ ቅንብር ውስጥ የስልክ ቁጥርን ታይነት ማረጋገጥህን አረጋግጥ አለበለዚያ ይህ መተግበሪያ አይሰራም")




def StartingRegistering(update, context):


    menuKeyBorad = [
                 [KeyboardButton("Agree and Continue")]
            ]


    replymakrkup = ReplyKeyboardMarkup(menuKeyBorad, resize_keyboard=True)
    bot.send_message(update.effective_user.id, text=Detail, reply_markup=replymakrkup)






def textCommandsHandler(update: Update, context: CallbackContext):
    command = update.message.text
    command = command.strip()

    telegramUserID = str(update.effective_user.id)
    if command == "Show Jobs":
        for job in dumJobsLists:
            bot.send_message(update.effective_user.id, text = job)
            
    elif command == "Profile":
        information = profileInformationRetriver(telegramUserID)
        if information is not None:
            Profile = """

                FullName:"""+information['FullName']+"""
                Default Phone Number : """+information['PhoneNumberOne']+"""
                Alternative Phone Number : """+information['PhoneNumberTwo']+"""
                User Name : """+information['telegramUserName']+"""
                Location : """+information['Location']+"""
                Email : """+information['Email']+"""
                CV """+information['cv']+"""
               
            """
            bot.send_message(update.effective_user.id, text=profile)
             
        else:
             bot.send_message(update.effective_user.id, text="Make Sure Register First")
                    

    elif command == "Agree and Continue": 

        if InitalizaeAuser(telegramUserID):
           
            repl  = ReplyKeyboardRemove()

            bot.send_message(update.effective_user.id, text="Insert Your Full Name/ሙሉ ስምህን አስገባ?",reply_markup=repl)
        else:
            StartingRegistering(update,CallbackContext)
    else:

        if checkifUserAlreadRegisteredOrNot(telegramID=telegramUserID):

            status = stageForInformationFetcher(telegramID=telegramUserID)
             

            if status == "1":
                if command == "Yes/አዎ":
                    if statusInformationUpater(telegramUserID):
                            KeyBoardMaker(update, CallbackContext ,[KeyboardButton("Phone Number",request_contact=True)],"share Your Telegram using Number by presing button blelow ")
                    else:
                       print("Vlaue can't be inserted ################ code 480")
 
                     # to the next question
                elif command == "No/አይ":
                    
                    KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")],"Insert Your Full Name/ሙሉ ስምህን አስገባ?")
          
                else:
                    if inertingTheInformation(telegramUserID, "FullName", (str(command)).strip()):
                        
                        KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")] , "Are You Sure Do You Want To Contunue?")   
                    
                    else:
                        print("Vlaue can't be inserted ################ code 452")

                 # insering name
            elif status == "2":
                
                    bot.send_message(update.effective_user.id, text="Share Your Number By Pressing Button Below!! in order to Continue")
                 # phoenumnber one
            elif status  == "3":
                # if user is skipping
                if command == "Skip":
                    if inertingTheInformation(telegramUserID, "PhoneNumberTwo", "Not APPLICABLE"):
                            KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")] , "Are You Sure Do You Want To Contunue?")  
                    else:
                        print("Vlaue can't be inserted ################ code 45552")  

                elif command == "Yes/አዎ":
                    if statusInformationUpater(telegramUserID):
                            KeyBoardMaker(update, CallbackContext ,[KeyboardButton("Share Location",request_location=True)],"Insert your Location/የቴሌግራም ተጠቃሚዎን ቦታ ያስገቡ")
                    else:
                       print("Vlaue can't be inserted ################ code 4856560")
 
                elif command == "No/አይ":
                    KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Skip") ],"Insert An Alternactivae Phone number")
                else:
                    leng = 0
                    if command.startswith("+"):
                        leng = len(command.strip()) #+251924041650
                    elif command.startswith("09"):
                        leng = len(command.strip()) # 0924041650
                    
                    if leng == 13 or leng == 10:
                        if inertingTheInformation(telegramUserID, "PhoneNumberTwo", (str(command)).strip()):
                            KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")] , "Are You Sure Do You Want To Contunue?")  
                        else:
                            print("Vlaue can't be inserted ################ code 47852")  
                            
                    else:
                        KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Skip") ],"Share Your Number By typing ur valid full phone number or skip Pressing in order to Continue")
                 
                         # it is just an answer thatis not phone number so ignores it
                    

                 # phone Number Two
            elif status == "4":
                bot.send_message(update.effective_user.id, text="Share Your Location By Pressing Button Below!! in order to Continue if you are currently on telegram desktop switch to mobile phone to send the location")
                #  location
            elif status == "5":

                username = str(update.effective_user.username)
                if username.strip() == "" or username is None:
                    bot.send_message(update.effective_user.id, [ KeyboardButton("Share username") ], text="Share Your Username By Pressing Button Below!! in order to Continue if you are current setting is not visbible make sure u check the visiblity in your setting")
                else:
                    if inertingTheInformation(telegramUserID, "telegramUserName", "@"+username) and statusInformationUpater(telegramUserID):
                        repl  = ReplyKeyboardRemove()
                        bot.send_message(update.effective_user.id, text="Enter Your Email address?")
                    else:
                        print("Vlaue can't be inserted ################ code 4550052")  

                 #  useraname
            elif status == "6":
                if command == "Yes/አዎ":
                    if statusInformationUpater(telegramUserID):
                            bot.send_message(update.effective_user.id, text="Upload your curriculum vitae(CV) in file format of(.docx or pdf)")
                    else:
                       print("Vlaue can't be inserted ################ code 12480")
 
                     # to the next question
                elif command == "No/አይ":
                    
                    KeyBoardMaker(update, CallbackContext , [ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")],"Insert Your Email Adress CarFully?")
          
                else:
                    if inertingTheInformation(telegramUserID, "Email", (str(command)).strip()):
                        
                        KeyBoardMaker(update, CallbackContext ,[ KeyboardButton("Yes/አዎ"), KeyboardButton("No/አይ")] , "Are You Sure Do You Want To Contunue?")   
                    
                    else:
                        print("Vlaue can't be inserted ################ code 450782")


                 # email
            elif status == "7":
                repl =ReplyKeyboardRemove()
                if command == "Yes/አዎ":

                    menuKeyBorad = [ ["Show Jobs"], ["Profile"] ]
                    replymakrkups = ReplyKeyboardMarkup(menuKeyBorad, resize_keyboard=True)
                    if statusInformationUpater(str(update.effective_user.id)):
                        bot.send_message(update.effective_user.id, text="******* congratulation U have succesfully Registered To The bot choose how you want to proceed? ******", reply_markup = replymakrkups)
                    else:
                        print("Vlaue can't be udpated ################ code 49640")
                elif command == "No/አይ":
                    bot.send_message(update.effective_user.id, text="Upload Your CV in file format (.docx, .doc, pdf)",reply_markup = repl)
                else:
                     bot.send_message(update.effective_user.id, text="Make Sure You upload the right file format",reply_markup = repl)
                    
                 # cv
            elif status == "8":
                pass # resume
            elif status == "9":
                pass #web link 


            # user is already in so check for what stage of infomation he is in 
        else:
            StartingRegistering(update,CallbackContext)
            

    


dispatcher.add_handler(CommandHandler("start", StartingRegistering))
dispatcher.add_handler(MessageHandler(Filters.text,textCommandsHandler))
dispatcher.add_handler( MessageHandler(Filters.contact, PhoneNumberFetcherFromaAuser))
dispatcher.add_handler(MessageHandler(Filters.location, locationAndUserNameHandler))
dispatcher.add_handler(MessageHandler(Filters.document, documnetHandler))



# PORT = int(os.environ.get('PORT', '443'))
# HOOK_URL = 'YOUR-CODECAPSULES-URL-HERE' + '/' + key_token
# updater.start_webhook(listen='0.0.0.0', port=PORT, url_path=key_token, webhook_url=HOOK_URL)
# updater.idle()

updater.start_polling()
updater.idle()



# after rquest for basic infn staring from name