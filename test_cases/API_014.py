# TC14_get_user_by_email.py
import http.client
import urllib.parse

def run_test():
    print("Running TC14: GET /getUserDetailByEmail with valid email")
    logs = []
    status_code = None
    try:
        email = "johndoe16@example.com"
        encoded_email = urllib.parse.quote(email)

        conn = http.client.HTTPSConnection("automationexercise.com")
        endpoint = f"/api/getUserDetailByEmail?email={encoded_email}"
        payload = ''
        headers = {}

        conn.request("GET", endpoint, payload, headers)
        res = conn.getresponse()
        data = res.read()

        status_code = res.status
        logs.append(f"Status Code: {status_code}")
        logs.append(f"Response: {data.decode('utf-8')[:300]}")

        success = status_code == 200
        return success, logs, status_code
    except Exception as e:
        logs.append(f"Error: {str(e)}")
        return False, logs, status_code
