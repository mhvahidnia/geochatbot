import os
from typing import Dict, Optional

from requests import ConnectionError, HTTPError, Timeout, TooManyRedirects

owm_api_key = os.getenv("OWM_KEY", "")  # API key
#owm_api_key= os.environ.get('AG_API_KEY')
print(owm_api_key)
from pyowm.owm import OWM
owm = OWM(owm_api_key)
reg = owm.city_id_registry()
print(reg)
