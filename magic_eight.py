import random

def question():
    response = input("What is your question?")

# B - pick a random answer
ans_list_b = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]

ans_b = random.choice(ans_list_b)
print(ans_b)

# Question_C answer is here:
answer_c_list =["Reply hazy, try again.","Ask  again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

answer_c_item = random.choice(answer_c_list)
print(answer_c_item)
