import json
import requests
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
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

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump()

    def update(self, **kwargs) -> 'RequestData':
        updated_data = self.model_copy(update=kwargs)
        return updated_data