# TC09_delete_verify_login_invalid_method.py
import http.client
import json

def run_test():
    print("Running TC09: DELETE /verifyLogin (invalid method)")
    logs = []
    status_code = None

    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = ''
        headers = {}

        conn.request("DELETE", "/api/verifyLogin", payload, headers)
        res = conn.getresponse()
        data = res.read()

        status_code = res.status
        decoded_data = data.decode('utf-8')
        logs.append(f"Status Code: {status_code}")
        logs.append(f"Response: {decoded_data[:300]}")

        # Parse JSON response to check logical responseCode
        try:
            response_json = json.loads(decoded_data)
            response_code = response_json.get("responseCode")
            success = response_code in [400, 405]
        except Exception:
            success = False

        return success, logs, status_code
    except Exception as e:
        logs.append(f"Error: {str(e)}")
        return False, logs, status_code
