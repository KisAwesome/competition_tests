def test(qid, func):
    questions = {
        1: [
            ("hello world", 2),
            ("lorem ipsum dolor sit amet", 5),
            ("testing the code you wrote", 5),
        ]
    }

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
        print("All tests passed good job!")
