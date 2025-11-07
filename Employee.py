# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
class Employee:

    def __init__(self, name, id_num, department, job_title):

        self._name = name
        self._id_number = id_num
        self._department = department
        self._job_title = job_title

    def __str__(self):
        return (f"Name: {self._name}\n"
                f"ID Number: {self._id_number}\n"
                f"Department: {self._department}\n"
                f"Job Title: {self._job_title}")

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

def main():
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    print("--- Employee Database Records ---")
    
    print("\nEmployee 1:")
    print(employee1)
    print("\nEmployee 2:")
    print(employee2)
    print("\nEmployee 3:")
    print(employee3)
    
    print("-" * 35)

if __name__ == '__main__':
    main()