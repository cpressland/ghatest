import requests


def main():
    r = requests.get("https://httpstat.us/200")
    print(r.text)


if __name__ == "__main__":
    main()
