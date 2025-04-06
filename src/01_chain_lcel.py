from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.util.utils import get_model_4
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model=get_model_4())

prompt = ChatPromptTemplate.from_template('Crie uma frase sobre o seguinte: {assunto}.')

chain = prompt | model | StrOutputParser()

result = chain.invoke({'assunto': 'gatinhos'})

print(result)

