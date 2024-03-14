# 2. INTRO TO PYTHON II: FUNCTIONS & BASIC DATA STRUCTURES
def reverse_fruits(array):
    for i in range(len(array)-1, -1, -1):
        print(array[i])


def main():
    fruits = ["Apples", "Cantaloupe", "Grapes", "Strawberries"]
    fruits[0] = 'Oranges'
    print(fruits)


main()


