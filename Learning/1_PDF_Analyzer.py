'''Python AI&ML Journey Projekt-1, i will try to analyse certain aspects of an PDF'''
import pandas as pd
import streamlit as st

import pdfplumber
import textstat
st.header(":blue[PDF] Analyzer")
data = st.file_uploader(label='Upload your Pdf here', type=['pdf'])

if data is None:
    st.warning("Please Upload an PDF !")
    st.stop()


with pdfplumber.open(data) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

if not text or text.strip() == "":
 st.warning("The PDF was empty or somthing did not work !")
 st.stop()

lenght_text = len(text)
number_of_whitspaces = text.count(" ")
characters_no_whitspaces = lenght_text - number_of_whitspaces

st.write(f"The number of Characters is: {lenght_text}, {number_of_whitspaces} of them are whitespaces")

df = pd.DataFrame({ 'NumberofWhitespace': [number_of_whitspaces], 'CharactersNoWhitespace': [characters_no_whitspaces]})
st.table(df)

st.bar_chart(df, horizontal=True)

st.write("""
         # Readabillity Stats
         **Here i will display Readabillity stats** """)

score = textstat.flesch_reading_ease(text)
grade = textstat.flesch_kincaid_grade(text)
class_level = textstat.text_standard(text)
grade_level_to_understand = textstat.gunning_fog(text)

score = int(score)
grade = int(grade)

df_levels = pd.DataFrame({'Textscore(0/100)': [score]})

st.bar_chart(df_levels)

st.subheader(":red[Grade Levels for this text]")

st.markdown(f"""
             **The text looks like its from: {class_level} level** ,
             **To understand the text you shouldt atleast be in: {grade_level_to_understand:.0f} grade !**
            """)

