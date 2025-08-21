# TC10_post_verify_login_missing_content_type.py

import http.client

def run_test():
    print("Running TC15: POST /verifyLogin with custom email and password")
    logs = []
    status_code = None
    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = 'email=karthik%40gmail.com&password=Tester%401234'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        conn.request("POST", "/api/verifyLogin", payload, headers)
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
