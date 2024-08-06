from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

class ComicChatbot:
    def __init__(self):
        self.template= self.get_template()
        self.prompt=prompt=ChatPromptTemplate.from_template(self.template)
        self.model= OllamaLLM(model="llama3.1")
        self.chain= self.prompt | self.model


    def get_template(self):

        template =""" You are a helpful assistant that provides information about Comics(Marvel & DC). 

        Question:{question}

        Please do start with an answer with a comic joke related to the {question} 

        Answer: 

        """
        return template
    
    def get_response(self,memory,question):
        return self.chain.invoke({"memory":memory,"question":question})
        





