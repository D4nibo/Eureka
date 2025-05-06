from langchain_text_splitters import RecursiveCharacterTextSplitter

class RecursiveTextChunker():
    __splitter = None 
    __chunk_size = 2000
    __chunk_overlap = 0
    __length_function = len

    def __init__(self):
        self.__splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.__chunk_size,
            chunk_overlap = self.__chunk_overlap,
            length_function = self.__length_function,
            is_separator_regex = True
        )

    def chunk(self, path_to_text):
        with open(path_to_text, 'r', encoding='utf-8') as file:
            txt_file = file.read()
            
        chunks = self.__splitter.split_text(txt_file)
        return self.__splitter.create_documents(chunks)