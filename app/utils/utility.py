from typing import Tuple, Optional, Dict, Union
from cookie_manager.cookie_utils import cookies
import requests
import random
import string
import re



# Header: for csrf_token value which can be found in cookies
def get_csrf_token() -> str:
    return cookies.get("csrftoken", "")


# Data:  for random value of __s
def generate_random_s_key() -> str:
    """
    Generates a random '__s' key in the format 'xxxxxx:xxxxxx:xxxxxx' 
    where each segment is a mix of letters and digits.

    Returns:
        str: Randomly generated '__s' value.
    """
    def random_segment(length=6):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    return f"{random_segment()}:{random_segment()}:{random_segment()}"


# Data: for random value of __req
def generate_random_req_key() -> str:
    """
    Generates a dynamic '__req' key.

    Returns:
        str: The generated '__req' value.
    """
    # Randomly decide if the value should be a number or a number followed by a letter
    if random.choice([True, False]):
        # Generate a number between 1 and 20
        return str(random.randint(1, 20))
    else:
        # Generate a number between 1 and 9 followed by a random lowercase letter
        return f"{random.randint(1, 9)}{random.choice(string.ascii_lowercase)}"


# Utility function to extract the first match of a regex pattern from a given text
def extract_value(pattern: str, text: str) -> str:
    """
    Extracts the first match of the given regex pattern from the provided text.

    Args:
        pattern (str): The regex pattern to search for.
        text (str): The text from which the value should be extracted.

    Returns:
        str: The extracted value if a match is found, otherwise None.
    """
    match = re.search(pattern, text)
    return match.group(1) if match else None


def extract_all_values_from_html(patterns: dict, response_text:Union[dict, str]) -> Dict[str, str]:
    """
    Extracts multiple predefined values from the given response text using predefined regex patterns.

    Args:
        response_text (str): The text from which values will be extracted.

    Returns:
        Dict[str, str]: A dictionary containing extracted values with corresponding labels.
    """
    extracted_values = {}
    # Loop through each pattern and extract corresponding value from the response text
    for label, pattern in patterns.items():
        value = extract_value(pattern, response_text)
        if value is not None:
            extracted_values[label] = str(value)

    return extracted_values


def update_model_fields(model, extracted_values: Dict[str, str]) :
    """
    Updates the fields of a Pydantic model with the extracted values if they differ
    and returns a dictionary.

    Args:
        model: The original Pydantic model instance.
        extracted_values (Dict[str, str]): The extracted values to update the model with.

    Returns:
        Dict[str, str]: A dictionary with alias names representation of the updated model.
    """
    updated_model = model.model_copy(update=extracted_values)
    return updated_model.model_dump(by_alias=True)  # Convert to dictionary with alias names


# Find the latest post id and its media's id
def extract_first_code_and_pk(response: requests.Response) -> Tuple[Optional[str], Optional[str]]:
    """
    Extracts the first post code and pk from the response JSON.

    Args:
        response (requests.Response): The response object containing the JSON data.

    Returns:
        Tuple[Optional[str], Optional[str]]: A tuple containing the first post code and pk, or None if not found.
    """
    # Extract the list of edges from the response JSON
    edges = response.json().get('data', {}).get('xdt_api__v1__feed__user_timeline_graphql_connection', {}).get('edges', [])
    
    # Use a generator expression to find the first code and pk
    first_code = next((edge.get('node', {}).get('code') for edge in edges if edge.get('node', {}).get('code')), None)
    first_pk = next((str(edge.get('node', {}).get('pk')) for edge in edges if edge.get('node', {}).get('pk')), None)
    
    return first_code, first_pk


# Access the last post's page
def access_post_page(session: requests.Session, headers: Dict[str, str], post_id: str) -> requests.Response:
    """
    Accesses the URL of the last post.

    Args:
        session (requests.Session): The session object to make the request.
        headers (Dict[str, str]): The headers to include in the request.
        post_id (str): The ID of the post to access.

    Returns:
        requests.Response: The response object from the GET request.
    """
    response = session.get(f'https://www.instagram.com/p/{post_id}', headers=headers)
    print("Accessing last post:", response.status_code)
    return response


# Like the post
def like_post(session: requests.Session, headers: Dict[str, str], post_media_id: str) -> requests.Response:
    """
    Likes the post with the given media ID.

    Args:
        session (requests.Session): The session object to make the request.
        headers (Dict[str, str]): The headers to include in the request.
        post_media_id (str): The media ID of the post to like.

    Returns:
        requests.Response: The response object from the POST request.
    """
    response = session.post(f'https://www.instagram.com/api/v1/web/likes/{post_media_id}/like/', headers=headers)
    print("Liking last post:", response.status_code)
    return response


# find doc_id based on fb_friendly_name
def extract_doc_id(session, url, fb_friendly_name, extract_func):
    """
    Fetches a webpage, identifies JavaScript resource links, and extracts values 
    associated with a specified key in the scripts.

    Args:
        session (requests.Session): The active HTTP session.
        url (str): The URL of the page to fetch.
        fb_friendly_name (str): The key to search for in the JavaScript files.
        extract_func (callable): A function that extracts key-value pairs from script content.

    Returns:
        dict: A dictionary containing extracted values where the key is fb_friendly_name 
              and the value is the corresponding extracted data. Returns an empty dict if nothing is found.
    """
    try:
        response = session.get(url, timeout=5)
        if response.status_code != 200:
            return {}

        # Extract JavaScript resource links
        script_links = re.findall(r'https://static\.cdninstagram\.com/rsrc\.php/[^\s"]+', response.text)
        extracted_data = {}

        # Compile a regex pattern for the target key
        pattern = {fb_friendly_name: rf'__d\("{re.escape(fb_friendly_name)}[^"]*",\[\],\(function\(.*?\)\{{e\.exports="([^"]+)"\}}\),null\);'}

        # Iterate through script links and extract relevant data
        for link in script_links:
            try:
                js_response = session.get(link, timeout=5)
                if js_response.status_code == 200:
                    extracted_data.update(extract_func(pattern, js_response.text))  # Extract values using provided function
            except requests.RequestException:
                continue  # Skip script links that fail to load

        return extracted_data.get(fb_friendly_name)


    except requests.RequestException:
        return {}  # Return empty dictionary if the main request fails
    
