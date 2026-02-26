
import pandas
import re
import json
import math
print(max(5, 10))
print(min(5, 10))
print(abs(-7))
print(pow(3, 2))

print(int(math.sqrt(16)))
print(round(3.7))
print(math.ceil(3.2))
print(math.floor(3.7))
print(math.pi)

data = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(data)
print(parsed_data['name'])
print(data)

object = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(
    object, indent=4, separators=(". ", " + "), sort_keys=True)
print(json_data)

txt = "The Rain in Spain"
c = re.search("^The.*Spain$", txt)
if c:
    print("YES! We have a match!")
else:
    print("No match")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Change 2 to 20
matrix[0][1] = 20
print(matrix)

for row in matrix:
    for item in row:
        print(item)


numbers = [2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


f_string = f"the private number is 0909"
print(f_string)
df = pd.read_csv("./data/dataset - 2020-09-24.csv")
print(df)
