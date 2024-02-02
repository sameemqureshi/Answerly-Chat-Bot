from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
 
import streamlit as str
str.set_page_config(page_title="Answerly Chatbot")
str.header("Answerly using Langchain")
from dotenv import load_dotenv
load_dotenv()
import os
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response = llm(question)
    return response






input=str.text_input("Input:",key='input')
response=get_openai_response(input)
submit=str.button("Ask me Anything")

if submit:
    str.subheader("The Response is:")
    str.write(response)

chat=ChatOpenAI(temperature=0.5)

# if 'flowmessages' not in str.session_state:
#     str.session_state['flowmessages']=[
#         SystemMessage(content="Yor are a comedian AI assitant")
#     ]

# ## Function to load OpenAI model and get respones

# def get_chatmodel_response(question):

#     str.session_state['flowmessages'].append(HumanMessage(content=question))
#     answer=chat(str.session_state['flowmessages'])
#     str.session_state['flowmessages'].append(AIMessage(content=answer.content))
#     return answer.content

# input=str.text_input("Input: ",key="input")
# response=get_chatmodel_response(input)

# submit=str.button("Ask the question")

# ## If ask button is clicked

# if submit:
#     str.subheader("The Response is")
#     str.write(response)

