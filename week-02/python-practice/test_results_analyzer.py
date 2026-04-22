total_test_counter = 0
passed_counter = 0
failed_counter = 0
total_duration = 0.0
longest_test_duration = 0.0
longest_test_name = ""
failed_tests = []
summary = {}

test_results = [
    ("login_valid_user", "passed", 1.2),
    ("login_invalid_password", "failed", 0.8),
    ("checkout_with_card", "passed", 2.5),
    ("checkout_with_coupon", "failed", 2.1),
    ("profile_update", "passed", 1.7),
    ("logout", "passed", 0.4),
    ("reset_password", "failed", 1.9),
]

for test in test_results:
    total_test_counter += 1
    total_duration += test[2]
    if "passed" in test:
        passed_counter += 1
    if "failed" in test:
        failed_counter +=1
        failed_test_name, _, _ = test
        failed_tests.append(failed_test_name)
    if test[2] > longest_test_duration:
        longest_test_duration = test[2]
        longest_test_name, _, _ = test

summary["total"] = total_test_counter
summary["passed"] = passed_counter
summary["failed"] = failed_counter
summary["total_duration"] = total_duration
summary["longest_test"] = longest_test_name

print(f"Total tests: {total_test_counter}")
print(f"Passed: {passed_counter}")
print(f"Failed: {failed_counter}")
print(f"Total duration: {total_duration}")
print(f"Longest test: {longest_test_name} - {longest_test_duration}")
print("Failed tests:")
for test in failed_tests:
    print(f" - {test}")

print(summary)