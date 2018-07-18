
state = input("Enter a state name: ")

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                     'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                     'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

print(state_dictionary.get(state.capitalize(), 'Capital unknown'))
