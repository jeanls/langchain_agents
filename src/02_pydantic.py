from typing import List
from pydantic import BaseModel, Field #Importação atualizada
from typing import Optional
from enum import Enum
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from src.util.utils import get_model_4

load_dotenv()

chat = ChatOpenAI(model=get_model_4())

class Person:
    def __init__(self, name: str, age: int, weight: float) -> None:
        self.name = name
        self.age = age
        self.weight = weight

# Class withou pydantic
person1 = Person(name='Jean', age=30, weight=76)
print(person1)

# Class with pydantic
class PersonEnhanced(BaseModel):
    name: str
    age: int
    weight: float

person2 = PersonEnhanced(name='Jean Leal', age=30, weight=76)
print(person2)

class Team(BaseModel):
    employeers: List[PersonEnhanced]

print(Team(employeers=[PersonEnhanced(name='Jean Leal', age=30, weight=76)]))

class UnidadeEnum(str, Enum):
    celsius = 'celsius'
    fahrenheit = 'fahrenheit'

class ObterTemperaturaAtual(BaseModel):
    """Obtém a temperatura atual de uma determinada localidade"""
    local: str = Field(description='O nome da cidade', examples=['São Paulo', 'Porto Alegre'])
    unidade: Optional[UnidadeEnum]

tool_temperatura = convert_to_openai_function(ObterTemperaturaAtual)
print(tool_temperatura)

resposta = chat.invoke('Qual a temperatura da cidade de porto alegre?', functions=[tool_temperatura])
print(resposta)