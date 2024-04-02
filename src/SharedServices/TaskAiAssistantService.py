from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import SystemMessage
from src.config.configurations import OPENAI_API_KEY


chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.0,
    openai_api_key=OPENAI_API_KEY
)


class AIAssistantService:
    def __init__(self, userInput):
        self.input = userInput
        self.systemContext = "As an AI assistant, You should focused on Indian states, their diverse cultures, " \
                             "traditions, and historical landmarks. Equip it with extensive knowledge about regional " \
                             "cuisines, festivals, languages, and notable personalities from each state. Ensure it " \
                             "can provide informative and engaging discussions on these topics."
        self.prompt = self.setChatPrompt()
        self.llm = self.createChain()
        self.response = self.processInput()

    def setChatPrompt(self):
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessage(content=self.systemContext),
                HumanMessagePromptTemplate.from_template("{input}")
            ]
        )
        return prompt

    def createChain(self):
        # Create a chain that uses the defined LLM and memory to process user input and generate responses
        llm = LLMChain(llm=chat, prompt=self.prompt)
        return llm

    def processInput(self):
        # Process user input through the chain and generate a response
        try:
            result = self.llm.run(input=self.input)
        except Exception as e:
            print(f"Exception process_input: {e}")
            result = ""
        return result

