
import streamlit as st 

import requests
r=requests.get('http://get.geojs.io/v1/ip.json')
ipadd=r.json()['ip']
print(ipadd)
st.write(ipadd)
