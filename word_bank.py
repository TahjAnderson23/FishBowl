import requests 

def get_animal_words():
    reponse = requests.get("https://random-word-form.herokuapp.com/random/animal")
    print(reponse.json())

#get_animal_words()
