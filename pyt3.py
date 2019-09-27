# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


# concatenation  of two or more strings
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)



# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")





# Python Program to Access 
# characters of String 
  
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 
  
# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 
  
# Printing Last character 
print("\nLast character of String is: ") 
print(String1[-1]) 
  
# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 
  
# Printing characters between  
# 3rd and 2nd last character 
print("\nSlicing characters between " +
    "3rd and 2nd last character: ") 
print(String1[3:-2]) 






# Python Program to Update 
# entire String 
  
String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 
  
# Updating a String 
String1 = "Welcome to the Geek World"
print("\nUpdated String: ") 
print(String1) 






# Python Program to Delete 
# entire String 
  
String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 
  
# Deleting a String 
# with the use of del 
del String1  
print("\nDeleting entire String: ") 
print(String1)






# Python Program for 
# Escape Sequencing  
# of String 
  
# Initial String 
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 
  
# Escaping Single Quote  
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ") 
print(String1) 
  
# Escaping Doule Quotes 
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ") 
print(String1) 
  
# Printing Paths with the  
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1) 
  
# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 
  
# Using raw String to  
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1)










# Python Program for 
# Formatting of Strings 
  
# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 
  
# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 
  
# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 
  
# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 
  
# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 
  
# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 
  
# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)










def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))
