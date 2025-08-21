import importlib
import os
import re
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

TEST_CASES_DIR = "test_cases"
OUTPUT_DIR = "test_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def current_millis():
    return int(round(time.time() * 1000))

# Load all test case filenames like API_001.py
test_case_files = sorted(
    f for f in os.listdir(TEST_CASES_DIR)
    if re.match(r"API_\d+\.py$", f)
)

# Function to run each test case
def run_test_case(filename):
    module_name = filename[:-3]
    print(f"⏳ Running {module_name}")

    start_time = current_millis()
    logs = []
    status_code = None
    success = False

    try:
        module = importlib.import_module(f"{TEST_CASES_DIR}.{module_name}")
        result_tuple = module.run_test()

        if len(result_tuple) == 3:
            success, log_list, status_code = result_tuple
        else:
            success, log_list = result_tuple
            logs.append({"log": "Warning: Status code not provided", "timestamp": current_millis()})

        logs.extend({"log": log, "timestamp": current_millis()} for log in log_list)

    except Exception as e:
        logs.append({"log": f"Error: {str(e)}", "timestamp": current_millis()})

    result = {
        "testcase_id": module_name,
        "created_at": start_time,
        "success": success,
        "status_code": status_code,
        "logs": logs,
        "completed_at": current_millis()
    }

    result_path = os.path.join(OUTPUT_DIR, f"{module_name}_result.json")
    with open(result_path, "w") as f:
        json.dump(result, f, indent=4)

    print(f"✅ Saved: {result_path}")
    return module_name

# Run tests in parallel batches of 7
batch_size = 7
for i in range(0, len(test_case_files), batch_size):
    batch = test_case_files[i:i+batch_size]
    print(f"\n🚀 Running Batch {i//batch_size + 1} ({len(batch)} tests)")

    with ThreadPoolExecutor(max_workers=batch_size) as executor:
        futures = [executor.submit(run_test_case, filename) for filename in batch]
        for future in as_completed(futures):
            future.result()
