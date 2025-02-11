from pydantic import BaseModel, Field
from utils.utility import get_csrf_token



# Define Pydantic Data Model for Headers
class RequestHeader(BaseModel):
    User_Agent: str = Field("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0", alias="User-Agent")
    Accept: str = "*/*"
    Accept_Language: str = Field("en-US,en;q=0.5", alias="Accept-Language")
    Content_Type: str = Field("application/x-www-form-urlencoded", alias="Content-Type")
    X_BLOKS_VERSION_ID: str = Field("8cfdad7160042d1ecf8a994bb406cbfffb9a769a304d39560d6486a34ea8a53e", alias="X-BLOKS-VERSION-ID")
    X_FB_Friendly_Name: str = Field("PolarisProfilePostsQuery", alias="X-FB-Friendly-Name")
    X_FB_LSD: str = Field("", alias="X-FB-LSD")
    X_CSRFToken: str = Field(default_factory=get_csrf_token, alias="X-CSRFToken")
    X_IG_App_ID: str = Field("936619743392459", alias="X-IG-App-ID")
    X_ASBD_ID: str = Field("129477", alias="X-ASBD-ID")
    Origin: str = "https://www.instagram.com"
    Connection: str = "keep-alive"
    Referer: str = "https://www.instagram.com/abugarcia_fishing/"
    Sec_Fetch_Dest: str = Field("empty", alias="Sec-Fetch-Dest")
    Sec_Fetch_Mode: str = Field("cors", alias="Sec-Fetch-Mode")
    Sec_Fetch_Site: str = Field("same-origin", alias="Sec-Fetch-Site")
    Upgrade_Insecure_Requests: str = Field("1", alias="Upgrade-Insecure-Requests")
    Sec_Fetch_User: str = Field("?1", alias="Sec-Fetch-User")
    Priority: str = "u=0, i"
    
    class Config:
        populate_by_name = True  # Allows alias names in output