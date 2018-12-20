"""
Script to find out the valid numbers from a given character list
# -----------------------------------------------------------
# Original Author: Subhashini Tatipamula
# Created Date : 11-Dec-2018
# ------------------------------------------------------------
"""
expected_number_word = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
temp = {'Z': ['ZERO'], 'E': ['ZERO', 'ONE', 'THREE', 'FIVE', 'SEVEN', 'NINE', 'EIGHT'], 'R': ['ZERO', 'THREE', 'FOUR'],
        'O': ['ZERO', 'ONE', 'FOUR'], 'N': ['ONE', 'SEVEN', 'NINE'], 'T': ['TWO', 'THREE', 'EIGHT'], 'W': ['TWO'],
        'H': ['THREE', "EIGHT"], 'F': ['FOUR', 'FIVE'], 'U': ['FOUR'], 'I': ['FIVE', 'SIX', 'EIGHT', 'NINE'],
        'V': ['FIVE', 'SEVEN'], 'S': ['SIX', 'SEVEN'], 'X': ['SIX'], 'G': ['EIGHT']}

# input_char_list = ['O', 'Z', 'O', 'N', 'E', 'T', 'O', 'W', 'E', 'R', 'R', 'Z', 'O', 'E']
input_char_list = ['S', 'E', 'V', 'E', 'N', 'F', 'O', 'U', 'R']

# Fetching probable words set
probable_set = set()
intermediate_set = set()
unwanted_char = set(temp.keys()) - set(input_char_list)
repeat_count = dict()
length = len(input_char_list)
expecting_count = 0
for char in input_char_list:
    words = temp[char]
    repeat_count[char] = repeat_count.get(char, 0) + 1
    for word in words:
        for elm in unwanted_char:
            if elm in word:
                break
        else:
            probable_set.add(word)

print(probable_set)


elm_dict = {}
for k in repeat_count.keys():
    for index, word in enumerate(probable_set):
        if k in word:
            elm_dict[k] = (elm_dict.get(k, list())) + [word]
        else:
            pass

# Collecting initial set of expected words and required data for figuring out the missing ones
filtering_data = set()
for k in repeat_count.keys():
    if repeat_count[k] == len(elm_dict[k]):
        intermediate_set.update(elm_dict[k])
    else:
        intermediate_set.add(k)

for word in intermediate_set:
    expecting_count += len(word)
final_list = list(intermediate_set)

print(filtering_data)
print(repeat_count)
print(elm_dict)
print(expecting_count)
print(length)

# Preparing the final list either by adding the missing words / removing excessive words
while length != expecting_count:
    for word in probable_set:
        if filtering_data.intersection(word) == filtering_data:
            if expecting_count < length:
                final_list.append(word)
                expecting_count += len(word)
            elif length != expecting_count:
                final_list.remove(word)
                expecting_count -= len(word)

print(final_list)
