
# returns the type of greeting where 1, 2, 3, are different type of greeting
def greetings(typ):
    print("============================================================")
    if typ == 0:
        print("Hi there, \nWelcome to the best teaching pratice for kids!!!")
    elif typ == 1:
        print("Welcome to Baby's First Words Teaching Game!")
    elif typ == 2:
        print("Welcome to the Baby Math Game!")
    else:
        print("Welcome to the Quiz section!")
    print("============================================================")


# 2. a function to read out the questions
# which typ Game

# this function takes in an interger specifying the type of response that should be created and returns a response in integer format
def questions(typ):
    if typ == 1:
        # ask a question for what type of game the user wants
        response = int(input(
            "What section of the Game do you want to play?\nPlease enter 1 or 2 or 3 or 4 as a response\n1.Words Game.\n2.Math Game. \n3. The Quiz\n4. Educational Videos"))
    elif typ == 2:
        # ask for the age range that the user want
        response = int(
            input("What age range do you want?\nPlease enter 1 or 2 as a response\n1.1-4 years old.\n2.5-8 year old"))
    elif typ == 3:
        response = int(input("What Quiz type do you want?\n1. Word Quiz\n2. Math Quiz\n3. Both Word and Math Quiz"))

    return response


def end_game():
    res = int(input("Enter:\n1. To repeat this section.\n2. To go another section.\n3. To End Game"))
    return res


# a function/variable name that holds a list of words for each
# this function reads a csv file and return
def readcsv(typ):
    import pandas
    if typ == 1:
        # the math part for 1-4 year old
        data = pandas.read_csv(r"english_young.csv")
    elif typ == 2:
        data = pandas.read_csv(r"english_sen.csv")
    elif typ == 3:
        # the math part for 5-8 year old
        data = pandas.read_csv(r"math_young.csv")
    elif typ == 4:
        data = pandas.read_csv(r"math_sen.csv")

    # return a dictionary that maps the column name the values (string or integers) in the column
    dictionary_data = {}
    for col in data:
        dictionary_data[col] = list(data[col])

    return dictionary_data




# the dictionaries
"""
return {1: {1: ["A is for A P P L E Apple"], 2: ["word means ......],}
2: {1: ["1 + 1 = 2"], 2: ["15/5 = 3"]},
# 1 represents english 
3: {1: {1: [A is for what?\n Apple\n Egg], 2: ["What is the meaning of word* "]}
    2: {1: ["1 + 1 = "]
        2: ["15/ 5 = "]}}
"""


def getString(number):
    result = []
    diction = readcsv(number)

    if number == 1:
        for i in range(len(diction["letter"])):
            result.append(diction["letter"][i] + ": " + diction["sentence"][i])
    elif number == 2:

        for i in range(len(diction["word"])):
            result.append(diction["word"][i] + ": " + diction["word"][i] + " means " + diction["definition"][i])
    elif number == 3:
        #         len_a = len(data["letter"])
        for i in range(len(diction["num1"])):
            result.append((str(list(diction["num1"])[i]) + " " + str(list(diction["operation"])[i]) + " " + str(
                list(diction["num2"])[i]) + " = " + str(diction["result"][i])))
    else:

        for i in range(len(diction["num1"])):
            result.append((str(diction["num1"][i]) + " " + str(diction["operation"][i]) + " " + str(
                diction["num2"][i]) + " = " + str(diction["result"][i])))

    return result


def files():
    result = {1: {},
              2: {},
              3: {1: {1: [], 2: []}, 2: {1: [], 2: []}}}

    # English
    list_en_young = getString(1)
    result[1][1] = list_en_young

    list_en_sen = getString(2)
    result[1][2] = list_en_sen

    # Math
    list_ma_young = getString(3)
    result[2][1] = list_ma_young

    list_ma_sen = getString(4)
    result[2][2] = list_ma_sen

    # Quiz

    return result


# spell out the world
# given word = "APPLE"
# return "name_alphabet is spelt then A P P L E"
def spellWords(word):
    letters = ' '
    for char in word:
        letters += char + " "

    return letters


# this function takes in the a string and return
def readSentence(sen):
    # Import the required module for text
    # to speech conversion
    import pyttsx3

    pytt = pyttsx3.init()

    pytt.say(sen)
    pytt.setProperty("rate", 120)
    pytt.runAndWait()


def operations():
    ques1 = questions(1)
    greetings(ques1)
    ques2 = questions(2)
    return (ques1, ques2)


def breakQues():
    res = int(input("Enter 1 or 2 or 0:\n1 Do you want to repeat?\n2 Do you want to go to another section?\n0 Exite"))

    if res == 0:
        return (res, res)
    return (res, 1)


def section(tup):
    names = ["english_young", "english_sen", "math_young", "math_sen"]
    if tup[0] == 1:
        if tup[1] == 1:
            return names[0]
        else:
            return names[1]
    elif tup[0] == 2:
        if tup[1] == 1:
            return names[2]
        else:
            return names[3]


# this fuction generates a random number from 0 to 7 within the length of the array
def indexs(section, age):
    import random

    diction = files()
    stop_point = len(diction[section][age])

    list_nums = []
    print(stop_point)
    i = 0
    while i < 7:
        index = random.randint(0, stop_point - 1)
        if index not in list_nums:
            list_nums.append(index)
            i += 1
    return list_nums


def quizes():
    questions = {1: {1: [[], []], 2: [[], []]}, 2: {1: [[], []], 2: [[], []]}}
    diction1 = readcsv(1)
    diction2 = readcsv(2)
    diction3 = readcsv(3)
    diction4 = readcsv(4)

    index = indexs(1, 1)
    print(index)
    for i in index:
        questions[1][1][0].append("What is the first letter in  " + diction1["word"][i])
        questions[1][1][1].append(diction1["letter"][i])

    index = indexs(2, 1)
    for i in index:
        questions[1][2][0].append("What means " + diction2["definition"][i])
        questions[1][2][1].append(diction2["word"][i])

        questions[2][1][0].append(
            str(list(diction3["num1"])[i]) + " " + str(list(diction3["operation"])[i]) + " " + str(
                list(diction3["num2"])[i]) + " = ")
        questions[2][1][1].append(str(diction3["result"][i]))

        questions[2][1][0].append(
            str(list(diction4["num1"])[i]) + " " + str(list(diction4["operation"])[i]) + " " + str(
                list(diction4["num2"])[i]) + " = ")

        questions[2][1][1].append(str(diction4["result"][i]))

    return questions
    # nit returns 


def correct(correct_ans, answers):
    count = 0
    for i in range(len(answers)):
        if correct_ans[i].lower() == answers[i].lower():
            count += 1

    print("You got " + str(count) + " correct!")


# Extension
def playVideo(age):
    diction = {1: ["https://youtu.be/e_04ZrNroTo", "https://www.youtube.com/watch?v=yseWMJS8IHw", "https://www.youtube.com/watch?v=Mt_CIBlEGos"], 2:["https://www.youtube.com/watch?v=PJ7LBQo_t58", "https://www.youtube.com/watch?v=jQ2e0KH5WrI", "https://www.youtube.com/watch?v=OmQ0WJKvNe0"]}
    import vlc
    import pafy

    index = videoName(age)

    url = diction[age][index]
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)

    media.play()

def videoName(age):

    if age == 1:
        ques = input("Enter 1 or 2 or 3\n1. Wheels on the bus go round.\n2. Abc song.\n3. Funny face song")
    else:
        ques = input("Enter 1 or 2 or 3\n1. What is time?.\n2. Personal Hygiene.\n3. Bullying.")
    return int(ques)