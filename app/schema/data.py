from pydantic import BaseModel, Field
from typing import Optional
import json
from utils.utility import generate_dynamic_req_key, generate_random_s_key



class RequestData(BaseModel):
    av: str = "17841461316017780"
    d: str = Field("www", alias="__d")
    user: str = Field("0", alias="__user")
    a: str = Field("1", alias="__a")
    req: str = Field(default_factory=generate_dynamic_req_key, alias="__req")
    hs: str = Field("20122.HYP:instagram_web_pkg.2.1...1", alias="__hs")
    dpr: str = "1"
    ccg: str = Field("MODERATE", alias="__ccg")
    rev: str = Field("1019778846", alias="__rev")
    s: str = Field(default_factory=generate_random_s_key, alias="__s")
    hsi: str = Field("7467110157858687506", alias="__hsi")
    dyn: str = Field("7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew6ywaq0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9wtUd8-U2zxe2GewGw9a361qw8Xxm16wUwtE1wEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb8jK5V89F8uwm8jxK2K2G0EoKmUhw", alias="__dyn")
    csr: str = Field("gtOgpjMhgz4b5Xn6FZRICx5J8GjGJ7RiZuiGmR8AjmJuEgrhuOriBAqVWBVqKlulqJBx2vqGWGVoB6DAlfAKVoy9BByoPVbCBKaigJ2GDFzpoKKumuEVAAGUtiAhBG7GhngC5HGmbgHxqucJ4yK9QmcxGSJfQdoqypHxO00jXC0ESiu1Ez168wzgR1u9Bwim0ly4X878ggjwdeVo2dwKwjQ3K0aEw6dw7tw6Pw2B4zyE5-8LykE9ax6hS2Sm2efg5G1xCxBeh0aLwv6634CF764gAg1RwNwFzEbgA9AU4W6o4Sq266Flc1Qg47weS3C2f20eE0oQO00mX8G047U0i8w", alias="__csr")
    comet_req: str = '7'
    fb_dtsg: str = 'NAcPJyOgOUfd61pNglvukLPwBhr1rnfJSWEhRELNrkHRUyiYM4-yNvQ:17864863018060157:1738666704'
    jazoest: str = '26445'
    lsd: str = 'eDrY_g4wC0UiJoSzmhqcMi'
    spin_r: str = Field('1019814589', alias="__spin_r")
    spin_b: str = Field('trunk', alias="__spin_b")
    spin_t: str = Field('1738666752', alias="__spin_t")
    fb_api_caller_class: str = 'RelayModern'
    fb_api_req_friendly_name: Optional[str] = "PolarisProfilePostsQuery"
    variables: str = '{"data":{"count":12,"include_reel_media_seen_timestamp":true,"include_relationship_info":true,"latest_besties_reel_media":true,"latest_reel_media":true},"username":"abugarcia_fishing","__relay_internal__pv__PolarisIsLoggedInrelayprovider":true,"__relay_internal__pv__PolarisShareSheetV3relayprovider":false}'
    server_timestamps: str = 'true'
    doc_id: str = '9066276850131169'
    
    def set_username(self, username: str):
        variables_dict = json.loads(self.variables)
        variables_dict["username"] = username
        self.variables = json.dumps(variables_dict)
    
    class Config:
        populate_by_name = True  # Allows alias names in output

    

