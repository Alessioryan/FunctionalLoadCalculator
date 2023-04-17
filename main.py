
import json

# Define vowel sequences
English = {
    "vowels": [['i', 'ɪ', 'eɪ', 'ɛ', 'æ', 'ɑ', 'ɔ', 'oʊ', 'ʊ', 'u', 'aɪ', 'aʊ', 'ɔɪ'], "V"]
}


# Import the file
def import_file(file_name):
    with open(file_name, 'r') as file:
        unprocessed_json = json.loads(file.read() )
    for key, value in unprocessed_json.items():
        unprocessed_json[key] = value.split()
    return unprocessed_json

# Neutralizes all the contrasts within the natural class.
# May be passed in as a list of contrasts to be neutralized.
# Each contrast will be replaced with the second item of the list, and the first list is what is neutralized
def neutralize(natural_class, mapping):
    new_mapping = {}
    for key, value in mapping.items():
        new_value = []
        for phoneme in value:
            new_value.append(phoneme if phoneme not in natural_class[0] else natural_class[1])
        new_mapping[key] = new_value
    return new_mapping

# Find size
def find_size(mapping):
    word_set = set()
    for key, value in mapping.items():
        word_set.add(tuple(value) )
    return len(word_set)

# Find the score of a certain neutralization. Is 0 if makes no difference (k --> q), 1 if maps all to the same
def score(natural_class, mapping):
    return find_size(neutralize(natural_class, mapping) ) / find_size(mapping)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word_to_phoneme_mapping = import_file("Britfone.json")
    print(score(English["vowels"], word_to_phoneme_mapping) )


