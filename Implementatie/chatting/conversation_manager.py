from openai import OpenAI
from dotenv import load_dotenv
from .aya_model_encap import AyaModel
from .openai_model_encap import OpenAIModel

class ConversationManager():
    __moderation_model_name = None
    __moderator_client = None 
    __chat_model_encap = None

    def __init__(self, chat_model_encap = OpenAIModel()):
        self.__load_moderator()
        self.__chat_model_encap = chat_model_encap

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
        
        return self.__chat_model_encap.generate_answer(question, ctx)

    def __load_moderator(self):
        load_dotenv()
        self.__moderation_model_name = 'omni-moderation-latest'
        self.__moderator_client = OpenAI()

