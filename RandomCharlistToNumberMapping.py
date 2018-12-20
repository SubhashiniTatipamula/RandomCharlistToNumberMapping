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


input_char_list = ['S', 'E', 'V', 'E', 'N', 'F', 'O', 'U', 'R', 'F', 'O', 'U', 'R']


# Method to return non matching characters
def diff(temp_list):
    char_set = set()
    print(set(ip).intersection(temp_list))
    if set(input_char_list).intersection(temp_list):
        for letter in ip:
            if letter in temp_list and (input_char_list.count(letter) == temp_list.count(letter)):
                pass
            else:
                char_set.add(letter)

    return char_set


# Fetching probable words set
probable_set = set()
final_list = list()
unwanted_char = set(temp.keys()) - set(input_char_list)
repeat_count = dict()
length = len(input_char_list)
expecting_count = 0
for char in input_char_list:
    words = temp[char]
    for word in words:
        for elm in unwanted_char:
            if elm in word:
                break
        else:
            probable_set.add(word)
            repeat_count[word] = repeat_count.get(word, 0) + 1

final_list = list(probable_set)
for word in final_list:
    expecting_count += len(word)
print(probable_set)
print(repeat_count)
print(expecting_count)
print(length)

char_balancer = []
for word in probable_set:
    char_balancer.extend(word)

# Preparing the final list either by adding the missing words / removing excessive words
sorted_dict = {r: repeat_count[r] for r in sorted(repeat_count, key=repeat_count.get, reverse=True)}
sorted_list = list(sorted_dict.keys())
print(sorted_list)
add_index = 0
while length != expecting_count:
    if expecting_count < length:
        elm = sorted_list[add_index]
        final_list.append(elm)
        char_balancer.extend(elm)
        expecting_count += len(elm)
        add_index += 1

    test = diff(char_balancer)
    if test:
        print(test)
        for word in final_list:
            temp_val = test.intersection(word)
            if temp_val == test or (len(temp_val) > len(word) / 2):
                final_list.remove(word)
                expecting_count -= len(word)
                for char in word:
                    char_balancer.remove(char)
print(final_list)
