from langchain_community.document_loaders import PyMuPDFLoader
import os

class TextExtractor:
    __TXT_LOCATION = './text_processing/temp' 
    __TXT_NAME = 'conversion_res_temp'

        
    def extract(self, path):
        loader = PyMuPDFLoader(
            path,
            mode='single', # Extracts entire document
            extract_tables="markdown",
        )  

        doc_obj = loader.load()
        text = doc_obj[0].page_content

        temp_path = f'{os.path.join(self.__TXT_LOCATION, self.__TXT_NAME)}.txt'
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(text)

        return temp_path
