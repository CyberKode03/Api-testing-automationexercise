# TC11_post_create_account.py
import http.client

def run_test():
    print("Running TC11: POST /createAccount with valid details")
    logs = []
    status_code = None
    try:
        conn = http.client.HTTPSConnection("automationexercise.com")
        payload = (
            "name=karthik1212&email=devadigakarthik%40gmail.com&password=Tester%401234"
            "&title=Mr&birth_date=15&birth_month=10&birth_year=1995"
            "&firstname=karthik&lastname=devadiga&company=OpenAI"
            "&address1=123%20Main%20Street&address2=Apt%20101"
            "&country=United%20States&zipcode=12345"
            "&state=California&city=Los%20Angeles&mobile_number=1234567890"
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        conn.request("POST", "/api/createAccount", payload, headers)
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
