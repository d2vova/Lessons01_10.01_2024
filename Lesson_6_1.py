people = [
    {
        "name": "John",
        "age": 13
    },
    {
        "name": "Nick",
        "age": 14
    },
    {
        "name": "Bob",
        "age": 18
    },
    {
        "name": "Jackkkk",
        "age": 45}]

min_age = min(person["age"] for person in people)
youngest_names = [person["name"] for person in people if person["age"] == min_age]
max_name_length = max(len(person["name"]) for person in people)
longest_names = [person["name"] for person in people if len(person["name"]) == max_name_length]
tot_age = sum(person["age"] for person in people)
tot_people = len(people)
tot_average = tot_age/tot_people if tot_people > 0 else 0

print("a) youngest people: ", youngest_names)
print("b) longest name: ", longest_names)
print("c) average age: ", tot_average)