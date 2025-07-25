def word_count(text):
    split_list= text.split()
    word_count=len(split_list)
    #print(f"{word_count} words found in the document")
    return word_count

# returns the characters in with a key: charachter, value: count
def char_count(text):
    char_list_dic={}
    word_list= text.split()
    for word in word_list:
        for char in word:
            char=char.lower()
            if char not in char_list_dic:
                char_list_dic[char] =1
            else:
               char_list_dic[char] +=1 
    return char_list_dic


def sort_on(items):
    return items["num"]

#Return the sorted character dictionary by highest count
def sort_on_letters(items):
    sort_list=[]
    for char in items:
        temp_dic={}
        temp_dic["char"]=char
        temp_dic["num"]=items[char]
        sort_list.append(temp_dic)
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
