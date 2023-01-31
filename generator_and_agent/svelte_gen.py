
import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import sys
from dotenv import load_dotenv
load_dotenv()


OPENAI_KEY = os.getenv("OPENAI_API_KEY")


def submit_form(fn, file_path):
    os.environ["OPENAI_API_KEY"] = OPENAI_KEY
    llm = OpenAI(temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["component"],
        template="Create a " + fn + " component for: {component}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    if not os.path.exists('myapp'):
        with open(file_path, "r") as f:
            question_list = [line.strip() for line in f]
        # create components folder but only if it doesn't exist
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
        # chnage back to root directory
        os.chdir("..")
        # npm init @svelte-add/kit@latest my-new-app -- --with typescript+eslint
        print("directory is", os.getcwd())
        os.system(
            "npm create svelte@latest myapp  && cd $_")
        # send commands to svelte cli in the terminal
        # cd myapp
        os.chdir("myapp")
        # npm i
        os.system("npm i")
        # move components folder into src directory
        os.system("mv ../components src")

        # npm run dev
        os.system("npm run dev")
    else:
        print("myapp already exists")

        with open(file_path, "r") as f:
            question_list = [line.strip() for line in f]
        # create components folder but only if it doesn't exist
        # cd myapp/src/components
        os.chdir("myapp/src")
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


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python svelte_gen.py <file_extension> <file_path>")
        sys.exit(1)

    fn = sys.argv[1]
    file_path = sys.argv[2]
    submit_form(fn, file_path)


# list of external dependencies
# langchain
# dotenv
# openai
