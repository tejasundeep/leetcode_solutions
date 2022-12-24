string_1 = "sizent"
string_2 = "listen"

list_one = []

for i in string_1:
    list_one.append(i)

string_one_length = len(string_1)
string_two_length = len(string_2)


list_two = []

if string_one_length == string_two_length:
    for i in range(string_one_length):
        if list_one[i] in string_2:
            list_two.append("Success")        
else:
    print("Not an anagram")

if len(list_two) == string_one_length:
    print("It is an anagram")
else:
    print("It is not an anagram")