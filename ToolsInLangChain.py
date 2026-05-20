# from langchain_core.tools import tool

# @tool
# def add_numbers(a: int, b: int) -> int:
#     "Add two numbers"
#     return a + b

# print(add_numbers.name)           # add_numbers
# print(add_numbers.description)    # Add two numbers together.
# print(add_numbers.args)           # {'a': int, 'b': int}


# from langchain_core.tools import tool

# @tool
# def add_numbers(a: int, b: int) -> int:
#     "Add two numbers"
#     return a + b
# @tool
# def multiply_numbers(c: int, d: int) -> int:
#     "Multiply two nubmers"
#     return c * d

# @tool
# def get_weather(city: str) -> str:
#     "get weather for a city"
#     weather = {
#         "lahore": "35C Sunny",
#         "karachi": "32C Humid",
#         "islamabad": "28C Cloudy"
#     }
#     return weather.get(city, "City not found")


# print(add_numbers.invoke({"a": 3, "b": 4}))
# print(multiply_numbers.invoke({"c": 3, "d": 4}))
# print(get_weather.invoke({"city": "islamabad"}))


# from langchain_groq import ChatGroq
# from langchain_core.tools import tool
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# @tool
# def add_numbers(a: int, b: int) -> int:
#     "Add two numbers"
#     return a + b

# @tool
# def get_weather(city: str) -> str:
#     "get weather for a city"
#     weather = {
#         "lahore": "35C Sunny",
#         "karachi": "32C Humid",
#         "islamabad": "28C Cloudy"
#     }
#     return weather.get(city, "City not found")

# tools = [add_numbers, get_weather]

# llm_with_tools = llm.bind_tools(tools)

# response = llm_with_tools.invoke("what is 5 + 7")
# print(response.content)
# print(response.tool_calls)


# from langchain_groq import ChatGroq
# from langchain_core.tools import tool
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# @tool
# def add_numbers(a: int, b: int) -> int:
#     "Add two numbers"
#     return a + b

# @tool
# def get_weather(city: str) -> str:
#     "get weather for a city"
#     weather = {
#         "lahore": "35C Sunny",
#         "karachi": "32C Humid",
#         "islamabad": "28C Cloudy"
#     }
#     return weather.get(city.lower(), "City not found")

# tools = [add_numbers, get_weather]
# #tools_dict = {t.name: t for t in tools}
# tools_dict = {
#     "add_numbers": add_numbers,
#     "get_weather": get_weather
# }

# llm_with_tools = llm.bind_tools(tools)

# response = llm_with_tools.invoke("what is 4  + 7")

# if response.tool_calls:
#     for tool_call in response.tool_calls:
#         tool_name = tool_call["name"]
#         tool_args = tool_call["args"]
#         result = tools_dict[tool_name].invoke(tool_args)

#         print(f"Tool: {tool_name}")
#         print(f"Args: {tool_args}")
#         print(f"Result: {result}")
# else:
#     print(response.content)



#Ex1


# from langchain_core.tools import tool

# @tool
# def multiply(a, b):
#     "multiply 2 numbers"
#     return a * b

# @tool
# def square(n):
#     "square of number"
#     return n * n

# @tool 
# def is_even(e):
#     "check number is even"
#     if e%2==0:
#         return True
#     else:
#         return False
    
# print(multiply.invoke({"a": 6, "b": 6}))
# print(square.invoke({"n": 9}))
# print(is_even.invoke({"e": 7}))


#Ex2

# from langchain_groq import ChatGroq
# from langchain_core.tools import tool
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# @tool
# def get_population(country: str) -> str:
#     "population of country"
#     population = {
#         "pakistan": "230 million",
#         "india": "1.4 billion",
#         "usa": "330 million",
#     }
#     return population.get(country.lower(), "country not found")

# @tool
# def get_capital(country: str) -> str:
#     "capital of country"
#     capital = {
#         "pakistan": "Islamabad",
#         "india": "New Delhi",
#         "usa": "Washington DC",
#     }
#     return capital.get(country.lower(), "capital not found")

# tools = [get_population, get_capital]

# # tools_dict banao
# tools_dict = {
#     "get_population": get_population,
#     "get_capital": get_capital
# }

# llm_with_tools = llm.bind_tools(tools)

# response = llm_with_tools.invoke(
#     "What is the capital and population of Pakistan?"
# )

# # Tool calls handle karo
# if response.tool_calls:
#     for tool_call in response.tool_calls:
#         tool_name = tool_call["name"]
#         tool_args = tool_call["args"]
#         result = tools_dict[tool_name].invoke(tool_args)
#         print(f"Tool: {tool_name}")
#         print(f"Args: {tool_args}")
#         print(f"Result: {result}")
#         print("-" * 30)
# else:
#     print(response.content)


#Ex3

# from langchain_groq import ChatGroq
# from langchain_core.tools import tool
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# @tool
# def calculator(a, b, opr):
#     "this is a calculator"
#     if opr == "/":
#         return a / b
#     elif opr == "-":
#         return a - b
#     elif opr == "*":
#         return a * b
#     elif opr == "+":
#         return a + b
#     else:
#         return "Invalid operator or number"
    
# tools = [calculator]
# tools_dict = {
#     "calculator": calculator
# }

# llm_with_tools = llm.bind_tools(tools)
# response = llm_with_tools.invoke("What is 100 divided by 4?")

# if response.tool_calls:
#     for tool_call in response.tool_calls:
#         tool_name = tool_call["name"]
#         tool_args = tool_call["args"]
#         result = tools_dict[tool_name].invoke(tool_args)
#         print(f"Tools :{tool_name}")
#         print(f"Args : {tool_args}")
#         print(f"Result :{result}")
# else:
#     print(response.content)


#Ex4 


# from langchain_groq import ChatGroq 
# from langchain_core.tools import tool
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# @tool
# def get_weather(city: str) -> str:
#     """Get weather for a city."""
#     weather = {
#         "karachi": "32C Humid ",
#         "lahore": "35C Sunny ",
#         "islamabad": "28C Cloudy "
#     }
#     return weather.get(city.lower(), "City not found")

# @tool
# def get_time(city: str) -> str:
#     """Get current time for a city."""
#     times = {
#         "karachi": "3:00 PM",
#         "lahore": "3:00 PM",
#         "islamabad": "3:00 PM"
#     }
#     return times.get(city.lower(), "City not found")

# @tool
# def get_population(city: str) -> str:
#     """Get population of a city."""
#     population = {
#         "karachi": "16 million",
#         "lahore": "13 million",
#         "islamabad": "1.1 million"
#     }
#     return population.get(city.lower(), "City not found")

# tools = [get_weather, get_time, get_population]
# tools_dict = {
#     "get_weather": get_weather,
#     "get_time": get_time,
#     "get_population": get_population
# }

# llm_with_tools = llm.bind_tools(tools)
# response = llm_with_tools.invoke("Tell me weather, time and population of Karachi")

# if response.tool_calls:
#     for tool_call in response.tool_calls:
#         tool_name = tool_call["name"]
#         tool_args = tool_call["args"]
#         result = tools_dict[tool_name].invoke(tool_args)
#         print(f"Tool:   {tool_name}")
#         print(f"Args:   {tool_args}")
#         print(f"Result: {result}")
#         print("-" * 30)
# else:
#     print(response.content)

