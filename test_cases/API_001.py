# TC01_get_products.py

# TC_001.py
import http.client

def run_test():
    print("Running TC01: GET /productsList")
    logs = []
    status_code = None

    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = ''
        headers = {}

        conn.request("GET", "/api/productsList", payload, headers)
        res = conn.getresponse()
        data = res.read()

        status_code = res.status
        logs.append("Status Code: {}".format(res.status))
        logs.append("Response: {}".format(data.decode("utf-8")[:300]))  # Partial preview

        return True, logs, status_code

    except Exception as e:
        logs.append("Error: {}".format(str(e)))
        return False, logs, status_code
