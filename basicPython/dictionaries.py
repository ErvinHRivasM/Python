#In this section, we programing a simple game
from os import times

def run():
   my_dictionaries = { 
       'key1': 1,
       'key2': 2,
       'key3': 3,
   }
   
   population_countries = {
       'Argentina': 449938712,
       'Brasil': 210147125,
       'Colombia': 50372424,
   }

   for country in population_countries.keys():
       print("Keys of Dictionary: "+str(country))
   
   for country2 in population_countries.values():
       print("Values of Dictionary: "+str(country))

   for keys_,values_ in population_countries.items():
       print(keys_+" Have : "+str(values_)+" populations" )



if __name__ == '__main__':
    run()