def get_failed_tests(test_results: list[tuple]) -> list[str]:
    failed_tests = []
    for name, status, _ in test_results:
        if status == "failed":
            failed_tests.append(name)
    
    return failed_tests


def get_longest_test(test_results: list[tuple]) -> tuple[str, float]:
    longest_test = ("", 0.0)
    for name, _, duration in test_results:
        if duration > longest_test[1]:
            longest_test = name, duration
    
    return longest_test


def get_passed_tests(test_results: list[tuple]) -> list[str]:
    passed_tests = []
    for name, status, _ in test_results:
        if status == "passed":
            passed_tests.append(name)
    
    return passed_tests


def total_test_duration(test_results: list[tuple]) -> float:
    total_duration = 0.0
    for _, _, duration in test_results:
        total_duration += duration
    
    return total_duration


def get_pass_rate(test_results: list[tuple]) -> float:
    pass_rate = len(get_passed_tests(test_results)) / len(test_results) * 100
    pass_rate = round(pass_rate, 1)
    return pass_rate


def average_test_duration(test_results: list[tuple]) -> float:
    average_duration = total_test_duration(test_results) / len(test_results)
    average_duration = round(average_duration, 2)
    return average_duration


def get_slow_tests(test_results: list[tuple], threshold: float) -> list[str]:
    slow_tests = []
    for name, _, duration in test_results:
        if duration > threshold:
            slow_tests.append(name)
    
    return slow_tests


def analyze_tests(test_results: list[tuple]) -> dict:
    analyze_test_summary = {}
    analyze_test_summary["total"] = len(test_results)
    analyze_test_summary["passed"] = len(get_passed_tests(test_results))
    analyze_test_summary["failed"] = len(get_failed_tests(test_results))
    analyze_test_summary["total_duration"] = total_test_duration(test_results)
    analyze_test_summary["longest_test"] = get_longest_test(test_results)
    analyze_test_summary["pass_rate"] = get_pass_rate(test_results)
    analyze_test_summary["average_duration"] = average_test_duration(test_results)
    analyze_test_summary["slow_tests"] = get_slow_tests(test_results, 2.0)
    return analyze_test_summary

test_results = [
    ("login_valid_user", "passed", 1.2),
    ("login_invalid_password", "failed", 0.8),
    ("checkout_with_card", "passed", 2.5),
    ("checkout_with_coupon", "failed", 2.1),
    ("profile_update", "passed", 1.7),
    ("logout", "passed", 0.4),
    ("reset_password", "failed", 1.9),
]

analyze_test_results = analyze_tests(test_results)
print("=== TEST SUMMARY ===")
print(f"Total: {analyze_test_results.get('total')}")
print(f"Passed: {analyze_test_results.get('passed')}")
print(f"Failed: {analyze_test_results.get('failed')}")
print(f"Total duration: {analyze_test_results.get('total_duration')}")
print(f"Longest test: {analyze_test_results.get('longest_test')}")
print(f"Pass rate: {analyze_test_results.get('pass_rate')}")
print(f"Average duration: {analyze_tests_result.get('average_duration')}")
print(f"Slow tests: {analyze_test_results.get('slow_tests')}")