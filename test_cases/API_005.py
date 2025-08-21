# TC05_post_search_product.py
import http.client
import urllib.parse

def run_test():
    print("Running TC05: POST /searchProduct (valid payload)")
    logs = []
    status_code = None

    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = urllib.parse.urlencode({
            "search_product": "jeans"
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        conn.request("POST", "/api/searchProduct", payload, headers)
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
