from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings
from uuid import uuid4 
from pathlib import Path

class Embedder:
    __embedding_model = None
    __datastore = None
    __DB_PATH = './storage/db'

    def __init__(self, collection):
        Path(self.__DB_PATH).mkdir(parents=True, exist_ok=True)
        self.__init_datastore(collection)
        
    def embed(self, chunks, course, filename):
        for c in chunks:
            c.metadata['course'] = course 
            c.metadata['filename'] = filename
            c.id = str(uuid4())

        self.__datastore.add_documents(chunks)

    def query(self, question, course):
        return self.__datastore.similarity_search_with_score(
            question, 
            k = 2,
            filter = {'course': course}
        )

    def __init_datastore(self, collection):
        self.__embedding_model = HuggingFaceEmbeddings(model_name='BAAI/bge-m3')
        self.__datastore = Chroma(
            collection_name=collection,
            persist_directory = self.__DB_PATH,
            embedding_function=self.__embedding_model
        )
