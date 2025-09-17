from dotenv import load_dotenv
import os
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.chat_models import ChatOllama
# from langchain_groq import ChatGroq
import streamlit as st


# load_dotenv()
genai.configure(api_key="")



def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  # db_uri = "mysql+mysqlconnector://root:psswd@localhost:3306/newname"
  print(db_uri)
  return SQLDatabase.from_uri(db_uri)

def get_sql_chain(db):
  template = """

    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, write a SQL query as a normal text that would answer the user's question. Take the conversation history into account.
    
    <SCHEMA>{schema}</SCHEMA>
    
    Conversation History: {chat_history}
    
    Write only the SQL query as a normal text and nothing else. Do not wrap the SQL query in any other text, not even backticks.
    
    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;
    
    Your turn:
    
    Question: {question}
    SQL Query:
    """
    
  prompt = ChatPromptTemplate.from_template(template)
  
  # llm = ChatOpenAI(model="gpt-4-0125-preview")
  # llm = ChatGroq(model="mistral-large-latest", temperature=0)
  # llm = ChatOllama(model="llama3")
  # llm = ChatOllama(model="deepseek-r1")
  llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-001-tuning",temperature=0.5,api_key="")

  def get_schema(_):
    return db.get_table_info()

  
  return (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm
    | StrOutputParser()
  )
    
def get_response(user_query: str, db: SQLDatabase, chat_history: list):
  sql_chain = get_sql_chain(db)
  
  template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, question, sql query, and sql response, write a natural language response.
    <SCHEMA>{schema}</SCHEMA>

    Conversation History: {chat_history}
    SQL Query: <SQL>{query}</SQL>
    User question: {question}
    SQL Response: {response}"""
  
  prompt = ChatPromptTemplate.from_template(template)
  
  # llm = ChatOpenAI(model="gpt-4-0125-preview")
  # llm = ChatGroq(model="mistral-large-latest", temperature=0)
  # llm = ChatOllama(model="llama3")
  llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-001-tuning",temperature=0.5,api_key="")

#  gemini-1.5-pro-002  --> resource exhausted
  #gemini-1.5-flash-001-tuning -> perfect for only data related queries

  chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
      schema=lambda _: db.get_table_info(),
      response=lambda vars: db.run(vars["query"]),
    )
    | prompt
    | llm
    | StrOutputParser()
  )
  
  return chain.invoke({
    "question": user_query,
    "chat_history": chat_history,
  })
    
  
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm a analyst assistant. Ask me anything about your database."),
    ]

load_dotenv()

# def display_message(content, sender="AI"):
#     """Function to display messages with colored backgrounds."""
#     style = (
#         "background-color: #e3f2fd; padding: 10px; border-radius: 10px; font-family: Arial;"
#         if sender == "AI" else
#         "background-color: #fce4ec; padding: 10px; border-radius: 10px; font-family: Arial;"
#     )
#     st.markdown(f"<div style='{style}'>{content}</div>", unsafe_allow_html=True)


st.set_page_config(page_title="Chat with Datakrew's data", page_icon="💬")

st.title("💬 Chat with Datakrew's data")

with st.sidebar:
    st.subheader("⚙️ Settings")
    st.write("This is a simple chat application using MySQL. Connect to the database and start chatting.")
    
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="Admin1234", key="Password")
    st.text_input("Database", value="ev_fleet_health", key="Database")
    
    if st.button("Connect"):
        with st.spinner("🔗 Connecting to database..."):
            try:
              db = init_database(
                  st.session_state["User"],
                  st.session_state["Password"],
                  st.session_state["Host"],
                  st.session_state["Port"],
                  st.session_state["Database"]
              )
              st.session_state.db = db
              st.success("✅ Connected to database!")
            except Exception as e:
              st.error(f"❌ Failed to connect to database: {e}")
    
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)



user_query = st.chat_input("Type a message...")
if user_query is not None and user_query.strip() != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
        
    with st.chat_message("AI"):
        response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
        st.markdown(response)
        
    st.session_state.chat_history.append(AIMessage(content=response))

  