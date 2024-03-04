import random
import string


def is_valid_brackets(brackets):
    stack = []
    brackets_map = {")": "(", "}": "{", "]": "["}

    for bracket in brackets:
        if bracket in brackets_map.values():
            stack.append(bracket)
        elif bracket in brackets_map:
            if not stack or stack.pop() != brackets_map[bracket]:
                return False

    return not stack


def random_brackets():
    x = (")", "(", "}", "{", "]", "[")
    n = ""
    for i in range(random.randint(0, 100)):
        n += random.choice(x)
    return (n, is_valid_brackets(n))


def generate_random_letters(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def generate_random_int_array(length, start_range, end_range):
    return [random.randint(start_range, end_range) for _ in range(length)]


def is_palindrome(input_str):
    cleaned_str = "".join(input_str.split()).lower()
    return cleaned_str == cleaned_str[::-1]


def generate_palindrome_case():
    x = generate_random_letters(random.randint(1, 100)).lower()
    return (x, is_palindrome(x))


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def generate_tip_cases():
    x = random.randint(1, 10000)
    return (x, x * 1.15)


def gen_rand_test_average_calculator():
    t = []
    x = []
    for i in range(random.randint(1, 100)):
        g = random.randint(0, 10000)
        t.append(str(g))
        x.append(g)

    return (",".join(t), average(x))


def calculate_median(arr):
    sorted_arr = sorted(arr)
    length = len(sorted_arr)

    if length % 2 == 1:
        median = sorted_arr[length // 2]
    else:
        mid1 = length // 2 - 1
        mid2 = length // 2
        median = (sorted_arr[mid1] + sorted_arr[mid2]) / 2

    return median


def generate_median_array_case():
    x = generate_random_int_array(random.randint(1, 1000), 0, random.randint(2, 1000))
    x2 = generate_random_int_array(random.randint(1, 1000), 0, random.randint(2, 1000))

    return ((x, x2), calculate_median(x + x2))


def generate_random_ip_case():
    return (
        f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}",
        True,
    )


questions = {
    1: [
        ("hello world", 2),
        ("lorem ipsum dolor sit amet", 5),
        ("testing the code you wrote", 5),
        ("Hello\te", 2),
        ("hello      testing\tg", 3),
    ],
    2: [gen_rand_test_average_calculator() for i in range(20)],
    3: [
        ("192.168.1.1.1", False),
        ("256.1.1.1", False),
        ("21", False),
        ("256.434", False),
        ("400.400.400.400", False),
        *[generate_random_ip_case() for i in range(20)],
    ],
    4: [generate_tip_cases() for i in range(50)],
    5: [
        ("racecar", True),
        ("eye", True),
        ("rotor", True),
        ("mom", True),
        ("dad", True),
        ("radar", True),
        *[generate_palindrome_case() for i in range(44)],
    ],
    6: [generate_median_array_case() for i in range(50)],
    7: [
        *[random_brackets() for i in range(42)],
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("[", False),
        ("]", False),
        (")", False),
        ("}", False),
        ("[}{", False),
    ],
}


def test(qid, func):
    assert callable(func), "Error ask for help"
    print("Running test for question", qid)
    passes = 0

    for tid, i in enumerate(questions[qid]):
        if isinstance(i[0], tuple):
            ret = func(*i[0])
        else:
            ret = func(i[0])

        if len(i) > 2:
            stat = i[2](i[1], ret)
        else:
            stat = i[1] == ret
        if stat:
            passes += 1
        else:
            print("Error function failed test id", tid)
    print()
    if len(questions[qid]) == passes:
        print(f"passed {passes}/{passes} test cases")
        print("All tests passed good job!")
    else:
        print(f"passed {passes}/{len(questions[qid])} test cases")
        print("Could not validate your code please debug and try again")


def interactive_debug():
    while True:
        inp = input("Enter question number to debug: ")
        if inp.isdigit():
            if int(inp) not in questions:
                print("Question number does not exist")
                continue
            return int(inp)
        print("Input must be a number")
