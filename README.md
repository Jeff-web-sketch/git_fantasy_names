# Update 1.2.0
fix misspeling of return_total_generated_names()<br>
add the length parameter to MakeNames(), you can now make names longer (some categories may not work well with this)<br>
added a new sample. Use the old=True parameter for the old one<br>
get_new_names() now retruns a list, the new names and the amount<br>
add duplicate detection in MakeNames()
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
