from litellm import completion
from dotenv import load_dotenv


# Load API keys from .env file
load_dotenv()

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"content": "Hello, How are you Do you know me?", "role": "user"}]
    )
    # response ek object hai, ismein se message content access karen
    print(response.choices[0].message.content)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)

if __name__ == "__main__":
   
    gemini()

#  Short Description:
#  Here i used two API (Open AI and Gemini), you can use any of them.
#  You can also use both of them, just uncomment the function you want to use.
#    openai()
#    gemini()

#  To run this code, you need to have a .env file with your API keys.
#  Example of .env file:
#  OPENAI_API_KEY=your_openai_api_key
#  GEMINI_API_KEY=your_gemini_api_key
#  You can also used Gemini2 by using the gemini2's secret key. 