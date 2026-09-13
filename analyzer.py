login_status = [
    "success",
    "success",
    "success",
    "success",
    "failed",
    "failed",
    "failed",
    "failed",
    "failed",
    "failed",
    "failed",
    "success",
    "success",
    "success",
    "failed",
    "unknown",
    "unknown",
    "failed",
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

print("login success:",success_count)
print("login failed:",failed_count)
print("unrecognized:",unrecognized_count)

print("Data total:", success_count + failed_count + unrecognized_count)
