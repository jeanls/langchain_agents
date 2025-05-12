from typing import List

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field #Importação atualizada
from typing import Optional
from enum import Enum
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from src.classes.classes_apoio import ListaAcontecimento, BlogSite
from src.util.utils import get_model_4

load_dotenv()

chat = ChatOpenAI(model=get_model_4())

texto = '''A Apple foi fundada em 1 de abril de 1976 por Steve Wozniak, Steve Jobs e Ronald Wayne 
com o nome de Apple Computers, na Califórnia. O nome foi escolhido por Jobs após a visita do pomar 
de maçãs da fazenda de Robert Friedland, também pelo fato do nome soar bem e ficar antes da Atari 
nas listas telefônicas.

O primeiro protótipo da empresa foi o Apple I que foi demonstrado na Homebrew Computer Club em 1975, 
as vendas começaram em julho de 1976 com o preço de US$ 666,66, aproximadamente 200 unidades foram 
vendidas,[21] em 1977 a empresa conseguiu o aporte de Mike Markkula e um empréstimo do Bank of America.'''

tool_acontecimentos = convert_to_openai_function(ListaAcontecimento)
print(tool_acontecimentos)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extraia as frases de acontecimento. Elas devem ser extraídas integralmente"),
    ("user", "{input}"),
])

chain = prompt | chat.bind(functions=[tool_acontecimentos], function_call={"name": "ListaAcontecimento"}) | JsonOutputFunctionsParser()

# result = chain.invoke({"input": texto})
# print(result)

url_blog = 'https://hub.asimov.academy/blog/'

### Extraindo informações da web

loader = WebBaseLoader(url_blog)
page = loader.load()
print(page)

tool_blog = convert_to_openai_function(BlogSite)
print(tool_blog)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Extraia da página todos os posts de blog com autor e data de publicação"),
    ("user", "{input}"),
])

chain = prompt | chat.bind(functions=[tool_blog], function_call={"name": "BlogSite"}) | JsonOutputFunctionsParser()
result = chain.invoke({"input": page})
print(result)