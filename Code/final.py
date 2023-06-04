# # def function(n):
# #     for i in range(n):
# #         for j in range(n, n*2):
# #             print(i*j)

# # function(10)


# # def unique_elements_as_tuple(lst):
# #     unique_elements = tuple(set(lst))
# #     return unique_elements

# # lst = ["ball", "dog", "mouse", "apple", "dog"] 
# # print(type(unique_elements_as_tuple(lst)))
# # print(unique_elements_as_tuple(lst))

# # Problem 5
# def Primes(n):
#     primes = []
#     for num in range(2, n):
#         if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#             primes.append(num)
#     return primes

# print(len(Primes(100)) == 25)
# print(Primes(100))

# def Goldbach(n, primes):
#     for i in primes:
#         for j in primes:
#             if i + j == n:
#                 return (i, j)
#     return None

# print(Goldbach(12, Primes(12)))

# Problem 6
def read_towns_file(filename):
    towns = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    town, population = line.split(', ')
                    towns[town] = int(population)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print("An error occurred:", str(e))
    return towns


# filename = "./filename.txt"
# print(read_towns_file(filename))

def get_town_population(towns):
    town_name = input("Enter the name of a town: ")
    population = towns.get(town_name)
    
    if population is not None:
        print("Population of", town_name + ":", population)
    else:
        print("Town not found.")

def calculate_total_population(towns):
    total_population = sum(towns.values())
    print("Total population of the district:", total_population)

# Main program
filename = "./filename.txt"
Towns = read_towns_file(filename)
if Towns:
    get_town_population(Towns)
    calculate_total_population(Towns)

