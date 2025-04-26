import os
import logging

from chatting import ConversationManager
from text_processing import TextProcessor
from storage import Embedder

class RagFacade:
    __text_processor = None 
    __embedder = None
    __conversation_manager = None 

    def __init__(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M%S'
        )
        
        self.__init_text_processor()
        self.__init_embedder()
        self.__init_conversation_manager()

    def insert_file(self, path, course):
        logging.info('File insertion will take place in a moment')
        logging.info('Extracting chunks from file...')
        chunks = self.__text_processor.extract_from(path)
        filename = os.path.basename(path)
        logging.debug(filename)
        logging.info('Embedding chunks...')
        self.__embedder.embed(chunks, course, filename)
        logging.info('File has been inserted !')

    def ask(self, question, course):
        answ = None 
        logging.info('Question will be answered in a moment')
        logging.info('Question\'s content is being scanned for inadequate content...')
        flag_raised = self.__conversation_manager.moderation(question)
        
        if flag_raised: answ = 'Helaas, kan ik je daarmee niet helpen.'
        else:
            logging.info('Question is being answered...')
            chunks = self.__embedder.query(question, course)
            answ = self.__conversation_manager.generate_answer(question, chunks)

        logging.info('Answer has been generated !')
        return answ
    
    def __init_text_processor(self):
        logging.info('Initializing text processor...')
        self.__text_processor = TextProcessor()

    def __init_embedder(self):
        logging.info('Initializing embedder...')
        self.__embedder = Embedder()

    def __init_conversation_manager(self):
        logging.info('Initializing conversation manager...')
        self.__conversation_manager = ConversationManager()
    