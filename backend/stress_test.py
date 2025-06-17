import requests

def simulate_traffic():
    for i in range(500):  # Simulate 500 concurrent requests
        response = requests.post("http://127.0.0.1:8000/athlete_comparison/compare_athlete", json={"data": [[1,2,3], [4,5,6]], "labels": ["label1", "label2"]})
        print(response.json())

simulate_traffic()
