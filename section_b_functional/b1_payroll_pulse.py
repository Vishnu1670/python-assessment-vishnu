# num = [1,2,3,4]
# result = map(lambda x:x*2,num)
# print(list(result))

# names = ["vishnu", "arun", "divya"]
# res = list(map(lambda name: name.upper(),names))
# print(res)

# nums = [5, 10, 15]
# res = list(map(lambda num: num+10,nums))
# print(res)

# num = [1, 2, 3, 4]
# res = list(map(lambda x: x*x,num))
# print(res)

# wor =["HELLO", "WORLD"]
# res = list(map(lambda x:x.lower(),wor))
# print(res)

# ad = [30000, 40000, 50000]
# res = list(map(lambda x:x+5000,ad))
# print(res)

# nums=[1,2,3,4,5,6,7,8,9,10]
# res = list(filter(lambda x: x % 2 == 0, nums))
# print(res)

# names = ["Ram", "Vishnu", "Arun", "Raj"]
# res = list(filter(lambda x: len(x) > 4,names))
# print(res)

from functools import reduce


employees = [
    {"id": 1, "name": "Aarav",   "dept": "Engineering", "salary": 75000,  "experience": 4},
    {"id": 2, "name": "Bhavna",  "dept": "Sales",       "salary": 55000,  "experience": 2},
    {"id": 3, "name": "Charan",  "dept": "Engineering", "salary": 90000,  "experience": 6},
    {"id": 4, "name": "Divya",   "dept": "HR",          "salary": 48000,  "experience": 3},
    {"id": 5, "name": "Eswar",   "dept": "Engineering", "salary": 120000, "experience": 8},
    {"id": 6, "name": "Farah",   "dept": "Sales",       "salary": 65000,  "experience": 5},
    {"id": 7, "name": "Gokul",   "dept": "HR",          "salary": 52000,  "experience": 4},
    {"id": 8, "name": "Hema",    "dept": "Engineering", "salary": 85000,  "experience": 5},
]


#Apply Hike using map()
def apply_hike(employees, percentage):

    return list(map(lambda emp: {**emp,"salary": emp["salary"] + (emp["salary"] * percentage / 100)},employees))


#Eligible for Bonus using filter()
def eligible_for_bonus(employees):

    return list(filter(lambda emp:emp["experience"] >= 5 and emp["salary"] < 100000,employees))


# Total Salary using reduce()
def total_salary(employees):

    return reduce(lambda total, emp: total + emp["salary"],employees,0)


#Group by Department using comprehension
def group_by_department(employees):

    departments = {emp["dept"] for emp in employees}

    return {dept: list(filter(lambda emp: emp["dept"] == dept,employees))
        for dept in departments
    }


# Top N Earners using sorted()
def top_n_earners(employees, n):

    return sorted(employees,
        key=lambda emp: emp["salary"],
        reverse=True
    )[:n]



# Compose Functions
def compose(*funcs):

    return lambda x: reduce(
        lambda value, func: func(value),
        reversed(funcs),
        x
    )


# Apply 10% hike
hiked = apply_hike(employees, 10)

print("Total Salary After Hike:")
print(total_salary(hiked))


print("\nEligible for Bonus:")

bonus_list = eligible_for_bonus(employees)

print([e["name"] for e in bonus_list])


print("\nTop 3 Earners:")

top3 = top_n_earners(employees, 3)

print([e["name"] for e in top3])


print("\nGrouped by Department:")

grouped = group_by_department(employees)

for dept, emp_list in grouped.items():

    print(dept, ":", [emp["name"] for emp in emp_list])


print("\nFunction Composition:")

pipeline = compose(
    eligible_for_bonus,
    lambda emps: apply_hike(emps, 10)
)

print([e["name"] for e in pipeline(employees)])