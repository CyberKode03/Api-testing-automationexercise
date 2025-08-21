# TC02_post_products.py
import http.client

def run_test():
    print("Running TC02: POST /productsList")
    logs = []
    status_code = None

    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = ''
        headers = {}

        conn.request("POST", "/api/productsList", payload, headers)
        res = conn.getresponse()
        data = res.read()

        status_code = res.status
        logs.append(f"Status Code: {status_code}")
        logs.append("Response: {}".format(data.decode("utf-8")[:300]))

        success = (status_code == 200)
        return success, logs, status_code

    except Exception as e:
        logs.append(f"Error: {str(e)}")
        return False, logs, status_code
