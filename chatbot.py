from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model=OllamaLLM(model="llama3.1")

template =""" You are a helpful assistant that provides information about Comics(Marvel & DC). 

Question:{question}

Please do start with an answer with a comic joke related to the {question} 

Answer: 

"""
prompt=ChatPromptTemplate.from_template(template)

chain = prompt | model                                    

print(chain.invoke({"question: Who is Tony Stark"}))
