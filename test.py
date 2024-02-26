questions = {
    1: [
        ("hello world", 2),
        ("lorem ipsum dolor sit amet", 5),
        ("testing the code you wrote", 5),
    ]
}


def test(qid, func):
    assert callable(func), "Error ask for help"

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
