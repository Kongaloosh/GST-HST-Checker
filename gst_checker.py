import requests
from bs4 import BeautifulSoup
from time import sleep
import json
# from mechanize import Browser
REQUEST_DATE = '2018-01-01'

dummy_data = json.dumps([{
        'businessNumber': 863961264,
        'businessName': 'Kearney Management Consulting Ltd'
}])


def check_gst(data):
        data = json.loads(data)
        results = []
        for entry in data:
                session = requests.Session()    # we use a session so that the gov site recognizes us as agreeing to terms
                # tell the gov't that we agree to their terms
                response = session.post(
                        'https://www.businessregistration-inscriptionentreprise.gc.ca/ebci/brom/registry/registryservlet',
                        data={'iagree':'yes'}
                )
                # make the form with the entry that we're going to be checking
                payload = {
                        'businessNumber': entry['businessNumber'],
                        'businessName': entry['businessName'],
                        'requestDate': REQUEST_DATE
                }
                # submit the form with the data we care about
                response = session.post(
                        url='https://www.businessregistration-inscriptionentreprise.gc.ca/ebci/brom/registry/registryservlet/ebci/brom/registry/registryPromptSubmit.action',
                        data=payload)
                # parse the html returned
                soup = BeautifulSoup(response.content, 'html.parser')
                # check to see if the GST/HST number is registered, and note it
                entry['isCorrect'] = 'GST/HST number registered on this transaction date.' in soup.text
                results.append(entry)
                sleep(0.1)      # sleep for 0.1 seconds to make sure the government doesn't get mad
        return json.dumps(data)     # return the data

if __name__ == '__main__':
        print(check_gst(dummy_data))
