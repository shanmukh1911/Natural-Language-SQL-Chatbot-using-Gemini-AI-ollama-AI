# # from langchain_community.utilities import SQLDatabase

# # def connectDatabase(username, port, host, password, database):
# #     mysql_uri = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
# #     global db
# #     db = SQLDatabase.from_uri(mysql_uri)

# # # Replace these values with your actual database credentials
# # username = "root"
# # port = "3306"
# # host = "127.0.0.1"
# # password = ""
# # database = ""

# # connectDatabase(username, port, host, password, database)

# # if 'db' in globals() and db:
# #     print("Database connected successfully")
# # else:
# #     print("Failed to connect to the database")

# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="newname"
# )
# mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for i in mycursor:
#     print(i)


import google.generativeai as genai

# Configure the API key
genai.configure(api_key="")

# List available models
models = genai.list_models()
for model in models:
    print(model)
