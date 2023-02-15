from datetime import datetime
from enum import Enum
import enum
from typing import Dict, List

from setuptools import Command

from hebsafeharbor import HebSafeHarbor
from hebsafeharbor.manager_heb import HebrewAnonymizerManager
import hebsafeharbor
from tests.evaluation_texts import texts_1

class CommandLineTest():
    
    def __init__(self) -> None:
        pass

    def test_run_time(self):
        """ Testing run time in old and new structure, 'hebsafeharbor' vs. 'hebrew_anonymizer'
        """
        
        # Testing 'hebsafeharbor'
        _start=datetime.now()
        _dict= [{"id":str(index), "text": _text} for index, _text in  enumerate(texts_1) ]
        hsh=HebSafeHarbor()
        hsh_results=hsh(_dict)
        run_time_1=(datetime.now()-_start).seconds

        # Testing 'hebrew_anoymizer'
        _start=datetime.now()
        heb_anony=HebrewAnonymizerManager()
        _results=[]
        for index, _text in enumerate(texts_1):
            _results.append(heb_anony(_text))
        run_time_2=(datetime.now()-_start).seconds

        print(f"Run time 'hebsafeharbor': {run_time_1} 'hebrew_anonymizer': {run_time_2}")
        return
    
    def test_long_texts(self, number_of_sentences:int):
        print(f"Long text test for {number_of_sentences} sentences")
        with open("tests\long_text.txt", "r", encoding="UTF-8") as _f:
            _text=_f.readlines()        
        print(f"Total {len(_text)} sentneces, picking top {number_of_sentences}")
        _text=[_t for _t in _text if _t!="\n"]
        print(f"Total {len(_text)} sentneces, after removing empty ones")
        # Take top n sentences
        _text=_text[:number_of_sentences]
        _text=" ".join([_t.replace("\n", "") for _t in _text])
        heb_anony=HebrewAnonymizerManager()
        result=heb_anony(_text)
        print(result)

        return 

    def test_special_character(self):
        """
        Test text with special charactes: '\n', '\r', HTML tags, etc.
        """
        pass


if __name__ == '__main__':
    #CommandLineTest().test_run_time()
    CommandLineTest().test_long_texts(number_of_sentences=10)
    
