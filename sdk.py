"""
sdk.py

MotionOS Python SDK stub. External devs can import formforge_avatar_feed()
to pull live avatar state without worrying about the HTTP details.
"""

import requests
from typing import Dict, Any

__all__ = ["formforge_avatar_feed"]

def formforge_avatar_feed(base_url: str = "http://localhost:8001") -> Dict[str, Any]:
    """
    Fetch the current avatar state from the MotionOS Avatar API.

    Args:
        base_url (str): The root URL for the Avatar API (default: 'http://localhost:8001').

    Returns:
        dict: Parsed JSON of the form:
            {
              "timestamp": <number>,
              "joints": [
                 {
                   "name": <string>,
                   "x": <number>,
                   "y": <number>,
                   "z": <number>,
                   "strain": <number>,
                   "fatigue": <number>
                 },
                 ...
              ]
            }
    Raises:
        requests.HTTPError: if the GET request fails.
    """
    endpoint = f"{base_url}/api/avatar-state"
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()

# Example usage:
# if __name__ == "__main__":
#     data = formforge_avatar_feed()
#     print("Live avatar state:", data)
