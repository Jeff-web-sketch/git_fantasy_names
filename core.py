import json
import requests
from random import randint
import colorama
import ast

colorama.init(autoreset=True)

class NameGenerator:
    '''Generate fantasy names'''
    def __init__(self,local_path=None,local_new_names_path=None,url="https://raw.githubusercontent.com/jeff-web-sketch/git-fantasy-names-data/main/data.json"):
        self.total_generated_names=0
        self.output_list=[]
        self.all_categories=[]
        self.local_path=local_path
        self.url=url
        self._load_json()
        self.local_new_names_path=local_new_names_path
        if local_new_names_path == None:
            self.new_names_url="https://raw.githubusercontent.com/jeff-web-sketch/git-fantasy-names-data/main/new_names.data"
        else:
            self.new_names_url=local_new_names_path
        
        
    def _pick(self, input_list: list):
        '''Pick a random item from a list'''
        return input_list[randint(0,len(input_list)-1)]
    
    def _load_json(self):
        '''Load the names data from url or file'''
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
        '''Call the loading script'''
        self._load_json()
    
    def MakeNames(self, category: str, count=5,length=1,cleanoutput=False):
        '''Generate names'''
        if category not in self.get_available_categories():
            print(colorama.Fore.RED+"Error 2: Name not available")
            return
        self.output_list=[]
        for json_category, json_obj in self.json_data.items():
            if json_category == category:
                for i in range(count):
                    output=(self._pick(list(json_obj["starts"])))
                    for i in range(length):
                        output+=(self._pick(list(json_obj["ends"])))
                        while True:
                            if output in self.output_list:
                                output=(self._pick(list(json_obj["starts"])))
                                for i in range(length):
                                    output+=(self._pick(list(json_obj["ends"])))
                            else:
                                break
                    else:
                        self.output_list.append(output)
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
        if self.local_new_names_path == None:
            new_names=requests.get(self.new_names_url).text
        else:
            new_names=ast.literal_eval(open(self.new_names_url).read())
        return [new_names,len(new_names)]
    
    def return_total_generated_names(self):
        '''Returns the number of names genereated in the current session'''
        return self.total_generated_names
    
    def show_url_or_path(self):
        if self.local_path==None:
            return self.url
        else:
            return self.local_path
    
    
    def sample(self,old=False):
        if old:
            print("---Centaur names---")
            print(self.MakeNames("centaur", count=10, cleanoutput=True))
            print("---Artifact names---")
            print(self.MakeNames("artifact", count=10, cleanoutput=True))
            print("---Mermaid names---")
            print(self.MakeNames("mermaid", count=10, cleanoutput=True))
            print("---Total Geneated---")
            print(ng.return_total_generated_names())
        else:
            character=self._pick(self.get_available_categories())
            name=self.MakeNames(character)
            print("Name:",name[randint(0,4)])
            print("Age:",randint(1, 100))
            print("Type:",character)
            print("Strength:",randint(1,20))
            print("Knowledge:",randint(1,20))
        

if __name__ == "__main__":
    ng=NameGenerator()
    ng.sample()
