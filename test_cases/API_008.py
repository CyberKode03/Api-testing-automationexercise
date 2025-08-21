# TC08_post_verify_login_empty.py
import http.client

def run_test():
    print("Running TC08: POST /verifyLogin with empty body")
    logs = []
    status_code = None

    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = ''
        headers = {}

        conn.request("POST", "/api/verifyLogin", payload, headers)
        res = conn.getresponse()
        data = res.read()

        status_code = res.status
        logs.append(f"Status Code: {status_code}")
        logs.append(f"Response: {data.decode('utf-8')[:300]}")

        success = status_code == 400 or status_code == 200
        return success, logs, status_code
    except Exception as e:
        logs.append(f"Error: {str(e)}")
        return False, logs, status_code
