import json


# Load Cookies
with open("cookies.json", "r") as f:
     cookies =json.load(f)


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