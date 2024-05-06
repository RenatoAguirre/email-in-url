import re
import urllib.request

def main():
    regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    url = input("Enter the URL: ")  

    data = read_url(url)

    matches = regex.finditer(data)
    print("All emails in the given url:")
    for match in matches:
        print(match)

def read_url(url: str) -> str:
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            return str(html)
    except ValueError:
        print("Error reading the URL")
        return ""


if __name__ == "__main__":
    main()