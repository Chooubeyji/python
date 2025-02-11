# Datatypes

-numbers : 1,2,3,4 3.41,3+6j,Decimal()
-strings : 'spas', "choubey" 
-list : [ 1, 2, ["hii" , 2] , 7 , 8 ] , list(range(10)) 
-tuple : (1,"choubey" , 3 , 4)
-dictionary :  { 'food' : 'tasty' }
-set : set('abc') , {'a','b','c'}
-boolean : true , false

capitalize(): Converts the first character to uppercase.
text = "hello world"
print(text.capitalize())  # Output: Hello world

casefold(): Converts string to lowercase.
text = "HELLO WORLD"
print(text.casefold())  # Output: hello world

center(width[, fillchar]): Centers the string within the specified width.
text = "Python"
print(text.center(10, "*"))  # Output: **Python**

count(sub[, start[, end]]): Returns the number of occurrences of a substring.
text = "Python is fun"
print(text.count("o"))  # Output: 2

encode([encoding[, errors]]): Encodes the string using the specified encoding.
text = "Python"
print(text.encode("utf-8"))  # Output: b'Python'

endswith(suffix[, start[, end]]): Checks if the string ends with the specified suffix.
text = "Python is fun"
print(text.endswith("fun"))  # Output: True

expandtabs([tabsize]): Replaces tabs with spaces.
text = "Python\tis\tfun"
print(text.expandtabs(4))  # Output: Python    is    fun

find(sub[, start[, end]]): Returns the lowest index of the substring.
text = "Python is fun"
print(text.find("is"))  # Output: 7
format([format_spec]): Formats the string using the specified format.

python
text = "Hello, {}!"
print(text.format("Python"))  # Output: Hello, Python!
index(sub[, start[, end]]): Similar to find() but raises an exception if the substring is not found.

python
text = "Python is fun"
print(text.index("is"))  # Output: 7
isalnum(): Checks if all characters are alphanumeric.

python
text = "Python123"
print(text.isalnum())  # Output: True
isalpha(): Checks if all characters are alphabetic.

python
text = "Python"
print(text.isalpha())  # Output: True
isdigit(): Checks if all characters are digits.

python
text = "123"
print(text.isdigit())  # Output: True
islower(): Checks if all characters are lowercase.

python
text = "python"
print(text.islower())  # Output: True
isspace(): Checks if all characters are whitespace.

python
text = "   "
print(text.isspace())  # Output: True
istitle(): Checks if the string is a titlecased string.

python
text = "Python Is Fun"
print(text.istitle())  # Output: True
isupper(): Checks if all characters are uppercase.

python
text = "PYTHON"
print(text.isupper())  # Output: True


join(iterable): Joins the elements of an iterable with the string as a separator.
python
text = "-"
print(text.join(["Python", "is", "fun"]))  # Output: Python-is-fun


ljust(width[, fillchar]): Left-justifies the string within the specified width.
python
text = "Python"
print(text.ljust(10, "*"))  # Output: Python****


lower(): Converts the string to lowercase.
python
text = "PYTHON"
print(text.lower())  # Output: python

squared num = [x**2 for x in range(10)]
squared num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 