# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:59:29 2025

@author: admin.emo
"""

import os
from together import Together
api_key = "6d63b30d07cd19e252baf2dfafad9d5880440d6e9889a8a4497f3a08aef6d15c"
client = Together(api_key=api_key)
file_resp = client.files.upload(file="datos.jsonl", check=True)

print(file_resp.model_dump())