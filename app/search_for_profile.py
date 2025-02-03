import requests
import json


# Initialize a session to persist certain parameters across requests (e.g., cookies, headers)
session = requests.Session()


# load cookies from json
with open('cookies.json', 'r') as file:
    cookies = json.load(file)


def update_and_save_cookies(session, updated_cookies=None, file_path="cookies.json"):
    """
    Updates the session with new cookies, merges them with existing cookies,
    and saves them to a JSON file.

    :param session: The requests session to update.
    :param updated_cookies: Dictionary of new cookies to merge.
    :param file_path: Path to the JSON file where cookies are stored.
    """
    try:
        # Load existing cookies from file
        with open(file_path, 'r') as file:
            cookies = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        cookies = {}  # Start fresh if file doesn't exist or is corrupted

    # Merge new cookies if provided
    if updated_cookies:
        cookies.update(updated_cookies)

    # Update session with merged cookies
    session.cookies.update(cookies)

    # Save updated cookies back to file
    with open(file_path, 'w') as file:
        json.dump(cookies, file, indent=4)


# function for updating or adding extra fields to data
def update_data(base_data, **kwargs):
    """
    Updates the base data dictionary dynamically with new key-value pairs.
    
    Args:
        base_data (dict): The initial data dictionary.
        **kwargs: Additional fields to update or add dynamically.

    Returns:
        dict: The updated data dictionary.
    """
    updated_data = base_data.copy()  # Avoid modifying the original dictionary
    updated_data.update(kwargs)
    return updated_data


# default headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-FB-Friendly-Name": "PolarisSearchNullStateQuery",
    "X-BLOKS-VERSION-ID": "8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e",
    "X-CSRFToken": cookies["csrftoken"],
    "X-IG-App-ID": "936619743392459",
    "X-FB-LSD": "BLoqaXOI_Q7IhuTVLrwftw",
    "X-ASBD-ID": "129477",
    "Origin": "https://www.instagram.com",
    "Referer": "https://www.instagram.com/"
}


data = 'route_urls^[0^]=^%^2Fstories^%^2Fhighlights^%^2F17869897943334651^%^2F^%^3Fr^%^3D1&route_urls^[1^]=^%^2Fstories^%^2Fhighlights^%^2F17981893000342210^%^2F^%^3Fr^%^3D1&route_urls^[2^]=^%^2Fstories^%^2Fhighlights^%^2F17916299836591418^%^2F^%^3Fr^%^3D1&route_urls^[3^]=^%^2Fabugarcia_fishing^%^2Ffollowers^%^2F&route_urls^[4^]=^%^2Fabugarcia_fishing^%^2Ffollowing^%^2F&routing_namespace=igx_www&__d=www&__user=0&__a=1&__req=1w&__hs=20122.HYP^%^3Ainstagram_web_pkg.2.1...1&dpr=1&__ccg=MODERATE&__rev=1019780606&__s=l0qn91^%^3Aaja29j^%^3A6yq7te&__hsi=7467200991684461158&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew6ywaq0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9wtUd8-U2zxe2GewGw9a361qw8Xxm16wUwtE1wEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb8jK5V89F8uwm8jxK2K2G0EoKmUhw&__csr=gTf0IsQahsn96l8YG4nvbsTi9h9ep4WnvhkAH_qFpqFvBBCWtejQBHVqSXBXKtzpkXaJp9VH-8AAhVKdg-49HGA9XZ2qHh-9haGWVuVUKqh7LzVLK4p8KmpaELVojgDuq8UJ2aXyQUly998G9DyFFpJ6K9DDzpozt6giGfCBy9omw04-ZwadADwq8Mhy88Qdgnypo4Bw5oxeO1O444U3jKm0zobE4Z0Xw2G81zo1To1IU0Fh8UG1vybUBa2iEhAtwJBwzzQ1qwopEpjAg2HU7NxwN9GhNx4940tocoaoW2Q92pe1exC1dCwxxGlj0t411U3JwVwzMw3G06dcw05KOaw11-04y8&__comet_req=7&fb_dtsg=NAcNqgl6_zEKWJfzHXnws7p0Vlg3OiqczVz33l_OcfSnTw1jLF7KUvQ^%^3A17865145036029998^%^3A1738574805&jazoest=26476&lsd=SdlcfsbF31F8J2dnwImpC0&__spin_r=1019780606&__spin_b=trunk&__spin_t=1738593213'

# function to find and access a user profile by its username
def load_profile_page(username, headers, data):

    # Define the URL for the user's profile
    profile_url = f"https://www.instagram.com/{username}/"

    # Update cookies in session   
    update_and_save_cookies(session)

    # Send the POST request
    response = session.post(profile_url, headers=headers, data=data)

    # Check the response status
    if response.status_code == 200:
        print(f"Successfully loaded profile page for {username}")
        # You can now parse the HTML, interact with it, or scrape data
    else:
        print(f"Failed to load profile page for {username}. Status code: {response.status_code}")


# Example usage
username = "abugarcia_fishing"  # Replace with the actual username you want to search

# Call the function
load_profile_page(username, headers, data)

data = 'av=17841460777147385&__d=www&__user=0&__a=1&__req=1q&__hs=20122.HYP^%^3Ainstagram_web_pkg.2.1...1&dpr=1&__ccg=MODERATE&__rev=1019780606&__s=l0qn91^%^3Aaja29j^%^3A6yq7te&__hsi=7467200991684461158&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew6ywaq0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9wtUd8-U2zxe2GewGw9a361qw8Xxm16wUwtE1wEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb8jK5V89F8uwm8jxK2K2G0EoKmUhw&__csr=gTf0IsQahsn96l8YG4nvbsTi9h9ep4WnvhkAH_qFpqFvBBCWtejQBHVqSXBXKtzpkXaJp9VH-8AAhVKdg-49HGA9XZ2qHh-9haGWVuVUKqh7LzVLK4p8KmpaELVojgDuq8UJ2aXyQUly998G9DyFFpJ6K9DDzpozt6giGfCBy9omw04-ZwadADwq8Mhy88Qdgnypo4Bw5oxeO1O444U3jKm0zobE4Z0Xw2G81zo1To1IU0Fh8UG1vybUBa2iEhAtwJBwzzQ1qwopEpjAg2HU7NxwN9GhNx4940tocoaoW2Q92pe1exC1dCwxxGlj0t411U3JwVwzMw3G06dcw05KOaw11-04y8&__comet_req=7&fb_dtsg=NAcNqgl6_zEKWJfzHXnws7p0Vlg3OiqczVz33l_OcfSnTw1jLF7KUvQ^%^3A17865145036029998^%^3A1738574805&jazoest=26476&lsd=SdlcfsbF31F8J2dnwImpC0&__spin_r=1019780606&__spin_b=trunk&__spin_t=1738593213&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisProfilePostsQuery&variables=^%^7B^%^22data^%^22^%^3A^%^7B^%^22count^%^22^%^3A12^%^2C^%^22include_reel_media_seen_timestamp^%^22^%^3Atrue^%^2C^%^22include_relationship_info^%^22^%^3Atrue^%^2C^%^22latest_besties_reel_media^%^22^%^3Atrue^%^2C^%^22latest_reel_media^%^22^%^3Atrue^%^7D^%^2C^%^22username^%^22^%^3A^%^22abugarcia_fishing^%^22^%^2C^%^22__relay_internal__pv__PolarisIsLoggedInrelayprovider^%^22^%^3Atrue^%^7D&server_timestamps=true&doc_id=8934560356598281'

# function for accessing id of the latest post in a users profile
def get_post_id(headers, data):
    # Define the URL
    profile_url = "https://www.instagram.com/graphql/query"

    # Update cookies in session   
    update_and_save_cookies(session)
    
    # Send the POST request
    response = session.post(profile_url, headers=headers, data=data)
    
    # Check for successful response
    if response.status_code == 200:
        # Parse JSON response
        json_data = response.json()
        
        # Accessing the value
        code = json_data.get('data', {}).get('xdt_api__v1__feed__user_timeline_graphql_connection', {}).get('edges', [])
        if code:
            code_value = code[0].get('node', {}).get('code')
            return code_value
        else:
            return "Key not found!"
    else:
        return f"Error: {response.status_code}"

# data provided from cURL of the request
data = """av=17841461002400656&__d=www&__user=0&__a=1&__req=7&__hs=20121.HYP%3Ainstagram_web_pkg.2.1...1&dpr=1&__ccg=MODERATE&__rev=1019772043&__s=4rquec%3Arzn4z9%3Ahvqkfh&__hsi=7466797561635021871&__dyn=7xe5WwlEnwn8K2Wmm1twpUnwgU7S6EeUaUco38w5ux609vCwjE1EE2Cw8G11w6zx62G3i1ywOwa90Fw4Hw9O0M82zxe2GewGw9a361qw8W5U4q09yyES1Twoob82ZwrUdUbGw4mwr86C1mwrd6goK10xKi2K7E5y4UrwHwcObBxm&__csr=&__comet_req=7&fb_dtsg=NAcMX8y-70vfn9Y2yeZt27RlxoaAzjQ4tzgiZuh_HaMSEPGNcYwOrjw%3A17858449030071790%3A1738410193&jazoest=26461&lsd=ThneM-hsSbTaKh7Ina08NP&__spin_r=1019772043&__spin_b=trunk&__spin_t=1738499282&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisProfilePostsQuery&variables=%7B%22data%22%3A%7B%22count%22%3A12%2C%22include_reel_media_seen_timestamp%22%3Atrue%2C%22include_relationship_info%22%3Atrue%2C%22latest_besties_reel_media%22%3Atrue%2C%22latest_reel_media%22%3Atrue%7D%2C%22username%22%3A%22abugarcia_fishing%22%2C%22__relay_internal__pv__PolarisIsLoggedInrelayprovider%22%3Atrue%7D&server_timestamps=true&doc_id=8934560356598281"""

# Call the function
last_post_id = get_post_id(headers, data)


#function for opening
def open_last_post(last_post_id, headers, data):
    # Define the URL for the last post
    url = f"https://www.instagram.com/p/{last_post_id}"

    # Update cookies in session   
    update_and_save_cookies(session)
    
    # Send the POST request
    response = session.post(url, headers=headers, data=data)
    
    return response

# Call the function
response = open_last_post(last_post_id, headers, data)


# function for liking latest post
def like_post(url, headers):

    # Define the new referer URL
    new_referer = f'https://www.instagram.com/p/f{last_post_id}/'

    # Check if 'Referer' is in the headers and update it, otherwise add it
    if 'Referer' in headers:
        headers['Referer'] = new_referer  # Update the existing Referer value
    else:
        headers['Referer'] = new_referer  # Add the Referer if not present

    # Update cookies in session   
    update_and_save_cookies(session)

    # Send the POST request
    response = session.post(url, headers=headers)

    # Check if the status code is 200
    if response.status_code == 200:
        print("Like completed successfully!")
    else:
        # Handle different error scenarios
        print(f"Error: {response.status_code}")
        try:
            # Try to parse the response as JSON to get more error details
            error_details = response.json()
            print("Error details:", error_details)
        except ValueError:
            # If the response is not JSON, just print the text content
            print("Response content:", response.text)

# Example usage
url = "https://www.instagram.com//api/v1/web/likes/3559410931047449099/like/"

like_post(url, headers)
    