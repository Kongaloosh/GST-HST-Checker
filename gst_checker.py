import requests
from bs4 import BeautifulSoup
from time import sleep
import re
import urllib3
import ssl
import certifi
# from mechanize import Browser
REQUEST_DATE = '2018-01-01'
# urllib3.contrib.pyopenssl.inject_into_urllib3()
while True:
        session = requests.Session()    # we use a session so that the gov site recognizes us as agreeing to terms
        response = session.post('https://www.businessregistration-inscriptionentreprise.gc.ca/ebci/brom/registry/registryservlet', data={'iagree':'yes'})
        #regForm.
        payload = {     # registryPromptSubmit
                'businessNumber': 863961264,
                'businessName': 'Kearney Management Consulting Ltd',
                'requestDate': REQUEST_DATE
        }
        response = session.post(url='https://www.businessregistration-inscriptionentreprise.gc.ca/ebci/brom/registry/registryservlet/ebci/brom/registry/registryPromptSubmit.action',data=payload)
        f = open('test.html', 'w')
        f.write(str(response.content))
        soup = BeautifulSoup(response.content, 'html.parser')
        print('GST/HST number registered on this transaction date.' in soup.text)
        sleep(0.1)
