import pandas as pd
import pymongo
from pymongo import MongoClient
import csv
from datetime import datetime
from pymongo import MongoClient
import streamlit as st


client = "mongodb://localhost:27017/"
# Opening the mongo client that is given
client = MongoClient(client)
db = client["com_vtx"]
asset_collection = db["Asset"]
unique_suppliers = df['supplier'].unique().tolist()
supplier = st.selectbox("Which supplier do you want asset info for?", unique_suppliers)

streamlit run asset_test.py []
