# -*- coding: utf-8 -*-

from googletrans import Translator
# print(googletrans.LANGCODES)

def translation(text):



      translater=Translator()

      language=translater.detect(text)
      translate_text=translater.translate(text,src=str(language.lang),dest='en')

      return translate_text.text
def translationuz(text):



      translater=Translator()

      language=translater.detect(text)
      translate_text=translater.translate(text,src=str(language.lang),dest='uz')

      return translate_text.text
#pip install googletrans==3.1.0a0