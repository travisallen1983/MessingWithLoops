import random


def upcoming_loop():
    shows = {"April 23rd": "Pears", "May 4th": "Sick Of It All, Agnostic Front, & Crown Of Thornz", "May 7th": "Hatebreed",
             "May 24th": "Lagwagon & Less Than Jake", "June 23rd": "Circle Jerks, The Adolescents, & Negative Approach"}
    print("---------------")
    print("UPCOMING SHOWS")
    print("---------------")
    for date, show in shows.items():
        print(date + " : " + show)


def numbers_loop():
    for i in range(1, 1045, 13):
        if i < 33:
            print(i, "||", (i + (i/33)))
        elif i < 73:
            print(i, "||", (i + (i / 13)))
        elif i < 133:
            print(i, "||", (i + (i % 5)))
        elif i < 333:
            print(i, "||", (i + (i/337)))
        elif 556 < i < 780:
            continue
        else:
            print(i, "||", (i + i + i))


def rand_band():
    bands = ["Circle Jerks", "Lagwagon", "Madball", "Bad Cop Bad Cop", "PEARS", "Agnostic Front", "Western Addiction"]
    random_number = random.randint(0, len(bands) - 1)
    loops_list = []
    #loops_list = {}
    for i in range(len(bands)):
        if i == random_number:
            band = "The random number was " + str(i) + ". The band at index " + str(i) + " is " + str(bands[i]) + "."
        else:
            band = "The random number was " + str(random_number) + ". The index was " + str(i) + "."

        #loops_list.update({i: band})
        loops_list.append("Iteration " + str(i) + " : " + band)

    return loops_list[random.randint(0, len(bands) - 1)]


def new_loop():
    starting_number = 0
    ending_number = 140
    number_list_13 = []
    number_list_14 = []
    while starting_number <= ending_number:
        starting_number += 1
        if starting_number % 13 == 0:
            number_list_13.append(starting_number)
        if starting_number % 14 == 0:
            number_list_14.append(starting_number)
    for i in range(len(number_list_13)):
        divisible_13 = "The numbers in the list divisible by 13: " + str(number_list_13)
    for i in range(len(number_list_14)):
        divisible_14 = "The numbers in the list divisible by 14: " + str(number_list_14)

    return divisible_13, divisible_14


def none_loop():
    smallest = None
    rand_list = []
    for i in range(500):
        num = random.randint(15 * random.randint(4, 55), 1000)
        rand_list.append(num)
    for value in rand_list:
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
    return smallest, rand_list


def count_loop():
    count = 0
    for i in range(2, 2201, 31):
        count += 1
        print(str(count) + " : " + str(i))


def string_loop():
    count = 0
    lower_list = []
    upper_list = []
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    alphabet_lower = alphabet.lower()
    alphabet_capital = alphabet.upper()
    for char in alphabet_capital:
        count += 1
        upper_list.append(char)
    upper_list.reverse()
    for char in alphabet_lower:
        count += 1
        lower_list.append(char)
    lower_list.reverse()
    return count, upper_list, lower_list

def dict_count():
    counts = dict()
    names = ["Mike", "James", "Penny", "James", "Pearl", "Pearl", "Mika"]
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    print(counts)

def dict_get():
    counts = dict()
    names = ["Mike", "James", "Penny", "James", "Pearl", "Pearl", "Mika"]
    for name in names:
        counts[name] = counts.get(name, 0) + 1

    print(counts)

def word_count():
    counts = dict()
    line = input("Enter a line of text: ")
    words = line.split()

    print("Words:", words)
    print("Counting: ")

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print("Counts", counts)

def main():
    #print(upcoming_loop())
    #print(numbers_loop())
    #print(rand_band())
    #print(new_loop())
    #print(none_loop())
    #print(count_loop())
    #print(string_loop())
    #print(dict_count())
    #print(dict_get())
    print(word_count())

if __name__ == "__main__":
    main()