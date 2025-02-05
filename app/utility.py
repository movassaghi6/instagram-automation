from typing import Dict
from schemas import RequestData

def to_dict(request_data: RequestData) -> Dict:
    return request_data.dict()

