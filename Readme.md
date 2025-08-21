# 🚀 API Testing Project - AutomationExercise

This repository contains **API test cases** for the [AutomationExercise API](https://automationexercise.com/api_list).  
It includes **individual test scripts** for each API as well as a **master runner** that executes all tests in parallel and stores results in JSON format.

---

## 📌 Project Overview
- Covered **14 API endpoints** with positive and negative scenarios.
- Verified **status codes, response payloads, and error handling**.
- Designed a **master runner** to automatically execute all test cases in batches and log results.
- Results saved in `test_results/` folder as JSON reports.

---

## 📂 Project Structure

---

## ⚙️ Master Runner (Parallel Execution)

The file **`run_all_tests.py`**:
- Dynamically discovers test case files (`API_001.py`, `API_002.py`, etc.).
- Runs them in **parallel batches of 7** using `ThreadPoolExecutor`.
- Captures:
  - ✅ Testcase ID  
  - ✅ Start & End timestamps  
  - ✅ Success/Failure status  
  - ✅ HTTP status codes  
  - ✅ Execution logs  
- Saves results in `test_results/` as structured JSON files.  

### Example Run:
```bash
python run_all_tests.py
