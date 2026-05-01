import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_classic.agents import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load env if available
load_dotenv()

st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 LangChain: Chat with SQL DB")

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_opt=['Use SQLite 3 Database - Student.db', "Connect to your SQL database"]

selected_opt=st.sidebar.radio(label='Choose the DB which you want to chat',options=radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide MySQL Host")
    mysql_user=st.sidebar.text_input("MYSQL User")
    mysql_password=st.sidebar.text_input("MYSQL password",type="password")
    mysql_db=st.sidebar.text_input("MySQL database")
else:
    db_uri=LOCALDB

api_key=st.sidebar.text_input(label='GROQ API Key',type='password')

if not db_uri:
    st.info('Pleae enter the database information and uri')

if not api_key:
    st.info("Please add the GROQ API key")

# LLM model
llm=ChatGroq(groq_api_key=api_key,model_name="llama-3.3-70b-versatile",streaming=True)

@st.cache_resource(ttl=7200)
def configure_db(db_uri, mysql_host=None, mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
        db_file_path=(Path(__file__).parent/'student.db').absolute()
        print(db_file_path)
        creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri==MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)

## toolkit
toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder='Ask anything from the database')

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)