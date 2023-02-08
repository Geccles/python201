with open("emails.txt", "r") as emails:
    emails = emails.readlines()

for email in emails:
    if "hotmail" in email:
        print(f"Found email address with hotmail: {email.rstrip()}")