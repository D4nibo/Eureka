from langchain_community.llms.gpt4all import GPT4All
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer

class AyaModel():
    __huggingface_repo_id = 'QuantFactory/aya-23-8B-GGUF'
    __hugging_face_filename = 'aya-23-8B.Q4_0.gguf'
    __original_model_name = 'CohereLabs/aya-23-8B'
    __chat_model = None

    def __init__(self):
        self.__load_chat_model()

    def generate_answer(self, question, ctx=''):
        tokenizer = AutoTokenizer.from_pretrained(self.__original_model_name)
        system_directives = (
            'Jij bent Eureka, de vriendelijke virtuele assistent van HOGENT die studenten helpt bij het beantwoorden van vakgerelateerde vragen. '
            'Beantwoord de gegeven ENKEL gebruikmakend van de meegeleverde context.\n\n'

            'Beantwoord in dezelfde taal als de vraag\n'
            'Indien de context GEEN correlatie heeft met de vraag, stel op een vriendelijke manier voor om de vraag anders te formuleren '
            ' of contact op te nemen met een docent.\n'
            'Indien de context WEL correlatie heeft met de vraag, formuleer een beknopt antwoord - max. 100 woorden -, vriendelijk en helder. Verwijs naar '
            'de informatiebron dat je gebruikt hebt (aangeduid na "EUREKA_FILE")'
        )

        user_message = (
            f'Question: {question.strip()}\n'
            f'Context:\n {ctx.strip()}\n'
        )
        
        messages = [
            {'role': 'system', 'content': system_directives},
            {'role': 'user', 'content': user_message}
        ]

        prompt = f'{tokenizer.apply_chat_template(messages, tokenize=False, return_tensors="pt")}<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>'
        
        print(f'MODEL MESSAGE: PROMPT IS - {prompt}')

        return self.__chat_model.invoke(prompt)
    
    def __load_chat_model(self):
        path = hf_hub_download(repo_id = self.__huggingface_repo_id, filename = self.__hugging_face_filename)
        self.__chat_model = GPT4All(
            model=path, 
            device = 'cpu', 
            n_threads = 10, 
            allow_download = False, 
            verbose=True,
            n_predict = 1000)

    