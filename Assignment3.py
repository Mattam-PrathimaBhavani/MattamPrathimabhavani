class Department:
    depart_count = 0
    id_counter = 5001 # Starting Department ID

    def __init__(self, name, location):
        self.dept_id = Department.id_counter
        self.name = name
        self.location = location
        Department.depart_count += 1
        Department.id_counter += 1

    def display_department_info(self):
        print("Depart Information:")
        print("------------------------")
        print(f"Id: {self.dept_id}")
        print(f"name: {self.name}")
        print(f"location: {self.location}")

    @classmethod
    def get_total_departments(cls):
        return cls.depart_count


# Dictionary to store departments {dept_id: Department}
departments = {}

# i -> take users input
# ii -> take no of users
num = int(input("How many departments do you want to add? "))

# iii -> create a list or dictionary to store different department
for _ in range(num):
    name = input("Enter depart name: ")
    location = input("Enter depart location: ")

    dept = Department(name, location)
    departments[dept.dept_id] = dept
    print(f"Department {dept.dept_id} added successfully!\n")


print("\n--- All Departments ---")
for dept in departments.values():
    dept.display_department_info()

print(f"\nTotal Departments in Organization: {Department.get_total_departments()}")

def search_by_id(dept_id):
    if dept_id in departments:
        departments[dept_id].display_department_info()
    else:
        print(f"No department found with ID {dept_id}")


def search_by_name_contains(partial_name):
    found = False
    for dept in departments.values():
        if partial_name.lower() in dept.name.lower():
            dept.display_department_info()
            found = True
    if not found:
        print("No matching department found.")


while True:
    print("\n--- Department Search Menu ---")
    print("1. Search by Department ID")
    print("2. Search by Department Name (contains)")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            search_id = int(input("Enter Department ID to search: "))
            search_by_id(search_id)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        name_part = input("Enter part of the department name to search: ")
        search_by_name_contains(name_part)
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid!!Please try again.")


