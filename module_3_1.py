calls =0
def count_calls():
    global calls
    calls += 1


def string_info (string):
    count_calls()
    return (len(string)), string.upper(), string.lower()


def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [i.upper() for i in list_to_search]

print(string_info('Капибара'))
print(string_info('Конец света'))
print(is_contains('Urban',['ban', 'BaNaN','urBAN']))
print(is_contains('цикл', ["рецикл","цикличность"]))
print(calls)