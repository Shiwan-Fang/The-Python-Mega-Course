#课程第八节，将之前学习的内容结合起来building a program
def sentence_maker(phrase):
    capitalized = phrase.capitalize()  # 让一个句子的首字母大写
    if phrase.startswith(("how", "what", "why")):  # 或者将括号里的替换成 interrogatives疑问词
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:  # 可以不用while里面插入if，而是创建一个函数，在这个循环里call这个函数就可以（拆解成几个模块，而不是混在一起）
    user_input = input("Say something: ")  # 在函数里放这一行是不行的，如果要放，需要call这个函数？
    if user_input == "/end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))  # 在results的每一项里面加一个空格
