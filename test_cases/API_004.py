# TC04_put_brands_list.py
import http.client

def run_test():
    print("Running TC04: PUT /brandsList")
    logs = []
    status_code = None

    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = ''
        headers = {}

        conn.request("PUT", "/api/brandsList", payload, headers)
        res = conn.getresponse()
        data = res.read()

        status_code = res.status
        logs.append(f"Status Code: {status_code}")
        logs.append("Response: {}".format(data.decode("utf-8")[:300]))

        # Accept 200 OK, 400 Bad Request, or 405 Method Not Allowed as expected
        success = status_code in [200, 400, 405]
        return success, logs, status_code

    except Exception as e:
        logs.append(f"Error: {str(e)}")
        return False, logs, status_code
