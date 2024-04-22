from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text


def read_sql_querry(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows



prompt = [
    """
    You are an expert in converting english questions to SQL code!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION \n\n
    For example\n Example 1 - How many entries of records are present ?, the SQL command will be 
    something like this SELECT COUNT(*) FROM STUDENT; 
    Also the SQL code should not have ''' in the beginning or end of the sql word in output
    \n Example 2 - Tell me all the student studying in Data Science class ?, the SQL command will be 
    something like this SELECT * FROM STUDENT where CLASS="Data Science"; 
    Also the SQL code should not have ''' in the beginning or end of the sql word in output
    """
]
    
    
    
st.set_page_config("I can retrieve data from SQL querry")
st.header("Gemini App to Retrieve SQL data")

question = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response = read_sql_querry(response, "student.db")
    st.subheader("The Response is ")
    for row in response:
        st.header(row)
