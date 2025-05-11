from openai import OpenAI
from dotenv import load_dotenv

from rag_enum import Models

from .aya_model import AyaModel
from .openai_model import OpenAIModel

class ConversationManager():
    __available_models = {
        Models.OPENAI: OpenAIModel, 
        Models.AYA: AyaModel
    }
    __moderation_model_name = None
    __moderator_client = None 
    __model = None

    def __init__(self, model_name):
        self.__load_moderator()
        self.__model = self.__available_models.get(model_name)()

    def moderation(self, question):
        def get_flag(moderation_response):
            return moderation_response.results[0].flagged

        moderation_response = self.__moderator_client.moderations.create(model=self.__moderation_model_name, input=question)
        return get_flag(moderation_response)

    def generate_answer(self, question, chunks=''):
        ctx = ''

        if chunks:
            ctx = '\n\n'.join(
                f'--------- CONTEXT {i + 1} ---------\n-- EUREKA_FILE: {chunk[0].metadata.get('filename')} --\n{chunk[0].page_content}'
                for i, chunk in enumerate(chunks)
            )
        
        print(ctx)
        
        return self.__model.generate_answer(question, ctx)

    def __load_moderator(self):
        load_dotenv()
        self.__moderation_model_name = 'omni-moderation-latest'
        self.__moderator_client = OpenAI()

