import requests
import json


# Initialize a session to persist certain parameters across requests (e.g., cookies, headers)
session = requests.Session()


# load cookies from json
with open('cookies.json', 'r') as file:
    cookies = json.load(file)


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


# Data dictionary to include POST request parameters and Instagram-specific data
data = {
    "av": "17841461002400656",
    "__d": "www",
    "__user": "0",
    "__a": "1",
    "__req": "16",
    "__hs": "20121.HYP:instagram_web_pkg.2.1...1",
    "dpr": "1",
    "__ccg": "MODERATE",
    "__rev": "1019771082",
    "__s": "dswjdn:rzn4z9:ahi64c",
    "__hsi": "7466716840802685629",
    "__dyn": "7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8aUco2qwJyEiw9-1DwUx60p-0LVE4W0qa321Rw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2iyo7u3ifK0zEkxe2GewGw9a3614xm0zK5o4q3y261kx-0ma2-azqwt8d-2u2J08O321LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubK5V89FbxG1oxe6UaUaE2xyVrx6",
    "__csr": "jMdJgkjnbbk8OkJlid4HsgSZeJZlAnX_GQDajiUxCnFbq_KOGiLHGQAAihBqAFV5hdk-mbGF9AyJemV4XHlbGh2XHhlgVtAzFcx7CBGVU-8LyUx2cCmqRxbACFBmiHgCqi4sBpbAyFkiVHGqmuaAzEhAzECQdGnyUAxdbBV4m4UGaFUlGiaBw04Sr80OUc41zwjolU4C0KX82CEa46qyojC5AgWqahl42Q2WS1Gw9u1mxOqt2EChwIwou2pdXolwik3zB50Xxa2qhPCgO093waa2O1YgdE6-5o0wa0nG0b3BIUC1mxmmRxqfxaH9hU-6Q7rzU5S1xByU-Vk0H42gU55xwwPQoml2187m362CewJ2gCjwjEmwk9EtxXdho790gu0X8eo8Y80Ww1zoE9o0Eqq4QfBG1lhojxp0Bg04RKE4K0w2auaw3bo1IUK09BQGxy2S045E0-pw",
    "__comet_req": "7",
    "fb_dtsg": "NAcMbE-9Uwk-r7aJpJ6zdu2mJaCGnzue7rX0xObtX2EN_vU4KShlUiQ:17858449030071790:1738410193",
    "jazoest": "26297",
    "lsd": "BLoqaXOI_Q7IhuTVLrwftw",
    "__spin_r": "1019771082",
    "__spin_b": "trunk",
    "__spin_t": "1738480488",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "PolarisSearchNullStateQuery",
    "variables": "{}",
    "server_timestamps": "true",
    "doc_id": "8568350183286091"
}



# function to find and access a user profile by its username
def load_profile_page(username, cookies, headers, data):
    # Create a session instance
    session = requests.Session()

    # Define the URL for the user's profile
    profile_url = f"https://www.instagram.com/{username}/"

    # Add cookies to session
    session.cookies.update(cookies)

    # Send the POST request
    response = session.post(profile_url, headers=headers, data=data)

    # Check the response status
    if response.status_code == 200:
        print(f"Successfully loaded profile page for {username}")
        # You can now parse the HTML, interact with it, or scrape data
    else:
        print(f"Failed to load profile page for {username}. Status code: {response.status_code}")

    # Get new cookies
    updated_cookies = session.cookies.get_dict()

    # Merge old and new cookies (update only changed fields)
    cookies.update(updated_cookies)

    # Save updated cookies back to file
    with open("cookies.json", "w") as f:
        json.dump(cookies, f, indent=4)

# Example usage
username = "abugarcia_fishing"  # Replace with the actual username you want to search

# Call the function
load_profile_page(username, cookies, headers, data)


# function for accessing id of the latest post in a users profile
def get_post_id(cookies, headers, data):
    # Define the URL
    profile_url = "https://www.instagram.com/graphql/query"
    
    # Create a session and add cookies
    session = requests.Session()
    session.cookies.update(cookies)
    
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
last_post_id = get_post_id(cookies, headers, data)