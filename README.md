# instagram-automation
This Python script automates the process of searching for a user's profile and liking the first post by making an authenticated POST request with session management and updated headers/cookies.

## Features

- **Search by Username**: Simulate the process of searching for a user's profile by sending a request to the profile URL.
- **Like the first post**: Simulate the process of liking a user's profile first post.
- **Handles CSRF and Session Tokens**: Updates session cookies and headers dynamically to keep the session alive.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/movassaghi6/instagram-automation.git
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Update `cookies.json` with your Instagram cookies (make sure you're logged in).

## Usage

1. Run the script:

    ```bash
    python .\app\main.py
    ```

The script will load the profile page for the specified username and like the first post.