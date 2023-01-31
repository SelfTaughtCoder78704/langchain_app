
from langchain import OpenAI, ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
import os
OPENAI_KEY = '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'
# ORGANIZATION='org-8u6gOmKjVAu4QwWNIZ7B7MmM'
os.environ["OPENAI_API_KEY"] = "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" 


from urllib.request import urlopen
import json

with urlopen("https://dummyjson.com/products?limit=10") as response:
    source = response.read()

products = json.loads(source)

first_input = 'Your name is now: ProductBot and you work for RangEmUp.com. Here is a list of products, from now on only talk about the products and questions related to them. Always be polite, but anything not about our products shall be redirected. Products: ' + \
    str(products)


start_up = input("Press Enter To Begin")

llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)


# conversation.predict(input=first_input)
# while True:
#     next_input = input("Chat: ")
#     conversation.predict(input=next_input)

print(conversation.predict(input=first_input))
while True:
    next_input = input("Chat: ")
    print(conversation.predict(input=next_input))

