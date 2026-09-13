login_status = [
    "success",
    "failed",
    "failed",
    "failed",
    "success",
    "success",
    "failed",
    "success",
    "success",
    "failed",
    "unknown",
    "xss",
    "unkown2",
    "unknown3",
    "unknown"
]

success_count = 0
failed_count = 0
unrecognized_count = 0


for status in login_status:
    if status == "success":
        success_count = success_count + 1
    elif status == "failed":
        failed_count = failed_count + 1
    elif status != "success" and status != "failed":
        unrecognized_count = unrecognized_count + 1

print("Number of successful logins:", success_count)
print("Number of failed logins:", failed_count)
print("Number of unrecognized:", unrecognized_count)

total_counted = success_count + failed_count + unrecognized_count
print("total counted:", total_counted, "| total data:", len(login_status))