import streamlit as st
import requests
import json
import time

text = " فضل المدرس عاى الطالب كبير جدا لا يجب نكرانه"
# result = search.find_similar(query_text=tweet ,top_n=5)
# for sentence in result:
#    print(sentence)

arab_eras = {'Before_Islam': 'قبل الإسلام', 'Veteran': 'المخضرمين', 'Abbasid': 'العباسي',
             'Umayyad': 'الأموي', 'Mamluk': 'المملوكي', 'Morocco_and_Andalusia': 'المغرب والأندلس',
             'Between_the_Two States': 'بين الدولتين', 'Fatimid': 'الفاطمي', 'Ayyubid': 'الأيوبي',
             'Hadith': 'الحديث', 'Islamic': 'الإسلامي', 'Ottoman': 'العثماني'}

arab_eras_inv = {v: k for k, v in arab_eras.items()}

st.set_page_config(layout="wide")

st.header('Eqtibas :sunglasses:')

with_diacritics = st.selectbox(
    "هل تريد الشعر بالتشكيل؟ ",
    ("نعم", "لا"),
)

text = st.text_area(" :) اكتب ما يدور في بالك")

eras = list(arab_eras.keys())

url = "http://35.154.173.90/ai"
headers = {
  'Content-Type': 'application/json'
}


if st.button("Process Text"):
    # process text and display output
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(list(arab_eras.values()))
    tabs = [tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12]
    if with_diacritics == 'نعم':
        payload = {"input_quote": f"{text}", "diacritics": "yes", "embedding_quotes_number": 3,
                   "keyword_quotes_number": 4}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        eras_poem = response.json()
    else:
        payload = {"input_quote": f"{text}", "diacritics": "no", "embedding_quotes_number": 3,
                   "keyword_quotes_number": 4}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        eras_poem = response.json()

    for tab, era in zip(tabs, eras_poem.keys()):
        with tab:
            with st.spinner(text="In progress..."):
                eras_poem[era].reverse()
                for result in eras_poem[era]:
                    st.markdown(f"> {result}")
