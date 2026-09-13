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
]

success_count = 0
failed_count = 0 


for status in login_status:
    if status == "success":
        success_count = success_count + 1
    elif status == "failed":
        failed_count = failed_count + 1

print("Number of successful logins:", success_count)
print("Number of failed logins:", failed_count)