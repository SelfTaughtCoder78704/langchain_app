import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import sys
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def generate_components(fn, file_path):
    os.environ["OPENAI_API_KEY"] = OPENAI_KEY
    llm = OpenAI(temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["component"],
        template="Create a " + fn + " component for: {component}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    with open(file_path, "r") as f:
        question_list = [line.strip() for line in f]
    # create components folder if it doesn't exist
    if not os.path.exists("components"):
        os.mkdir("components")
    # move into components folder
    os.chdir("components")
    for thing in question_list:
        parts = thing.split(":")
        if len(parts) < 2:
            print("Invalid input:", thing)
            continue
        file_name = parts[1].split(" -")[0].strip() + fn
        print(file_name)
        with open(file_name, "w") as f:
            f.write(chain.run(thing))

    # change back to root directory
    os.chdir("..")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python component_gen.py <file_extension> <file_path>")
        sys.exit(1)
    fn = sys.argv[1]
    file_path = sys.argv[2]
    generate_components(fn, file_path)


# setup: source myenv/bin/activate
# python just_components.py .svelte questions.txt