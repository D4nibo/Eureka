from langchain_community.llms import GPT4All
from huggingface_hub import hf_hub_download

class AyaModelEncap():
    __huggingface_repo_id = 'QuantFactory/aya-23-8B-GGUF'
    __hugging_face_filename = 'aya-23-8B.Q4_0.gguf'
    __chat_model = None

    def __init__(self):
        self.__load_chat_model()

    def generate_answer(self, question, ctx=''):
        
        system_directives = (
            '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>\n'
            'Jij bent Eureka, de vriendelijke virtuele assistent van HOGENT die studenten helpt bij het beantwoorden van vakgerelateerde vragen. '
            'Beantwoord de gegeven vraag op basis van de meegeleverde context.\n\n'
            'Indien de context geen relevantie heeft met de vraag, laat dan beleefd weten dat je het antwoord niet kent.\n\n'
            'Indien de context wel relevante informatie bevat, formuleer dan een duidelijk antwoord en vermeld de bronnen '
            'die je uit de context hebt gebruikt om tot dat antwoord te komen.\n'
            '<|END_OF_TURN_TOKEN|>'
        )

        user_message = (
            '<|START_OF_TURN_TOKEN|><|USER_TOKEN|>\n'
            f'Vraag: {question.strip()}\n'
            f'Context:\n {ctx.strip()}\n'
            '<|END_OF_TURN_TOKEN|>'
        )

        
        prompt = (
            '<|BOS_TOKEN|>\n'
            f'{system_directives}'
            f'{user_message}'
            '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>'
        )

        print(prompt)
        
        return self.__chat_model.invoke(prompt)
    
    def __load_chat_model(self):
        path = hf_hub_download(repo_id = self.__huggingface_repo_id, filename = self.__hugging_face_filename)
        self.__chat_model = GPT4All(model=path, device = 'cpu', n_threads = 10, allow_download = False, verbose=True)

    