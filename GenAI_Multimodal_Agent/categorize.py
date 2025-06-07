from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from dotenv import load_dotenv
from pathlib import Path
import os
import json

load_dotenv()

def get_item_code(item_name):
    """
    Returns the item code corresponding to the provided item name. If the item
    name does not match any predefined items, a default code is returned.

    :param item_name: The name of the item to retrieve the code for. Expected
                      values are "sari", "t-shirt", "jeans", "jacket".
    :type item_name: str
    :return: The code corresponding to the given item name. Returns "ITM001"
             for "sari", "ITM002" for "t-shirt", "ITM003" for "jeans",
             "ITM004" for "jacket", and "ITM999" for any other input.
    :rtype: str
    """
    if item_name == "sari":
        return "ITM001"

    if item_name == "t-shirt":
        return "ITM002"

    if item_name == "jeans":
        return "ITM003"

    if item_name == "jacket":
        return "ITM004"

    return "ITM999"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[get_item_code]
)

response = agent.run(
    message='''For each image, generate a JSON record that looks like this:
    {
        "item_name": "sari",
        "item_code": "ITM001",
        "color": "red",
        "gender": "female",
        "age_category": "adult" 
    }
    Output must be a JSON string that Python can parse it directly.
    Do not put any pre-amble instructions or event 'json' in front of the response string.
    item_name should be one of the following: sari, t-shirt, jeans, jacket
    age_category should be one of the following: adult, child 
    ''',
    images=[
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image1.jpg")),
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image2.jpg")),
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image3.jpg"))
    ]
)

response_json = json.loads(response.content)
print(response_json)
