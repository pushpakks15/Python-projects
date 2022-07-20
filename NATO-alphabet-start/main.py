
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data=pandas.read_csv("C:/Users/Admin/PycharmProjects/NATOproject/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
condict=data.to_dict()
new_dict={key:value for (key,value) in condict.items() if key=="letter"}
letters=new_dict["letter"]
alphabets=list(letters.values())

neww_dict={key:value for (key,value) in condict.items() if key=="code"}
figure=neww_dict["code"]
words=list(figure.values())
final_dict={}
count=0
for alphabet in alphabets:
    final_dict[alphabet]=words[count]
    count+=1
def code():
    try:
        user_input=input("Please enter your name: ").upper()
        list_of_words=[final_dict[each_alphabet] for each_alphabet in user_input]
    except KeyError:
       print("Sorry only letters in the name please")
       code()
    else:
       print(list_of_words)
code()




