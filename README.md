# langchain_app
* The main.py file is a flask server that has an index route. It also has a /chat endpoint. This fetches products from an exteranl link, then sends them along with
instructions to the AI to only speak about them from now on.
* The folder with the generator and the agent are 2 different apps. 
  * The agent can perform searches and math. 
  * The generator can read a text file, create components, create a svelte app, copy the components into the src dir of the svelte app and then run the app.


TO USE ANY OF THESE SCRIPTS YOU NEED TO CREATE .env and add your OPENAI_API_KEY.
TO use the Search tool in the agent.py, you need to also get a serpapi api key and set it in .env as SERPAPI_API_KEY
