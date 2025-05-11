print("🔎 WEBSITE URL CHECKER 🔍")
url = input("\nEnter a website url: ")

if url.startswith("https://"):
    print("This website uses a HTTPS (secure)")
elif url.startswith("http://"):
    print("This website uses a HTTP (Insecure)")
else:
    print("This does not look like a complete URL")
