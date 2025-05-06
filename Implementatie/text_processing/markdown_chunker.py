from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

class MarkdownChunker:
    __splitter = None 
    _sub_splitter = None

    def __init__(self):
        chunk_size = 2000
        chunk_overlap = 0
        length_function = len
        headers_to_split_on = [
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3"),
            ("####", "h4"),
        ]

        self.__splitter =  MarkdownHeaderTextSplitter(headers_to_split_on)
        self.__sub_splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            length_function = length_function,
            is_separator_regex = True
        )

    def chunk(self, path_to_markdown):
        with open(path_to_markdown, 'r', encoding='utf-8') as file:
            md_file = file.read()
        
        chunks = self.__splitter.split_text(md_file)
        
        # The chunks created by the MarkdownHeaderTextSplitter could still be
        # too big for the context of the LLM. Therefor, we let it go through
        # RecursiveCharacterTextSplitter to ensure its length
        return self.__sub_splitter.split_documents(chunks)
        