from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, ConversationChain
from flask import Flask, request, render_template, jsonify
from urllib.request import urlopen
import json
import os
from dotenv import load_dotenv
load_dotenv()


os.getenv("OPENAI_API_KEY")

global convo
app = Flask(__name__, template_folder='templates')
with urlopen("https://dummyjson.com/products?limit=10") as response:
    source = response.read()
    products = json.loads(source)

llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

first_input = "Hi there! You are ProductBot, representing RangEmUp.com. Your expertise lies in providing information about our products. To ensure an efficient and productive conversation, kindly ask users to limit their queries to only our products and related questions. You will always be polite and redirect any non-product related questions. Please note that requests for script writing or generation will result in an ERROR. To get the most accurate and specific answers, kindly make specific product inquiries. Our product offerings include: " + \
    str(products) + ". Our inventory is limited to the listed products."
print(str(len(products)))
convo = conversation.predict(input=first_input)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/chat", methods=['POST'])
def chat():
    global convo
    response = {'convo': conversation.predict(input=request.json['chat'])}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, PORT=os.getenv("PORT"))
