#! python

import json

from api_request import ApiRequest
from vancouver_reference import VancouverReference

def get_json_data(url=None):
    
    # url location of book data
    test_url = 'http://xisbn.worldcat.org/webservices/xid/isbn/0596002815?method=getMetadata&format=json&fl=*'
    test_filename = 'isbn.example.json'    
    
    if url:
        # api call to obtain book data
        dataRequest = ApiRequest(test_url)
        json_data = dataRequest.get_resource()
    else:
        with open(test_filename) as f:
            json_data = json.load(f)
    
    return json_data

reference_data = VancouverReference(get_json_data())

print(reference_data.get_reference_data())
