import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    #write the code here
     frenchtextdic = json.dumps(language_translator.translate(text=englishText, 
     model_id='en-fr').get_result())
     responce= json.loads(frenchtextdic)
     frenchText = responce["translations"][0]["translation"]
     print("frenchText ", frenchText)
     return frenchText




def frenchToEnglish(frenchText):
    #write the code here
    englishText = '';
    englishtextdic = json.dumps(language_translator.translate(text=frenchText, 
     model_id='fr-en').get_result())
    responce= json.loads(englishtextdic)
    englishText = responce["translations"][0]["translation"]
     
    print("englishText ", englishText)
    return englishText