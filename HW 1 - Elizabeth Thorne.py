#!/usr/bin/env python
# coding: utf-8

# # OOP - Class 

# ## Exercise 1: 
# Create a Player class with a name, a position, and a speed attributes. Set the initial value of speed to 1 and create any necessary methods.
# Then, 
# 1. Create two Player objects and print information about both players.
# 2. Assign 8 to player 1's speed
# 3. print information about both players.

# In[12]:


class Player:
    '''Player class attributes are name, position, and speed'''
    def __init__ (self, name, position):
        self.name = name
        self.position = position
        self.speed = 1
    def print_info(self):
        return f"Name is {self.name} Team position is {self.position} Speed is {self.speed}"
    
    


# In[13]:


player1 = Player('T-Bone','Short stop')
player2 = Player('Morizawa','Pitcher')

player1.speed = 8

player1.print_info()
player2.print_info()


# ## Exercise 2: 
# Create a class called Rectangle with height and length attributes and has following methods: 
# - perimeter() : returns a perimeter of a rectangle object
# - area() : returns an area of a rectangle object
# 
# Then,
# 1. create two instances of Rectangle class
# 2. print each rectangle's perimeter and determine which rectangle has larger perimeter
# 3. print each rectangle's area and determine which rectangle has larger area

# In[22]:


class Rectangle:
    '''Rectangle attributes are height and length, methods are perimeter and area'''
    def __init__ (self,height,length):
        self.height = height
        self.length = length 
    def perimeter(self):
        perimeter = (self.height*2)+(self.length*2)
        return perimeter
    def area(self):
        area = self.height*self.length
        return area


# In[25]:


rectangle1 = Rectangle(10,4)
rectangle2 = Rectangle(3,12)


# In[26]:


rectangle1.perimeter()


# In[28]:


rectangle2.perimeter()

#rectangle 2 has a larger perimeter


# In[29]:


rectangle1.area()

#rectangle 1 has a larger area


# In[30]:



rectangle2.area()


# ## Exercise 3: 
# Create a class called Triangle with height and base attributes and has following methods:
# 
# - perimeter() : returns a perimeter of a right triangle object
# - area() : returns an area of a right triangle object
# 
# Then,
# 
# - create two instances of Triangle class
# - print each triangle's perimeter and determine which triangle has larger perimeter
# - print each triangle's area and determine which triangle has larger area
# 
# Use 
# - perimeter of a right triangle = height + base + Square-Root((height \** 2) + (base \** 2)) 
# - area of a right triangle = ( height * base ) / 2
# 
# You'll need to <b>import math</b> library and use <b>math.sqrt()</b> function.
# 
# 

# In[39]:


import math

class Triangle:
    '''Triangle class has attributes height and base, with methods perimeter and area'''
    def __init__(self,height,base):
        self.height = height
        self.base = base
    def perimeter(self):
        perimeter = (self.height)+(self.base)+math.sqrt(self.height)+math.sqrt(self.base)
        return perimeter
    def area(self):
        area = (self.height*self.base)/2
        return area


# In[40]:


tri1 = Triangle(4,8)
tri2 = Triangle(12,3)


# In[41]:


tri1.perimeter()


# In[42]:


tri2.perimeter()
#triangle 2 has the larger perimeter


# In[43]:


tri1.area()


# In[44]:


tri2.area()
#triangle 2 also has the larger area


# ## Exercise 4: 
# Write a program that maintains a list of movies, and the user can list all the movies, add a movie to the list, or delete a movie from the list. All input/output are done at the program level, not at a class level.
# 
# 
# For Python 1 Day 3 Challenge Exercise, you wrote a program that maintains a list of movies, and the user can list all the movies, add a movie to the list, or delete a movie from the list. Modify that program to use a <b>Movie object</b> to store name, year, and genre of a movie. Create any method you need to access these attributes but your method can not use <b>print</b> function. 
# 
# Additionally, create any function you need to make sure program neat. You may use <b>print</b> function in your function.
# 

# In[51]:


class Movie:
    '''Movie class has attributes name, year, genre'''
    def __init__(self, name, year, genre):
        self.name = name
        self.year = year
        self.genre = genre
    def print_value (self):
        return f'The {self.year} {self.genre} film {self.name}'
        
class Movies:
    '''Movies has the attributes of movie in a list '''
    def __init__ (self):
        self.list = []
    def add_movie(self, movie):
        self.list.append(movie)
    def delete_movie(self,movie):
        self.list.remove(movie)
    def show_all(self):
        for movie in self.list:
            print(movie.print_value())


    


# In[52]:


movie1 = Movie('Brokeback Mountain',2005,'Drama')
movie2 = Movie('Napoleon Dynamite',2005,'Comedy')
movie3 = Movie('Chinatown',1974,'Neo-Noir')


# In[53]:


my_movies = Movies()


# In[54]:


my_movies.add_movie(movie1)
my_movies.add_movie(movie2)
my_movies.add_movie(movie3)


# In[55]:


my_movies.show_all()


# In[56]:


my_movies.delete_movie(movie2)


# In[57]:


my_movies.show_all()


# ## Exercise 5: 
# Create a class called Employee with 
# - firstname,
# - lastname, 
# - joined_date
# - active
# 
# attributes and methods to retrieve each attribute.
# 
# Then, write a program to 
# - add 10 or more employees
# - print all employees' information
# - print all active employees' information
# 
# Create any methods you need but all print statements should be called from your program, not in your class method!
# 
# You must use below data set (but can add more):
# 
#     data = [{"first":"elmo", "last":"monster", "year": 2000},
#             {"first":"count", "last":"count", "year": 1819},
#             {"first":"big", "last":"bird", "year": 2011},
#             {"first":"cookie", "last":"monster", "year": 2002},
#             {"first":"bert", "last": "person", "year": 2013},
#             {"first":"ernie", "last": "person", "year": 2013},
#             {"first":"oscar", "last": "grouch", "year": 1999},
#             {"first":"zoe", "last": "cutie", "year": 2015},
#             {"first":"abby", "last": "cadabby", "year": 2016},
#             {"first":"prairie", "last": "dawn", "year": 2020}
#        ]

# In[113]:


class Employee:
    '''Employee class has attributes firstname, lastname, joined_date, active'''
    def __init__(self, firstname, lastname, joined_date, active=True):
        self.firstname = firstname
        self.lastname = lastname
        self.joined_date = joined_date
        self.active = active
    def print_info(self):
        return f"First Name:{self.firstname}\nLast Name:{self.lastname}\nYear:{self.joined_date}\nActive Status:{self.active}"


# In[118]:


class Employees:
    def __init__(self):
        self.list = []
    def add_employees(self, employee):
        self.list.append(employee)
    def show_all(self):
        for employee in self.list:
            print(employee.print_info())
    def show_active(self):
        for employee in self.list:
            if employee.active == True:
                print(employee.print_info())

                


# In[119]:


my_employees = Employees()

data = [{"first":"elmo", "last":"monster", "year": 2000},
        {"first":"count", "last":"count", "year": 1819},
        {"first":"big", "last":"bird", "year": 2011},
        {"first":"cookie", "last":"monster", "year": 2002},
        {"first":"bert", "last": "person", "year": 2013},
        {"first":"ernie", "last": "person", "year": 2013},
        {"first":"oscar", "last": "grouch", "year": 1999},
        {"first":"zoe", "last": "cutie", "year": 2015},
        {"first":"abby", "last": "cadabby", "year": 2016},
        {"first":"prairie", "last": "dawn", "year": 2020}
   ]


for i in data:
    e = Employee(i['first'],i['last'],i['year'])
    my_employees.add_employees(e)

    
my_employees.show_all()



# In[120]:


inactive1 = Employee('Doctor','Horrible',2010,False)
inactive2 = Employee('Pinky','Brain',1999,False)

my_employees.add_employees(inactive1)
my_employees.add_employees(inactive2)


# In[121]:


my_employees.show_active()


