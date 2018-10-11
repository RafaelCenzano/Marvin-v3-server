from requests import get
from marvin.essentials import speak


#########################
# File to hold Api work #
#########################


class ApiService():
    def __init__(self, speak_type):
        self.speak_type = speak_type

    def tacoFullRand(self):
        url = 'http://taco-randomizer.herokuapp.com/random/?full-taco=true'
        self.requested_taco = get(url)
        title = self.requested_taco.json()['name']
        print('Got Taco recipe for ' + title)
        spliting = title.split(" ")
        title_with_under_scores = ("_").join(spliting)
        self.taco_txt = (str(title_with_under_scores) + '.txt')
        print(title, file=open(self.taco_txt, 'w'))

    def tacoRandRand(self):
        url = 'http://taco-randomizer.herokuapp.com/random/'
        self.requested_taco = get(url)

    def dataTaco(self):
        try:
            instructions = self.requested_taco.json()['recipe']
            print('\n\nInstructions:\n' + instructions, file=open(self.taco_txt + '.txt', 'a'))
        except:
            print('\n\nInstructions:\nNo recipe for this section', file=open(self.taco_txt + '.txt', 'a'))

        if self.requested_taco.json()['shell_url'] is not None:
            shell_instructions = self.requested_taco.json()['shell']['recipe']
            print('\n\nShell Instructions:\n' + shell_instructions, file=open(self.taco_txt + '.txt', 'a'))

        if self.requested_taco.json()['base_layer_url'] is not None:
            base_layer_instructions = self.requested_taco.json()['base_layer']['recipe']
            print('\n\nBase Layer Instructions:\n' + base_layer_instructions, file=open(self.taco_txt + '.txt', 'a'))

        if self.requested_taco.json()['seasoning_url'] is not None:
            season_instructions = self.requested_taco.json()['seasoning']['recipe']
            print('\n\nSeasoning Instructions:\n' + season_instructions, file=open(self.taco_txt + '.txt', 'a'))

        if self.requested_taco.json()['condiment_url'] is not None:
            condiment_instructions = self.requested_taco.json()['condiment']['recipe']
            print('\n\nCondiment Instructions:\n' + condiment_instructions, file=open(self.taco_txt + '.txt', 'a'))

        if self.requested_taco.json()['mixin_url'] is not None:
            mixin_instructions = self.requested_taco.json()['mixin']['recipe']
            print('\n\nMixin Instructions:\n' + mixin_instructions, file=open(self.taco_txt + '.txt', 'a'))

        print('Full Recipe put into file called ' + self.taco_txt)
        speak('Opening the full taco recipe for you', self.speak_type)