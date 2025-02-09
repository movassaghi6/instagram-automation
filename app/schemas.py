import json
import requests
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from utility import get_csrf_token
import time



# Define Pydantic Data Model for Request Data
class RequestData(BaseModel):
    av: str = "17841461316017780"
    __d: str = "www"
    __user: str = "0"
    __a: str = "1"
    __req: str = "17"
    __hs: str = "20122.HYP:instagram_web_pkg.2.1...1"
    dpr: str = "1"
    __ccg: str = "MODERATE"
    __rev: str = "1019778846"
    __s: str = "ea62h1:rzn4z9:23n1sd"
    __hsi: str = "7467110157858687506"
    __dyn: str = "7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew6ywaq0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9wtUd8-U2zxe2GewGw9a361qw8Xxm16wUwtE1wEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb8jK5V89F8uwm8jxK2K2G0EoKmUhw"
    __csr: str = "gtOgpjMhgz4b5Xn6FZRICx5J8GjGJ7RiZuiGmR8AjmJuEgrhuOriBAqVWBVqKlulqJBx2vqGWGVoB6DAlfAKVoy9BByoPVbCBKaigJ2GDFzpoKKumuEVAAGUtiAhBG7GhngC5HGmbgHxqucJ4yK9QmcxGSJfQdoqypHxO00jXC0ESiu1Ez168wzgR1u9Bwim0ly4X878ggjwdeVo2dwKwjQ3K0aEw6dw7tw6Pw2B4zyE5-8LykE9ax6hS2Sm2efg5G1xCxBeh0aLwv6634CF764gAg1RwNwFzEbgA9AU4W6o4Sq266Flc1Qg47weS3C2f20eE0oQO00mX8G047U0i8w"
    __comet_req:str = '7'
    fb_dtsg:str = 'NAcPJyOgOUfd61pNglvukLPwBhr1rnfJSWEhRELNrkHRUyiYM4-yNvQ:17864863018060157:1738666704'
    jazoest:str = '26445'
    lsd:str = 'eDrY_g4wC0UiJoSzmhqcMi'
    __spin_r:str = '1019814589'
    __spin_b:str = 'trunk'
    __spin_t:str = '1738666752'
    fb_api_caller_class:str = 'RelayModern'
    fb_api_req_friendly_name: Optional[str] = None
    variables: Dict[str, Any] = {}
    server_timestamps:str=  'true'
    doc_id:str = '28149645878012614'


# Define Pydantic Data Model for Headers
class RequestHeader(BaseModel):
    User_Agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
    Accept: str = "*/*"
    Accept_Language: str = "en-US,en;q=0.5"
    Accept_Encoding: str = "gzip, deflate, br, zstd"
    Content_Type: str = "application/x-www-form-urlencoded"
    X_BLOKS_VERSION_ID: str = "8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e"
    X_FB_Friendly_Name: str = ""
    X_FB_LSD: str = ""
    X_CSRFToken: str = Field(default_factory=get_csrf_token)
    X_IG_App_ID: str = "936619743392459"
    X_ASBD_ID: str = "129477"
    Origin: str = "https://www.instagram.com"
    Connection: str = "keep-alive"
    Referer: str = "https://www.instagram.com/abugarcia_fishing/"
    Sec_Fetch_Dest: str = "empty"
    Sec_Fetch_Mode: str = "cors"
    Sec_Fetch_Site: str = "same-origin"
    Upgrade_Insecure_Requests: str = "1"
    Sec_Fetch_User: str = "?1"
    Priority: str = "u=0, i"