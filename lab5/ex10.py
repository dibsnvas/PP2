import re
def camel_to_snake(camel_case):
    res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case)
    return res.lower()

camel = "DianaIsBest"
snake_case = camel_to_snake(camel)

print(f"{snake_case}")
