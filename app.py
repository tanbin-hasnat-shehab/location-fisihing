import streamlit as st
import json
import requests



def main():

	st.title('this is it')
	html_string = "this is"

	st.markdown(html_string, unsafe_allow_html=True)
	res=requests.get('http://ipinfo.io/')
	data=res.json()
	print(data)
	st.write(data)



if __name__ == "__main__":
    main()
