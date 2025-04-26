from .markdown_extractor import MarkdownExtractor
from .markdown_chunker import MarkdownChunker
      
class TextProcessor:
    __extraction_strategy = None
    __chunking_strategy = None

    def __init__(self, extraction_strategy = MarkdownExtractor(), chunking_strategy = MarkdownChunker()):
        self.__extraction_strategy = extraction_strategy
        self.__chunking_strategy = chunking_strategy

    def extract_from(self, path):
        path_to_temp = self.__extraction_strategy.extract(path)
        chunks = self.__chunking_strategy.chunk(path_to_temp)
        return chunks 