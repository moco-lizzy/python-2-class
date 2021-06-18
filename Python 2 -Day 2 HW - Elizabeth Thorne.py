{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# OOP - Composition, Encapsulation, & Inheritance"
   ]
  },
  {{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# OOP - Composition, Encapsulation, & Inheritance"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 1: \n",
    "Create a Temperature Converter program using OOP by creating a Temperature class with two private attributes to store Fahrenheit and Celsius degrees. In the Temperature class, define methods that \n",
    "- sets the private attributes. When you set one unit of temperature, it should calculate and set the other unit of temperature. For example, when you set degrees in Fahrenheit, it should calculate and set in Celsius degrees. \n",
    "- gets the hidden attributes that round the number to 2 decimal places. \n",
    "\n",
    "The output should look something like following:\n",
    "\n",
    "    MENU\n",
    "    1. Fahrenheit to Celsius\n",
    "    2. Celsius to Fahrenheit\n",
    "    3. Quit\n",
    "    \n",
    "    Enter a menu option: 1\n",
    "    Enter degrees in Fahrenheit: 99\n",
    "    99.00 oF is 37.22 oC.\n",
    "    \n",
    "    Enter a menu option: 2\n",
    "    Enter degrees in Celsius: 37.22\n",
    "    37.22 oC is 99.00 oF.\n",
    "    \n",
    "    Enter a menu option: 3\n",
    "    Bye\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Temp:\n",
    "    def __init__(self, degree, temp):\n",
    "        while degree != 1 and degree != 2:\n",
    "            degree = int(input(\"Please enter valid degree value, F is 1, C is 2\"))\n",
    "            if degree == 1 or degree == 2:\n",
    "                break\n",
    "        self.__degree = degree\n",
    "        self.__temp = temp\n",
    "    def FtoC(self):\n",
    "        if self.__degree == 1:\n",
    "            return round((self.__temp -32) *.5556, 2)\n",
    "    def CtoF (self):\n",
    "        if self.__degree == 2:\n",
    "            return round((self.__temp * 1.8) + 32, 2)\n",
    "\n",
    "    \n",
    "test1 = Temp(2,29)\n",
    "\n",
    "\n",
    "test1.FtoC()\n",
    "\n",
    "# test2 = Temp(2,59)\n",
    "\n",
    "# test2.CtoF()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_menu():\n",
    "    print(\"MENU\")\n",
    "    print(\"Fahrenheit to Celsius\")\n",
    "    print(\"Celsius to Fahrenheit\")\n",
    "    print(\"Quit\")\n",
    "    \n",
    "while True:\n",
    "    display_menu()\n",
    "    command = input(\"Command: \")\n",
    "    \n",
    "    if command == \"Fahrenheit to Celsius\":\n",
    "        degree = 1\n",
    "        temp = int(input(\"Tempurature: \"))\n",
    "        test = Temp(degree,temp)\n",
    "        print(test.FtoC())\n",
    "        break\n",
    "    elif command == \"Celsius to Fahrenheit\":\n",
    "        degree = 2\n",
    "        temp = int(input(\"Tempurature: \"))\n",
    "        test = Temp(degree,temp)\n",
    "        print(test.CtoF())\n",
    "        break\n",
    "    elif command == \"Quit\":\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 2: \n",
    "Create a <b>Privileges</b> class that has privileges, a private attribute. It can store a list of strings such as \"can add\", \"can delete\", and \"can modify\".  Write a method called show_privileges(). \n",
    "\n",
    "Create a class called <b>Admin</b> that inherits from the <b>Person</b> class (see next cell). Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person :\n",
    "    \n",
    "    def __init__(self, name, age, gender) :\n",
    "        self.__name = name\n",
    "        self.__age = age\n",
    "        self.__gender = gender\n",
    "\n",
    "    def get_name(self) :\n",
    "        return self.__name\n",
    "    \n",
    "    def get_info(self) :\n",
    "        return f\"Name: {self.__name}\\n Age: {self.__age}\\n Gender: {self.__gender}\"\n",
    "       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Privileges:\n",
    "    def __init__(self, privileges):\n",
    "        self.__privileges = privileges\n",
    "    def show_privileges(self):\n",
    "        return self.__privileges\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Admin(Person):\n",
    "    def __init__ (self, name, age, gender):\n",
    "        super().__init__(name,age,gender)\n",
    "        self.__privileges = \"can edit\"\n",
    "    def show_privileges(self):\n",
    "        return self.__privileges\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Name: Bryant\\n Age: 32\\n Gender: M'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "addy = Admin(\"Bryant\",32,\"M\")\n",
    "addy.get_info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'can edit'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "addy.show_privileges()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 3:\n",
    "1. Use the Product class from next cell\n",
    "2. Add get_description() method to Product class\n",
    "3. Create Book class inherited from the Product class. Add author attribute to the Book class and make modification to get_description() method\n",
    "4. Create Movie class inherited from the Product class. Add year attributes. Add/modify necessary methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# From Day 1 Class Demo\n",
    "class Product : \n",
    "    \"\"\"A simple attempt to model a product.\"\"\"\n",
    "    \n",
    "    def __init__(self, name, price, discount_rate) :\n",
    "        \"\"\"Initialize name, price, and discount_rate attributes\"\"\"\n",
    "        self.name = name\n",
    "        self.price = price\n",
    "        self.discount_rate = discount_rate\n",
    "        \n",
    "        \n",
    "    def get_discount_amount(self) :\n",
    "        \"\"\"Computes a discount calculation\"\"\"\n",
    "        return self.price * self.discount_rate / 100\n",
    "    \n",
    "        \n",
    "    def get_info(self) :\n",
    "        return(f\"Name: {self.name}\\n\" + \n",
    "                f\"Price: {self.price}\\n\" +\n",
    "                f\"Disicount Amount: ${self.get_discount_amount():,.2f}\\n\" +\n",
    "                f\"Discounted Price: ${self.get_sale_price():,.2f}\")\n",
    "    \n",
    "    def get_sale_price(self) :\n",
    "        \"\"\"Calls another method to find a sale price\"\"\"\n",
    "        return self.price - self.get_discount_amount()\n",
    "        \n",
    "    def get_description(self):\n",
    "        return f\"{self.name} sells for {self.price} with a discount rate of {self.discount_rate}\"\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The Illiad by Homer sells for $24 with a discount rate of 12%'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Book (Product):\n",
    "    def __init__(self, name, author, price, discount_rate):\n",
    "        super().__init__( name, price, discount_rate)\n",
    "        self.author = author\n",
    "    def get_author(self):\n",
    "        return self.author\n",
    "    def get_description(self):\n",
    "        return f\"{self.name} by {self.author} sells for {self.price} with a discount rate of {self.discount_rate}\"\n",
    "\n",
    "    \n",
    "book1 = Book(\"The Illiad\",\"Homer\",\"$24\",\"12%\")\n",
    "book1.get_description()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sleepless in Seattle from 1999 sells for $12 with a discount rate of 50%'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Movie (Product):\n",
    "    def __init__(self, name, year, price, discount_rate):\n",
    "        super().__init__( name, price, discount_rate)\n",
    "        self.year = year\n",
    "    def get_year(self):\n",
    "        return self.year\n",
    "    def get_description(self):\n",
    "        return f\"{self.name} from {self.year} sells for {self.price} with a discount rate of {self.discount_rate}\"\n",
    "\n",
    "    \n",
    "movie1 = Movie(\"Sleepless in Seattle\",\"1999\",\"$12\",\"50%\")\n",
    "movie1.get_description()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 4\n",
    "Create a <b>MyDate</b> class with month, day, year, hour, minute, and second <b>private attributes</b>.  Create an initialization method that takes a string in the format of \"mm-dd-yyyy hh:mm:ss\". Also create necessary public methods as needed.  \n",
    "\n",
    "Then, run below program to show your class works:\n",
    "\n",
    "    today = MyDate(\"10-10-2020 12:11:22\")\n",
    "    print(today.get_datetime())\n",
    "    today.set_datetime(\"11-31-1999 02:33:22\")\n",
    "    print(today.get_datetime())\n",
    "    print(today.get_datetime(month_first=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyDate:\n",
    "    def __init__ (self, date):\n",
    "        self.__month = date[0:2]\n",
    "        self.__day = date[3:5]\n",
    "        self.__year = date[6:10]\n",
    "        self.hour = date[11:13]\n",
    "        self.minute = date[14:16]\n",
    "        self.second = date[17:19]\n",
    "    def get_datetime(self,month_first = True):\n",
    "        if month_first == False:\n",
    "            return f\"It's {self.__day}, {self.__month} {self.__year} at {self.hour}:{self.minute} and {self.second} seconds \"\n",
    "        else:\n",
    "            return f\"It's {self.__month} {self.__day}, {self.__year} at {self.hour}:{self.minute} and {self.second} seconds \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's 10 10, 2020 at 12:11 and 22 seconds \n",
      "It's 10 10, 2020 at 12:11 and 22 seconds \n",
      "It's 10, 10 2020 at 12:11 and 22 seconds \n"
     ]
    }
   ],
   "source": [
    "# main program\n",
    "today = MyDate(\"10-10-2020 12:11:22\")\n",
    "print(today.get_datetime())\n",
    "print(today.get_datetime())\n",
    "print(today.get_datetime(month_first=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Challenge\n",
    "\n",
    "Modify <b>MyDate</b> class: \n",
    "\n",
    "    - to validate date & time (for month, days, hour, minute, and second). \n",
    "    - to add days\n",
    "    - to add hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyDate:\n",
    "    def __init__ (self, date):\n",
    "        self.__month = int(date[0:2])\n",
    "        self.__day = int(date[3:5])\n",
    "        self.__year = date[6:10]\n",
    "        self.__hour = int(date[11:13])\n",
    "        self.__minute = date[14:16]\n",
    "        self.__second = date[17:19]\n",
    "    def get_datetime(self,month_first = True):\n",
    "        if month_first == False:\n",
    "            return f\"It's {self.__day}, {self.__month} {self.__year} at {self.__hour}:{self.__minute} and {self.__second} seconds \"\n",
    "        else:\n",
    "            return f\"It's {self.__month} {self.__day}, {self.__year} at {self.__hour}:{self.__minute} and {self.__second} seconds \"\n",
    "    def add_day(self, day):\n",
    "        self.__day += day\n",
    "        return self.__day\n",
    "    def add_hour(self, hour):\n",
    "        self.__hour += hour\n",
    "        return self.__hour"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"It's 10 10, 2020 at 15:11 and 22 seconds \""
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "today = MyDate(\"10-10-2020 12:11:22\")\n",
    "\n",
    "\n",
    "today.add_hour(3)\n",
    "today.get_datetime()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "today.add_day(3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 1: \n",
    "Create a Temperature Converter program using OOP by creating a Temperature class with two private attributes to store Fahrenheit and Celsius degrees. In the Temperature class, define methods that \n",
    "- sets the private attributes. When you set one unit of temperature, it should calculate and set the other unit of temperature. For example, when you set degrees in Fahrenheit, it should calculate and set in Celsius degrees. \n",
    "- gets the hidden attributes that round the number to 2 decimal places. \n",
    "\n",
    "The output should look something like following:\n",
    "\n",
    "    MENU\n",
    "    1. Fahrenheit to Celsius\n",
    "    2. Celsius to Fahrenheit\n",
    "    3. Quit\n",
    "    \n",
    "    Enter a menu option: 1\n",
    "    Enter degrees in Fahrenheit: 99\n",
    "    99.00 oF is 37.22 oC.\n",
    "    \n",
    "    Enter a menu option: 2\n",
    "    Enter degrees in Celsius: 37.22\n",
    "    37.22 oC is 99.00 oF.\n",
    "    \n",
    "    Enter a menu option: 3\n",
    "    Bye\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Temp:\n",
    "    def __init__(self, degree, temp):\n",
    "        while degree != 1 and degree != 2:\n",
    "            degree = int(input(\"Please enter valid degree value, F is 1, C is 2\"))\n",
    "            if degree == 1 or degree == 2:\n",
    "                break\n",
    "        self.__degree = degree\n",
    "        self.__temp = temp\n",
    "    def FtoC(self):\n",
    "        if self.__degree == 1:\n",
    "            return round((self.__temp -32) *.5556, 2)\n",
    "    def CtoF (self):\n",
    "        if self.__degree == 2:\n",
    "            return round((self.__temp * 1.8) + 32, 2)\n",
    "\n",
    "    \n",
    "test1 = Temp(2,29)\n",
    "\n",
    "\n",
    "test1.FtoC()\n",
    "\n",
    "# test2 = Temp(2,59)\n",
    "\n",
    "# test2.CtoF()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_menu():\n",
    "    print(\"MENU\")\n",
    "    print(\"Fahrenheit to Celsius\")\n",
    "    print(\"Celsius to Fahrenheit\")\n",
    "    print(\"Quit\")\n",
    "    \n",
    "while True:\n",
    "    display_menu()\n",
    "    command = input(\"Command: \")\n",
    "    \n",
    "    if command == \"Fahrenheit to Celsius\":\n",
    "        degree = 1\n",
    "        temp = int(input(\"Tempurature: \"))\n",
    "        test = Temp(degree,temp)\n",
    "        print(test.FtoC())\n",
    "        break\n",
    "    elif command == \"Celsius to Fahrenheit\":\n",
    "        degree = 2\n",
    "        temp = int(input(\"Tempurature: \"))\n",
    "        test = Temp(degree,temp)\n",
    "        print(test.CtoF())\n",
    "        break\n",
    "    elif command == \"Quit\":\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 2: \n",
    "Create a <b>Privileges</b> class that has privileges, a private attribute. It can store a list of strings such as \"can add\", \"can delete\", and \"can modify\".  Write a method called show_privileges(). \n",
    "\n",
    "Create a class called <b>Admin</b> that inherits from the <b>Person</b> class (see next cell). Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person :\n",
    "    \n",
    "    def __init__(self, name, age, gender) :\n",
    "        self.__name = name\n",
    "        self.__age = age\n",
    "        self.__gender = gender\n",
    "\n",
    "    def get_name(self) :\n",
    "        return self.__name\n",
    "    \n",
    "    def get_info(self) :\n",
    "        return f\"Name: {self.__name}\\n Age: {self.__age}\\n Gender: {self.__gender}\"\n",
    "       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Privileges:\n",
    "    def __init__(self, privileges):\n",
    "        self.__privileges = privileges\n",
    "    def show_privileges(self):\n",
    "        return self.__privileges\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Admin(Person):\n",
    "    def __init__ (self, name, age, gender):\n",
    "        super().__init__(name,age,gender)\n",
    "        self.__privileges = \"can edit\"\n",
    "    def show_privileges(self):\n",
    "        return self.__privileges\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Name: Bryant\\n Age: 32\\n Gender: M'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "addy = Admin(\"Bryant\",32,\"M\")\n",
    "addy.get_info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'can edit'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "addy.show_privileges()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 3:\n",
    "1. Use the Product class from next cell\n",
    "2. Add get_description() method to Product class\n",
    "3. Create Book class inherited from the Product class. Add author attribute to the Book class and make modification to get_description() method\n",
    "4. Create Movie class inherited from the Product class. Add year attributes. Add/modify necessary methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# From Day 1 Class Demo\n",
    "class Product : \n",
    "    \"\"\"A simple attempt to model a product.\"\"\"\n",
    "    \n",
    "    def __init__(self, name, price, discount_rate) :\n",
    "        \"\"\"Initialize name, price, and discount_rate attributes\"\"\"\n",
    "        self.name = name\n",
    "        self.price = price\n",
    "        self.discount_rate = discount_rate\n",
    "        \n",
    "        \n",
    "    def get_discount_amount(self) :\n",
    "        \"\"\"Computes a discount calculation\"\"\"\n",
    "        return self.price * self.discount_rate / 100\n",
    "    \n",
    "        \n",
    "    def get_info(self) :\n",
    "        return(f\"Name: {self.name}\\n\" + \n",
    "                f\"Price: {self.price}\\n\" +\n",
    "                f\"Disicount Amount: ${self.get_discount_amount():,.2f}\\n\" +\n",
    "                f\"Discounted Price: ${self.get_sale_price():,.2f}\")\n",
    "    \n",
    "    def get_sale_price(self) :\n",
    "        \"\"\"Calls another method to find a sale price\"\"\"\n",
    "        return self.price - self.get_discount_amount()\n",
    "        \n",
    "    def get_description(self):\n",
    "        return f\"{self.name} sells for {self.price} with a discount rate of {self.discount_rate}\"\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The Illiad by Homer sells for $24 with a discount rate of 12%'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Book (Product):\n",
    "    def __init__(self, name, author, price, discount_rate):\n",
    "        super().__init__( name, price, discount_rate)\n",
    "        self.author = author\n",
    "    def get_author(self):\n",
    "        return self.author\n",
    "    def get_description(self):\n",
    "        return f\"{self.name} by {self.author} sells for {self.price} with a discount rate of {self.discount_rate}\"\n",
    "\n",
    "    \n",
    "book1 = Book(\"The Illiad\",\"Homer\",\"$24\",\"12%\")\n",
    "book1.get_description()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sleepless in Seattle from 1999 sells for $12 with a discount rate of 50%'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Movie (Product):\n",
    "    def __init__(self, name, year, price, discount_rate):\n",
    "        super().__init__( name, price, discount_rate)\n",
    "        self.year = year\n",
    "    def get_year(self):\n",
    "        return self.year\n",
    "    def get_description(self):\n",
    "        return f\"{self.name} from {self.year} sells for {self.price} with a discount rate of {self.discount_rate}\"\n",
    "\n",
    "    \n",
    "movie1 = Movie(\"Sleepless in Seattle\",\"1999\",\"$12\",\"50%\")\n",
    "movie1.get_description()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise 4\n",
    "Create a <b>MyDate</b> class with month, day, year, hour, minute, and second <b>private attributes</b>.  Create an initialization method that takes a string in the format of \"mm-dd-yyyy hh:mm:ss\". Also create necessary public methods as needed.  \n",
    "\n",
    "Then, run below program to show your class works:\n",
    "\n",
    "    today = MyDate(\"10-10-2020 12:11:22\")\n",
    "    print(today.get_datetime())\n",
    "    today.set_datetime(\"11-31-1999 02:33:22\")\n",
    "    print(today.get_datetime())\n",
    "    print(today.get_datetime(month_first=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyDate:\n",
    "    def __init__ (self, date):\n",
    "        self.__month = date[0:2]\n",
    "        self.__day = date[3:5]\n",
    "        self.__year = date[6:10]\n",
    "        self.hour = date[11:13]\n",
    "        self.minute = date[14:16]\n",
    "        self.second = date[17:19]\n",
    "    def get_datetime(self,month_first = True):\n",
    "        if month_first == False:\n",
    "            return f\"It's {self.__day}, {self.__month} {self.__year} at {self.hour}:{self.minute} and {self.second} seconds \"\n",
    "        else:\n",
    "            return f\"It's {self.__month} {self.__day}, {self.__year} at {self.hour}:{self.minute} and {self.second} seconds \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's 10 10, 2020 at 12:11 and 22 seconds \n",
      "It's 10 10, 2020 at 12:11 and 22 seconds \n",
      "It's 10, 10 2020 at 12:11 and 22 seconds \n"
     ]
    }
   ],
   "source": [
    "# main program\n",
    "today = MyDate(\"10-10-2020 12:11:22\")\n",
    "print(today.get_datetime())\n",
    "print(today.get_datetime())\n",
    "print(today.get_datetime(month_first=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Challenge\n",
    "\n",
    "Modify <b>MyDate</b> class: \n",
    "\n",
    "    - to validate date & time (for month, days, hour, minute, and second). \n",
    "    - to add days\n",
    "    - to add hours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyDate:\n",
    "    def __init__ (self, date):\n",
    "        self.__month = date[0:2]\n",
    "        self.__day = date[3:5]\n",
    "        self.__year = date[6:10]\n",
    "        self.__hour = date[11:13]\n",
    "        self.__minute = date[14:16]\n",
    "        self.__second = date[17:19]\n",
    "    def get_datetime(self,month_first = True):\n",
    "        if month_first == False:\n",
    "            return f\"It's {self.__day}, {self.__month} {self.__year} at {self.__hour}:{self.__minute} and {self.__second} seconds \"\n",
    "        else:\n",
    "            return f\"It's {self.__month} {self.__day}, {self.__year} at {self.__hour}:{self.__minute} and {self.__second} seconds \"\n",
    "    def add_day(self, day):\n",
    "        (self.__day) =+ day\n",
    "    def add_hour(self, hour):\n",
    "        (self.__hour) =+ hour"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "today = MyDate(\"10-10-2020 12:11:22\")\n",
    "\n",
    "\n",
    "print(today.add_hour(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
