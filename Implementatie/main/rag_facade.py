import os
import logging
from dotenv import load_dotenv

from chatting import ConversationManager
from text_processing import TextProcessor
from storage import Embedder
from rag_enum import Extractors, Chunkers, Models

class RagFacade:
    __text_processor = None 
    __embedder = None
    __conversation_manager = None 

    def __init__(self, extractor = Extractors.TEXT, chunker = Chunkers.RECURSIVE_TEXT, model = Models.AYA, collection = 'vakken'):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M%S'
        )

        load_dotenv() 
        self.__init_text_processor(extractor, chunker)
        self.__init_embedder(collection)
        self.__init_conversation_manager(model)

    def insert_files(self):    
        drop_zone_path = './drop_zone'
        i = 0
        for dir in os.scandir(drop_zone_path):
            course_name = dir.name.replace('_', ' ')
            print(f'File insertions will start for {course_name}')

            for file in os.scandir(dir.path):
                print('LOOPING OVER FILE: ' + str(i))
                i += 1

                print(f'Extracting chunks from {file.name}')
                chunks = self.__text_processor.extract_from(file.path)

                print(f'Embedding chunks of {file.name}\n')
                self.__embedder.embed(chunks, course_name, file.name)
        
    def ask(self, question, course):
        print(course.value)
        answ = None 
        print('Question is being scanned for inadequate content...')
        flag_raised = self.__conversation_manager.moderation(question)
        
        if flag_raised: answ = 'Helaas, kan ik je daarmee niet helpen.'
        else:
            print('Question is being answered...')
            chunks = self.__embedder.query(question, course.value)
            answ = self.__conversation_manager.generate_answer(question, chunks)

        print('Answer has been generated !')
        return answ
    
    def __init_text_processor(self, extractor, chunker):
        print('Initializing text processor...')
        self.__text_processor = TextProcessor(extractor, chunker)

    def __init_embedder(self, collection):
        print('Initializing embedder...')
        self.__embedder = Embedder(collection)

    def __init_conversation_manager(self, model):
        print('Initializing conversation manager...')
        self.__conversation_manager = ConversationManager(model)
    