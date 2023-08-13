
# import openai 

# def chatgpt(question):
#     openai.api_key = "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"

#     model_engine = "text-davinci-003"
#     prompt = "" + question + ""

#     completion = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     response = completion.choices[0].text
#     return response


# print(chatgpt("what is the size of the universe"))
# # enter your question below like above 
# print(chatgpt("your question"))




import openai 

def chatgpt(what_you_want_to_ask_about_data, question):
    openai.api_key = "your openai secret key here"

    model_engine = "text-davinci-003"
    prompt = ""+what_you_want_to_ask_about_data+" in this '" + question + "'"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response


print(chatgpt("what is the size of the universe"))
# enter your question below like above 
what_you_want_to_know_about_data = '''your question here'''
your_data = '''your data here'''
print(chatgpt("your_data", "what_you_want_to_know_about_data"))




# do not show the line below
# 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


# import site
# print(site.getsitepackages())














# print('python works')
# for i in range(1, 101):
#     print(i)
# import sys

# print(sys.executable)