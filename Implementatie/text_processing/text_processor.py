from .text_extractor import TextExtractor
from .character_text_chunker import CharacterTextChunker
from .recursive_text_chunker import RecursiveTextChunker

from .markdown_extractor import MarkdownExtractor
from .markdown_chunker import MarkdownChunker

from rag_enum import Extractors, Chunkers

import os

class TextProcessor:
    __extraction_strategies = {
        Extractors.TEXT: TextExtractor,
        Extractors.MARKDOWN: MarkdownExtractor
    }

    __chunking_strategies = {
        Chunkers.CHARACTER_TEXT: CharacterTextChunker,
        Chunkers.RECURSIVE_TEXT: RecursiveTextChunker,
        Chunkers.MARKDOWN: MarkdownChunker
    }

    __extraction_strategy = None
    __chunking_strategy = None
    __temporary_file_path = './text_processing/temp'

    def __init__(self, extractor, chunker):
        self.__extraction_strategy = self.__extraction_strategies.get(extractor)()
        self.__chunking_strategy = self.__chunking_strategies.get(chunker)()

    def __empty_temp_dir(self):
        for e in os.scandir(self.__temporary_file_path):
            if e.is_file():
                os.remove(e.path)

    def extract_from(self, path):
        path_to_temp = self.__extraction_strategy.extract(path)
        chunks = self.__chunking_strategy.chunk(path_to_temp)
        self.__empty_temp_dir() # Empty any temporary files that an Extractor and a Chunker could have made
        return chunks 