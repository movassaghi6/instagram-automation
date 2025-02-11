from cookie_manager.cookie_utils import update_and_save_cookies
from utils.utility import extract_all_values_from_html, update_model_fields, extract_first_code_and_pk, access_post_page, like_post
from schema.header import RequestHeader
from schema.data import RequestData
from utils.regex_patterns import header_patterns, data_patterns
import requests
import time


def automation_like_post(username: str):

    # create a session instance
    session = requests.session()


    # for update session with our cookies
    update_and_save_cookies(session)


    # first request for accessing instagram first pages html to update our header and data values
    response = session.get("https://www.instagram.com/")


    # update header values
    extracted_header_values = extract_all_values_from_html(header_patterns, response.text)
    request_header = RequestHeader()
    updated_header =update_model_fields(request_header, extracted_header_values)


    # update data values
    extracted_data_values = extract_all_values_from_html(data_patterns, response.text)
    request_data = RequestData()
    updated_data =update_model_fields(request_data, extracted_data_values)


    # go to profile
    session.get(f"https://www.instagram.com/p/{username}")
    

    # get last post id and media id from graphql
    graphql_response = session.post("https://www.instagram.com/graphql/query", headers= updated_header, data= updated_data)

    first_code, first_pk = extract_first_code_and_pk(graphql_response)


    # open post
    access_post_page(session, headers=updated_header, post_id=first_code)


    # like post
    like_post(session, headers=updated_header, post_media_id=first_pk)


if __name__ == "__main__":
    username = ""
    automation_like_post(username)


