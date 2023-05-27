from difflib import SequenceMatcher  
string1 = input("First String: ")
string2 = input("Second String: ")
match = SequenceMatcher(None,string1, string2)
result = match.ratio() * 100
print(int(result),"%")