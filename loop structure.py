''''i=1
while i<=100:
    print(i)
    i=i+1'''
'''marks=[12,34,55,67]#list [] for complex data type and just like array in c ele r in seq order
marks.append(99)
marks.insert(1,00)
print(marks)
print(93 in marks)
print(len(marks))
marks.clear()
print(marks)'''
#break and continue use in list
'''students=["rajesh","vineet","kapil","pankaj","suraj"]
for name in students:
    if (name=="kapil"):
        break;
    print(name)'''
#tuple ()in this we cannot change its elements btw the prgm once it defined it will as it is:-
'''marks=(98,84,85,84,84)
print(marks.count(84))
print(marks.index(84))'''
#set{} it does not have a index or seq order and it takes only the original common value only one 
#marks={333,33,445,556,66}
#print(marks)
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')
if __name__ == '__main__':
    first_name = input()
    last_name = input()
          

