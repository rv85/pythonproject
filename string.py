x="python"
print(x)
print(id(x))
print(type(x))
print(len(x))
print(x[3])
print(x[-4])

y="programming"
print(x+" "+y)

#string slicing
x="python program"
print(x[0:6]) #Always upperbound ix excluded. Print python

#extract prog
print(x[7:11])
print(x[11:7]) #returns empty string- because always slicing in the forward direction

#extract "prog" using negative index
print(x[-7:-3])

#extract entire word "program"
print(x[7:14])
print(x[:])

#string methods:
#upper() to print uppercase
x="hyderabad"
print(x.upper())

#upper() to print in uppercase
x="hyderabad"
print(x.upper())

#To print to lower case
x="CHENNAI"
print(x.lower())

#capatazlize the first letter
x="india"
print(x.capitalize())

#capatilizing the first character of each word
x="good evening hyderabad"
print(x.title())

#To print each name first character capital
emps="rohit,john,ravi,sruti,swetha"
print(emps.title())

#swapcase:
x="good evening hyderabad"
print(x.swapcase())

#replace
x="Java is easy and Java is simple"
print(x.replace("Java","Python"))

#count(): to count the no of occurences of a sub string or a character
x="hello hello hello ... how r you?"
print(x.count("hello"))

#Multi line string
data='''python is easy
python is simple
python supports 89300 modules
python is dynamic type
python is extensible'''
print(data.count("python"))

#format(): for substitutions
x="{} is the captain of indian team"
print(x.format("Rohit"))

x="His name is {} and he is {}"
print(x.format("Ravi","QA Engineer"))

#find():To check wheather a substring is available or not. If found it returns the 1st character index position else it returns -1
x="python is easier than Java"
print(x.find("Java"))
print(x.find("Hadoop"))

#split method: To remove the blank spaces before and after the string
x="                  Good Evening Hyderabad    "
print(x,len(x))
y=x.strip()
print(y,len(y))

#split: If we split a string we get list
x="Good Evening Hyderabad"
y=x.split(" ")
print(y,type(y))
print(y[2])

#string slicing; extract particular portion of a string( extract python)
x="python program"
print (x[0:6])
#extract program 
print (x[7:14])

#extract prog using negative index
print(x[-7:-3])

#print in uppercase
x="hyderabad"
print(x.upper())

#print in lowercase
x="HYDERABAD"
print(x.lower())

#capatalize
x="good evening hyderabad"
print(x.capitalize())

#swap-prints lower to upper
x="good evening hyderabad"
print(x.swapcase())