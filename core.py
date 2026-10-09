import json
import requests
from random import randint
import colorama

colorama.init(autoreset=True)

class NameGenerator:
    '''Generate fantasy names'''
    def __init__(self,local_path=None,url="https://raw.githubusercontent.com/jeff-web-sketch/git-fantasy-names-data/main/data.json"):
        self.total_generated_names=0
        self.output_list=[]
        self.all_categories=[]
        self.local_path=local_path
        self.url=url
        self._load_json()
        self.new_names="https://raw.githubusercontent.com/jeff-web-sketch/git-fantasy-names-data/main/new_names.data"
        
        
    def _pick(self, input_list: list):
        '''Pick a random item from a list'''
        return input_list[randint(0,len(input_list)-1)]
    
    def _load_json(self):
        '''Load the names data from url'''
        if self.local_path != None:
            try:
                self.json_data=json.loads(open(self.local_path,'r').read())
            except Exception as q:
                raise q
        else:
            try:
                self.json_data=(json.loads(requests.get(self.url).text))
            except Exception as e:
                raise Exception("Error 1: could not load json text from url:",e)
        return self.json_data
    
    def reload_json(self):
        self._load_json()
        
    def MakeNames(self, category: str, count=5, cleanoutput=False):
        '''Generate names'''
        if category not in self.get_available_categories():
            print(colorama.Fore.RED+"Error 2: Name not available")
            return
        self.output_list=[]
        for json_category, json_obj in self.json_data.items():
            if json_category == category:
                for i in range(count):
                    self.output_list.append(self._pick(list(json_obj["starts"]))+self._pick(list(json_obj["ends"])))
                    self.total_generated_names+=1
                if cleanoutput == True:
                    return ", ".join(self.output_list)
                else:
                    return self.output_list
            
    def get_available_categories(self):
        '''Get all available categories'''
        self.all_categories=[]
        for json_category, json_obj in self.json_data.items():
            self.all_categories.append(json_category)
        return self.all_categories
    
    def get_new_names(self):
        '''Returns the most recently added names from the url'''
        return json.loads(requests.get(self.new_names).text)
    
    def return_total_generated_names(self):
        '''Returns the number of names genereated in the current session'''
        return self.total_generated_names
        
    def sample(self):
        print("---Centaur names---")
        print(self.MakeNames("centaur", count=10, cleanoutput=True))
        print("---Artifact names---")
        print(self.MakeNames("artifact", count=10, cleanoutput=True))
        print("---Mermaid names---")
        print(self.MakeNames("mermaid", count=10, cleanoutput=True))
        print("---Total Geneated---")
        print(ng.return_total_geneated_names())

if __name__ == "__main__":
    ng=NameGenerator()
    ng.sample()
