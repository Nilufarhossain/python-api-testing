# 🐍 Python API Test Automation

A REST API automation project using **Python, pytest, and Requests** to demonstrate functional testing, CRUD operations, and API response validation.

### 🛠️ Technologies
`Python` • `pytest` • `Requests` • `JSON` • `pytest-html`

### 🧪 Test Coverage
- GET, POST, PUT, DELETE requests
- Positive and negative testing
- HTTP status code and JSON validation
- Parameterized testing
- Reusable API helper functions
- HTML test reports

### 📊 Test Results

✅ **13 Passed | 0 Failed | 0 Skipped**

### ▶️ Run Tests

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

### 📈 Generate HTML Report

```bash
python -m pytest --html=report.html --self-contained-html
```

**API Used:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a public practice API with simulated write operations.
