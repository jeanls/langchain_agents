from pydantic import BaseModel, Field

class Acontecimento(BaseModel):
    """Informação soobre um acontecimento"""

    data: str = Field(description='Data do acontecimento no formato YYYY-MM-DD')
    acontecimento: str = Field(description='Acontecimento extraído do texto')

class ListaAcontecimento(BaseModel):
    """Acontecimentos para extração"""

    acontecimentos: list[Acontecimento] = Field(description='Lista de acontecimentos presentes no texto informado')

class BlogPost(BaseModel):
    """Blog post information"""

    title: str = Field(description='Title of the blog post')
    autor: str = Field(description='author of the blog post')
    date: str = Field(description='Date of the blog post in YYYY-MM-DD format')

class BlogSite(BaseModel):
    """Blog site information"""

    posts: list[BlogPost] = Field(description='List of blog posts')