# TC13_update_account.py
import http.client

def run_test():
    print("Running TC13: PUT /updateAccount with valid data")
    logs = []
    status_code = None
    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = ('name=%20testere&email=karthik1212%40gmail.com&password=Tester%401234&title=%20Mr'
                   '&birth_date=%2015&birth_month=%2010&birth_year=%201995&firstname=%20John&lastname=%20Doe'
                   '&company=%20OpenAI&address1=%20123%20Main%20Street&address2=%20Apt%20101&country=%20United%20States'
                   '&zipcode=%2012345&state=%20California&city=%20Los%20Angeles&mobile_number=%201234567890')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        conn.request("PUT", "/api/updateAccount", payload, headers)
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
