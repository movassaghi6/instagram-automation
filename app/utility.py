from typing import Tuple, Optional, Dict, Union
from schemas import RequestData
from cookie_manager.cookie_utils import cookies
import requests
import re



def to_dict(request_data: RequestData) -> Dict:
    return request_data.dict()

def get_csrf_token() -> str:
    return cookies.get("csrftoken", "")


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



def update_model_fields(model, extracted_values: Dict[str, str]):
    """
    Updates the fields of a Pydantic model with the extracted values if they differ.

    Args:
        model (T): The original Pydantic model instance.
        extracted_values (Dict[str, str]): The extracted values to update the model with.

    Returns:
        T: A new instance of the model with updated values.
    """
    return model.model_copy(update=extracted_values)  



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