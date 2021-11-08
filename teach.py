from teachFiles import files, greetings, operations, quizes, breakQues, correct, readSentence, playVideo
def teach():

    learning_data = files()
    greetings(0)
    end_game = 1

    while end_game != 0:
        res = operations()
        print(res)
        section = 1
        #     name = section(res)
        if res[0] == 3:
            while section != 2 and end_game != 0:

                questions = quizes()[1][res[1]]
                result = []
                print(questions)
                print(
                    "***********************************************************\n***********************************************************\n")
                for ques in questions[0]:
                    ans = input(ques)
                    result.append(ans)
                print(
                    "\n***********************************************************\n***********************************************************")

                print(
                    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nRESULT\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                correct(questions[1], result)
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                break_k = breakQues()
                end_game = break_k[1]
                section = break_k[0]


        elif res[0] == 4:
            playVideo(res[1])
        else:
            while section != 2 and end_game != 0:

                print(
                    "***********************************************************\n***********************************************************\n")
                for text in learning_data[res[0]][res[1]]:
                    print(text + "\n")
                    readSentence(text)
                print(
                    "\n***********************************************************\n***********************************************************")
                break_k = breakQues()
                end_game = break_k[1]
                section = break_k[0]
teach()