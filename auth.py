import requests

def get_firebase_auth_headers(username: str, password: str) -> dict[str, str]:
    """
    Authenticate a user with Firebase and return the authorization headers required for subsequent API requests.
    
    Parameters:
    ----------
    username: str
        The email address of the user.
    password: str
        The password of the user.
    """ 
    firebase_key = "AIzaSyCECGQmWsGaZ3x7n_uGiq3kt-lyo-IYPvI"
    firebase_url = "https://identitytoolkit.googleapis.com/v1"
    firebase_endpoint = f"{firebase_url}/accounts:signInWithPassword?key={firebase_key}"
    data_dict = {'email': username, 'password': password, 'returnSecureToken': 'true'}
    response_post_token = requests.post(firebase_endpoint, data=data_dict)
    if response_post_token.status_code == 200:
        id_token = response_post_token.json()['idToken']
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {id_token}"}   
    else:
        print(f"Failed to authenticate user with Firebase. {response_post_token.text}")
        headers = {"Content-Type": "application/json", "Authorization" : ""} 
    return headers