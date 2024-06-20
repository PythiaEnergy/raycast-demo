import requests
from datetime import datetime
import json

def raycast_data_by_query(
    token: str,
    ref_datetime: datetime
):
    file_name = f"irradiance_{ref_datetime.strftime('%Y%m%dT%H%M%S')}.nc"
    resp = requests.get(
        url=f"https://api.ubiops.com/v2.1/projects/raycast-development/buckets/predictions/files/{file_name}/download", 
        headers={'Authorization': f'{token}'}
    )

    data = json.loads(resp.content)

    receive_file = requests.get(url=data["url"], stream=True)
    data = receive_file.raw.read(decode_content=True)
    
    if resp.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(data)
    else: 
        print(resp.status_code)
    return 