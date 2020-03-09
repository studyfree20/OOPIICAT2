#BIT2203: Advanced object Oriented Programming
import math
'''
CAT 2 + Assignment 2
Instructions: Answer all Questions (30 marks); Upload your code to Github
'''
#   a) Define the following terms as used in abject oriented programming (5 marks)
#i. Polymorphism
'''
Polymorphism is the provision of a single interface to entities of different types or the use of a single symbol to 
represent multiple different types. 
Polymorphism also is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs
when a super class reference is used to refer to a derived class object.
The most commonly recognized major classes of polymorphism are:
Ad hoc polymorphism: defines a common interface for an arbitrary set of individually specified types.
Parametric polymorphism: when one or more types are not specified by name but by abstract symbols that can represent 
any type.
Subtyping when a name denotes instances of many different classes related by some common superclass.
In real life polymorphism can refer to the ability of doing one thing in many ways.EG To move from point a-b one can run, walk,
drive or fly but the act of moving is in different forms

'''
#ii. Inheritance
'''
It is the mechanism of basing an object or class upon another object or class, while retaining similar implementation.
 Also defined as deriving new classes from existing ones and forming them into a hierarchy of classes.
It is the mechanism by which a parent class passes attributes,behavior and methods to a child class.It is a mechanism
 that enables reuse of code

'''
#iii. Abstraction
'''
It is the process of removing physical, spatial, or temporal details or attributes in the study of objects or systems
to focus attention on details of greater importance. It involves selecting data from a larger pool to show only the
relevant details to the object. It helps to reduce programming complexity and effort.
'''
#iv. Encapsulation
'''
This refers to the bundling of data with the methods that operate on that data, or the restricting of direct  access to some of an object's components.
It refers to bringing data, functions and methods under the same capsule
'''
#v. Function
'''
A function is a combination of instructions that are combined to achieve some result and is independent and not associated with a class.
An example of function is the user defined function
'''
#b) Write a python program to calculate the compound interest. Use the formula A= P(1 + R/100)t (5 marks)
#the program will get input from user
#parentesis is key here.Poor annotation will cause error since python has issues with floor / //
P = int(input("Please Enter starting principle. "))
n = int(input("Enter Compound intrest rate.(Eg half-year, yearly) "))
r = float(input("Enter annual interest amount. (In decimal) "))
t = int(input("Enter the amount of years. "))
#to avoid floor issues annual and compound interest are split while maintaining formula
final = P * (((1 + (r/(100.0 * n))) ** (n*t)))
#displays the final amount after number of years.
print ("The final amount after", t, "years is", final)




#c) Write a Python function to convert temperatures to and from celsius, fahrenheit. [ Formula : c/5 = f-32/9 [where c = temperature in celsius and f = temperature in fahrenheit ] (5 marks)
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius
def convert_temp(scale=None, source_temp=None):
    if scale == "FAH":
        return 'CEL', (source_temp - 32.0) * (5.0/9.0)
    elif scale == "CEL":
        return 'FAH', (source_temp * (9.0/5.0)) + 32.0
    else:
        print("Needs to be (FAH) or (CEL)!")

scale = input("Select (FAH) or (CEL): " )
source_temp = int(input("What is the temperature: " ))
s, m = convert_temp(scale, source_temp)
print(source_temp, "degrees", scale, "is", m, "degrees", s)
#d) Pig latin is a language game where English words are altered by moving some letters to the end of the word and/or 
# by adding a suffix. (5 marks)
#Task Write a program that will take a word and output the pig latin version of the word
#by following the following rules:
#a. If the word starts with a consonant or group of consonants, move all letters before the first vowel to the end of
#  the word then add "ay".
#Example :
#will -> illway
#dog -> ogday
#category -> ategorycay
#chatter -> atterchay
#trash -> ashtray
#2. If the word starts with a vowel, simply add "way" to the end of the word.
#Example :
#electrician – electricianway
pigLatin = input("Convert message to pig latin: ")
wordList = pigLatin.lower().split(" ")
vowels = ['a', 'e', 'i', 'o', 'u']
pigLatin = []
eachWord = []
for word in wordList:
#case where vowel is first
    if word[0] in 'aeiou': 
        pigLatin.append(word + 'yay')
    else:
        for letter in word:
            if letter in 'aeiou':
                pigLatin.append(word[word.index(letter):] + word[:word.index(letter)] +'ay')
                break


print(" ".join(pigLatin))

#e) Write a Python function to find the Max of three numbers (5 marks)

#defining numbers and allowing users to input
def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list) 
#Getting input from user
x = int(input("Please Enter First number"))
y = int(input("Please Enter Second number"))
z = int(input("Please Enter Final number"))
print("Maximum Number is ::>",maximum(x, y, z))  

#f) Write a Python program to print the even numbers from a given list. (5 marks)
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]
beginof = int(input("Please Enter the start of your target range Eg 1: ")) 
endof = int(input("Please Enter the end of your target range Eg 50: ")) 
#defining range 
for num in range(beginof, endof + 1): 
      
    # checking condition 
    if num % 2 == 0: 
        print(num, end = " ")
#End of simple assignment
