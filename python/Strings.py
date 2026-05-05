#STRING METHODS

#String - A string is a sequence of characters (letters, numbers, symbols) enclosed in quotes.
name = "raju"
city = "vzg"
phno = '1234567890'

#String Methods:
#1. replace() : Replaces a substring with another substring.
   str = "python is programming"
   print(str.replace("python","java")) #java is programming
   #str is immutable datatype. Doesnot modify the original string.
   print(str) #python is programming

#2. strip() : removes spaces (or characters) from both ends.
    str1 = "  python is programming language  "
    print(str1.strip(" "))
    str1 = "python is programming language"
    print(str1.strip("age"))
    print(str1.strip("p"))

#3. join() : joins the elements of a list into a string.
    str2 = ["i","am","raju"]
    print(" ",join.(str2))

#4. count() : counts occurrences of a substring.
   str = "python is programming"
   print(str.count("a"))
   print(str.count("i"))

#5. index() : returns first position of substring(error if not found). and execution stops there when substring is not found.
   str = "python is programming"
   print(str.index("p"))

#6. rindex() : returns last position of substring.
   str = "python is programming"
   print(str.rindex("p"))

#7. find() : returns first index, returns (-1) when substring is not found.
   str = "python is programming"
   print(str.find("y"))
   print(str.find("z"))

#8. rfind() : returns last index, -1 if not found.
   str = "python is programming"
   print(str.rfind('i'))
   
#9. isupper() : checks if all charaters are uppercase.
   str = "python is programming"
   print(str.isupper())
   
#10. upper() : converts all characters into uppercase.
    str = "python is programming"
    print(str.upper())
    
#11. islower() : checks if all charaters are islower.
    str = "python is programming"
    print(str.islower())
    
#12. lower() : converts all characters into uppercase.
    name = "pyTHon is programming"
    print(name.lower())
    
#13. isalpha() : checks if string contains only letters.
    str = "python is programming"
    print(str.isalpha())
    
#14. isnumeric() : checks if string contains only digits.
    str3 = "123"
    print(str3.isnumeric())
    
#15. isalnum() : checks if string contains only letters + numbers.
    str5 = "python is programming123"
    print(str5.isalnum())
    
#16. isdigits() : checks digits only.
    print(str3.isdigit())
    
#17. endswith() : checks if strings ends with given value.
    str = "python is programming"
    print(str.endswith("programming"))
    
#18. startswith() : checks if strings starts with given value.
    str = "python is programming"
    print(str.startswith("python"))
    
#19. Concatenation() : joins the two strings.
    str = "python is programming"
    str3 = "123"
    print(str+str3)
    
#20. zfill()
