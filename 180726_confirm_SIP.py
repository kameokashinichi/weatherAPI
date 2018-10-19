#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:04:41 2018

@author: kameokashinichi
"""

import json
import requests


url = 'http://dev.listenfield.com:3232/cropsim/v1.1/simulations'

payload = {
  "transplant_date": "2017-04-25",
  "crop_ident_ICASA": "RIC",
  "cultivar_name": "Koshihikari",
  "model": "simriw",
  "weather_file": "http://dev.listenfield.com:8080/weather/static/ex/" + kgenlist[-1] + '.zip',
  "field_latitude": 35.706179,
  "field_longitude": 140.482362,
  "wait": True,
}

jsondata = json.dumps(payload, ensure_ascii=True, separators=(',',':'))

headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "059b0079-7950-4e39-97ec-d767e2008ba0"
}

r = requests.request("POST", url, data=jsondata, headers=headers)

