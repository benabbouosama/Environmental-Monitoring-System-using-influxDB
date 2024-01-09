# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:13:04 2024

@author: Oussama
"""

from dotenv import load_dotenv
from random import uniform
from time import sleep
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os

load_dotenv()
url = os.getenv('URL', None)
org = os.getenv('ORG', None)
token = os.getenv('TOKEN',None)
bucket = os.getenv('BUCKET', None)

locations = ["Fez", "Jeddah", "New York", "Sydney", "Tokyo" ]

with InfluxDBClient(url=url, token=token, org=org) as client:
    print(client.ping())
    with client.write_api(write_options=SYNCHRONOUS) as writer:
        while True:
            for location in locations:
                temp = uniform(20.5, 25.5)
                humidity = uniform(30.0, 50.0)
                pressure = uniform(950.0, 1050.0)
                p = Point("my_measurement").tag("location", location).field("temperature", temp).field("humidity", humidity).field("pressure", pressure)
                print(f"New measurement for {location}...")
                res = writer.write(bucket=bucket, org=org, record=p)
            sleep(5)
