# TC12_delete_account.py
import http.client

def run_test():
    print("Running TC12: DELETE /deleteAccount with valid credentials")
    logs = []
    status_code = None
    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = "email=karthik1212%40gmail.com&password=Tester%401234"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        conn.request("DELETE", "/api/deleteAccount", payload, headers)
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
