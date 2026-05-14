# hard/200-c-football-championship

**Status:** FAIL

sandbox error (status=Failed)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp66dr0aiw
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmprpqzk5a5.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
AERLAND DERLAND 2:1
DERLAND CERLAND 0:3
CERLAND AERLAND 0:1
AERLAND BERLAND 2:0
DERLAND BERLAND 4:0


Expected Output:
6:0

Actual Output from /app/solution.py:
6:0

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
AERLAND DERLAND 2:2
DERLAND CERLAND 2:3
CERLAND AERLAND 1:3
AERLAND BERLAND 2:1
DERLAND BERLAND 4:1


Expected Output:
IMPOSSIBLE

Actual Output from /app/solution.py:
IMPOSSIBLE

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
CRWEYDMET BERLAND 6:2
J CRWEYDMET 5:4
LYUTZZCGW BERLAND 8:4
LYUTZZCGW CRWEYDMET 3:4
LYUTZZCGW J 2:2


Expected Output:
IMPOSSIBLE

Actual Output from /app/solution.py:
IMPOSSIBLE

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
AERLAND DERLAND 1:0
DERLAND CERLAND 0:0
CERLAND AERLAND 1:0
AERLAND BERLAND 0:0
DERLAND BERLAND 1:0


Expected Output:
1:0

Actual Output from /app/solution.py:
2:1
FAILED

=================================== FAILURES ===================================
__________________________ test_code_contest_solution __________________________

    def test_code_contest_solution():
        """Test the solution using pytest assertions"""
    
        # Load test data
        test_data_path = "/tests/test_data.json"
    
        if not os.path.exists(test_data_path):
            assert False, "Test data file not found at /tests/test_data.json"
    
        with open(test_data_path, "r") as f:
            test_data = json.load(f)
    
        inputs = test_data.get("inputs", [])
        expected_outputs = test_data.get("outputs", [])
    
        # Check that we have test cases
        assert inputs, "No input test cases found in test data"
        assert expected_outputs, "No output test cases found in test data"
        assert len(inputs) == len(expected_outputs), f"Mismatch: {len(inputs)} inputs vs {len(expected_outputs)} outputs"
    
        # Verify solution file exists at /app/solution.py
        solution_file = "/app/solution.py"
        assert os.path.exists(solution_file), f"Solution file not found at {solution_file}. Please write your solution to /app/solution.py"
    
        # Run tests
        for i, (inp, expected) in enumerate(zip(inputs, expected_outputs)):
            print(f"\n{'='*60}", flush=True)
            print(f"Test {i+1}/{len(inputs)}", flush=True)
            print(f"{'='*60}", flush=True)
            print(f"Input:", flush=True)
            print(inp, flush=True)
            print(f"\nExpected Output:", flush=True)
            print(expected, flush=True)
    
            actual = run_solution(inp)
            assert actual is not None, f"Test {i+1}: Failed to run solution"
    
            print(f"\nActual Output from /app/solution.py:", flush=True)
            print(actual, flush=True)
    
            # Normalize outputs for comparison
            expected_lines = expected.strip().split('\n')
            actual_lines = actual.strip().split('\n')
    
            # Assert outputs match
>           assert expected_lines == actual_lines, f"\nTest {i+1} FAILED! Expected: {expected_lines} but got: {actual_lines}"
E           AssertionError: 
E             Test 4 FAILED! Expected: ['1:0'] but got: ['2:1']
E           assert ['1:0'] == ['2:1']
E             At index 0 diff: '1:0' != '2:1'
E             Full diff:
E             - ['2:1']
E             + ['1:0']

tmprpqzk5a5.py:73: AssertionError
=========================== short test summary info ============================
FAILED tmprpqzk5a5.py::test_code_contest_solution - AssertionError: 
============================== 1 failed in 1.38s ===============================
```

## raw response

```json
{
  "status": "Failed",
  "message": "",
  "compile_result": null,
  "run_result": {
    "status": "Finished",
    "execution_time": 3.327153444290161,
    "return_code": 1,
    "stdout": "============================= test session starts ==============================\nplatform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0\nPyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2\nrootdir: /tmp/tmp66dr0aiw\nconfigfile: pytest.ini\nplugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1\ncollected 1 item\n\ntmprpqzk5a5.py::test_code_contest_solution \n============================================================\nTest 1/10\n============================================================\nInput:\nAERLAND DERLAND 2:1\nDERLAND CERLAND 0:3\nCERLAND AERLAND 0:1\nAERLAND BERLAND 2:0\nDERLAND BERLAND 4:0\n\n\nExpected Output:\n6:0\n\nActual Output from /app/solution.py:\n6:0\n\n\u2713 Test 1 PASSED - Output matches expected!\n\n============================================================\nTest 2/10\n============================================================\nInput:\nAERLAND DERLAND 2:2\nDERLAND CERLAND 2:3\nCERLAND AERLAND 1:3\nAERLAND BERLAND 2:1\nDERLAND BERLAND 4:1\n\n\nExpected Output:\nIMPOSSIBLE\n\nActual Output from /app/solution.py:\nIMPOSSIBLE\n\n\u2713 Test 2 PASSED - Output matches expected!\n\n============================================================\nTest 3/10\n============================================================\nInput:\nCRWEYDMET BERLAND 6:2\nJ CRWEYDMET 5:4\nLYUTZZCGW BERLAND 8:4\nLYUTZZCGW CRWEYDMET 3:4\nLYUTZZCGW J 2:2\n\n\nExpected Output:\nIMPOSSIBLE\n\nActual Output from /app/solution.py:\nIMPOSSIBLE\n\n\u2713 Test 3 PASSED - Output matches expected!\n\n============================================================\nTest 4/10\n============================================================\nInput:\nAERLAND DERLAND 1:0\nDERLAND CERLAND 0:0\nCERLAND AERLAND 1:0\nAERLAND BERLAND 0:0\nDERLAND BERLAND 1:0\n\n\nExpected Output:\n1:0\n\nActual Output from /app/solution.py:\n2:1\nFAILED\n\n=================================== FAILURES ===================================\n__________________________ test_code_contest_solution __________________________\n\n    def test_code_contest_solution():\n        \"\"\"Test the solution using pytest assertions\"\"\"\n    \n        # Load test data\n        test_data_path = \"/tests/test_data.json\"\n    \n        if not os.path.exists(test_data_path):\n            assert False, \"Test data file not found at /tests/test_data.json\"\n    \n        with open(test_data_path, \"r\") as f:\n            test_data = json.load(f)\n    \n        inputs = test_data.get(\"inputs\", [])\n        expected_outputs = test_data.get(\"outputs\", [])\n    \n        # Check that we have test cases\n        assert inputs, \"No input test cases found in test data\"\n        assert expected_outputs, \"No output test cases found in test data\"\n        assert len(inputs) == len(expected_outputs), f\"Mismatch: {len(inputs)} inputs vs {len(expected_outputs)} outputs\"\n    \n        # Verify solution file exists at /app/solution.py\n        solution_file = \"/app/solution.py\"\n        assert os.path.exists(solution_file), f\"Solution file not found at {solution_file}. Please write your solution to /app/solution.py\"\n    \n        # Run tests\n        for i, (inp, expected) in enumerate(zip(inputs, expected_outputs)):\n            print(f\"\\n{'='*60}\", flush=True)\n            print(f\"Test {i+1}/{len(inputs)}\", flush=True)\n            print(f\"{'='*60}\", flush=True)\n            print(f\"Input:\", flush=True)\n            print(inp, flush=True)\n            print(f\"\\nExpected Output:\", flush=True)\n            print(expected, flush=True)\n    \n            actual = run_solution(inp)\n            assert actual is not None, f\"Test {i+1}: Failed to run solution\"\n    \n            print(f\"\\nActual Output from /app/solution.py:\", flush=True)\n            print(actual, flush=True)\n    \n            # Normalize outputs for comparison\n            expected_lines = expected.strip().split('\\n')\n            actual_lines = actual.strip().split('\\n')\n    \n            # Assert outputs match\n>           assert expected_lines == actual_lines, f\"\\nTest {i+1} FAILED! Expected: {expected_lines} but got: {actual_lines}\"\nE           AssertionError: \nE             Test 4 FAILED! Expected: ['1:0'] but got: ['2:1']\nE           assert ['1:0'] == ['2:1']\nE             At index 0 diff: '1:0' != '2:1'\nE             Full diff:\nE             - ['2:1']\nE             + ['1:0']\n\ntmprpqzk5a5.py:73: AssertionError\n=========================== short test summary info ============================\nFAILED tmprpqzk5a5.py::test_code_contest_solution - AssertionError: \n============================== 1 failed in 1.38s ===============================\n",
    "stderr": ""
  },
  "executor_pod_name": null,
  "files": {}
}
```
