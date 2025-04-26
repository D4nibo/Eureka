from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import save_output
from marker.config.parser import ConfigParser
import os

class MarkdownExtractor:
    __converter = None
    __MD_LOCATION = './text_processing/temp'
    __MD_NAME = 'conversion_res_temp'

    def __init__(self):
        self.__init_extractor()
        
    def extract(self, path):
        # A FileNotFoundError could be thrown from here
        # TODO: Decide how to handle the error
        rendered = self.__converter(path)
        save_output(rendered, self.__MD_LOCATION, self.__MD_NAME)
        return os.path.join(self.__MD_LOCATION, f'{self.__MD_NAME}.md')

    def __init_extractor(self):
        config = { 
            'output_format': 'markdown',
            'disable_image_extraction': True,
        }
        config_parser = ConfigParser(config)

        self.__converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config=config_parser.generate_config_dict(),
        )