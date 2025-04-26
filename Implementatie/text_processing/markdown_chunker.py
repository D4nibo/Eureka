from langchain_text_splitters import MarkdownHeaderTextSplitter

class MarkdownChunker:
    __splitter = None 

    def __init__(self):
        headers_to_split_on = [
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3"),
            ("####", "h4"),
        ]

        self.__splitter =  MarkdownHeaderTextSplitter(headers_to_split_on)
        

    def chunk(self, path_to_markdown):
        with open(path_to_markdown, 'r', encoding='utf-8') as file:
            md_file = file.read()
            
        return self.__splitter.split_text(md_file)
        