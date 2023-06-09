import json

profanity_list = []


with open('profanity_filter/profanity.txt', encoding='utf-8') as data:
    for line in data:
        word = line.lower().split('\n')[0]
        if word != '':
            profanity_list.append(word)


with open('profanity_filter/profanity.json', 'w', encoding='utf-8') as file:
    json.dump(profanity_list, file)
