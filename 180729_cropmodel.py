#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 12:38:06 2018

@author: kameokashinichi
"""

#utilize crop model

import json
import requests
from urllib import request

url = "http://ec2-52-196-202-21.ap-northeast-1.compute.amazonaws.com/cropsim/v1.1/simulations"

payload = {
      "transplant_date": "2018-04-25",
      "crop_ident_ICASA": "RIC",
      "cultivar_name": 'koshihikari',
      "model": "simriw",
      "weather_file": "http://dev.listenfield.com:8080/weather/static/ex/20180830-054017-kziinh23.zip",
      "field_latitude": 35.706179,
      "field_longitude": 140.482362,
      "wait": "true",
      "model_params":
                {
      "tp_cool": "true"
      }
}

headers = {
'Content-Type': "application/json",
'Cache-Control': "no-cache",
'Postman-Token': "7f8b4590-5d03-4b6a-b4b8-189a0e188cde"
}

payload = json.dumps(payload)

r = requests.request('POST', url, data=payload, headers=headers)

print(r.text)

resjson = json.loads(r.text)

print(resjson['id'])

#request.urlretrieve()

"""
Url for the weather data in agrisasamoto 1980-2016 uploaded
"http://ec2-52-196-202-21.ap-northeast-1.compute.amazonaws.com/cropsim/uploads/2018-09-05T00-02-04-380Z4a7f56c80b29cecf/180905_sasa_wth.zip"
crop simulation ID -> "2018-09-05T00-03-52-210Z3704f4c48a9fcbf7"

Url for the weather data in agrisasamoto 2000, 2010 uploaded
"http://ec2-52-196-202-21.ap-northeast-1.compute.amazonaws.com/cropsim/uploads/2018-09-05T00-38-01-662Z73cfbe3a6cb3d927/YKSH.zip"
crop simulation ID -> "2018-09-05T00-42-13-754Zf80f69fe981c3af6"

Url for the weather data in agrisasamoto 1980, uploaded
"http://ec2-52-196-202-21.ap-northeast-1.compute.amazonaws.com/cropsim/uploads/2018-09-05T00-57-55-282Z87738be3070b892d/19808001.WTH.zip"
crop simulation ID -> "2018-09-05T00-59-30-494Zf63ea919416c4986"
"""








