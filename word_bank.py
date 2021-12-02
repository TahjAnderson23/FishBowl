import requests 


def get_animal_words():
    reponse = requests.get("https://random-word-form.herokuapp.com/random/animal")
    print(reponse.json()[0])

def get_words_like(key):
    response = requests.get("https://api.datamuse.com/words?ml="+key)
    word_list = []
    for i in range(len(response.json())):
        word_list.append(response.json()[i]['word'])
    return word_list
    
def get_words_rhyme(key):
    response = requests.get("https://api.datamuse.com/words?rel_rhy="+key)
    word_list = []
    for i in range(len(response.json())):
        word_list.append(response.json()[i]['word'])
    return word_list

bank = get_words_rhyme('apple')

print(bank)
#get_animal_words()
