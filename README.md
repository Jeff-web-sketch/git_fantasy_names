# Update 1.1.6
fix misspeling of return_total_generated_names
# Usage
from git_fantasy_names import *<br>
ng=NameGenerator()<br>
ng.sample()<br>
<br>
or<br>
<br>
from git_fantasy_names import *<br>
ng=NameGenerator()<br>
print(ng.MakeNames(ng.get_available_categories()[3],count=10,cleanoutput=True))
print(ng.return_total_generated_names())
# Instalation
pip install git-fantasy-names
# Error explinations
#Error 1: couldn't load the json data from the url<br>
#Error 2: name isn't in the list of generators
