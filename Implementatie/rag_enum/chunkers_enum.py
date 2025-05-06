from enum import Enum

class Chunkers(Enum):
    CHARACTER_TEXT = 'character_text_chunker'
    RECURSIVE_TEXT = 'recursive_text_chunker'
    MARKDOWN = 'markdown_chunker'