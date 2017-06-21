"""this method:
-helps to find the spell between 'fe' and 'ai'
-checks if the spell is correct(begins with fe, ends with ai and has only one 'fe')"""
def extract_body(word):
    body_found = False
    find_fe = word.find("fe")
    find_ai = word.rfind("ai")
    new_word = ""
    if find_fe>-1 and find_ai>-1 and find_ai>find_fe and word.count("fe")==1:
        new_word = word[find_fe+2:find_ai]
        body_found = True
    return body_found,new_word

"""this methods below count damage: the first one for a single subword, the second one for a list of subwords"""
def  dam_s(subword):
    if subword=="ai":
        return 2
    elif subword=="fe":
        return 1
    elif subword == "je":
        return 2
    elif subword == "jee":
        return 3
    elif subword == "ain":
        return 3
    elif subword == "dai":
        return 5
    elif subword == "ne":
        return 2
    else:
        return -1*len(subword)
def count_damage(my_list):
    dam = 0
    for i in range(len(my_list)):
        dam+=dam_s(my_list[i])
    return dam

"""this method takes a string a splits it to all possible substrings"""
def all_substr(string):
    for i in range(len(string)):

        if i == len(string)-1:
            yield string

        first_part = string[0:i+1]
        second_part = string[i+1:]

        for j in all_substr(second_part):
            yield ','.join([first_part, j])

def damage(spell):
    result = (max(count_damage(i.split(',')) for i in (all_substr(extract_body(spell)[1]))) + 3)
    if extract_body(spell)[0]==False:
        return 0
    elif result<0:
        return 0
    else:
        return result



print (damage('xxxxxfejejeeaindaiyaiaixxxxxx'))
