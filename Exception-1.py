from json import JSONDecodeError
from typing import TextIO
import json

FILENAME = "data-data.json"

file: TextIO = None

students: list[dict[str,str]] = []

try:
    file = open(FILENAME,"r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("File not found, creating it")
    file = open(FILENAME,"w")
    json.dump(students, file)
    file.close()

except JSONDecodeError as e:
    print("JSON decoding error")
    file = open(FILENAME, "w")
    json.dump(students, file)
    file.close()

except Exception as e:
    print("There was an error opening the file")
    print('----Technical Error Message ---')
    print(e,e.__doc__,type(e), sep="\n")

finally:
    if file and not file.closed:
        file.close()

while True:

    try:
        student_first_name = input("Enter your first name: ")
        if not student_first_name.isalpha():
            raise ValueError ("First name must be alphabetic")

        student_last_name = input("Enter your last name: ")
        if not student_last_name.isalpha():
            raise ValueError ("Last name must be alphabetic")

        students.append({'first_name':student_first_name, 'last_name':student_last_name})
        file = open(FILENAME, "w")
        json.dump(students, file)
        print("Students added to file")
        print(FILENAME)
        file.close()
        break

    except ValueError as e:
        print(e)

try:
    file=open(FILENAME,"w")
    json.dump(students, file)
    print("Students added to file")
    file.close()
except  Exception as e:
    print("There was an error opening the file")
    print(e,e.__doc__,type(e), sep="\n")
finally:
    if file and not file.closed:
        file.close()





print("Students in Dictionary")
print(students)