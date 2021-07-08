import requests
from pprint import pprint

def main():
    print("Executing Python Module")

    result = requests.get('https://jsonplaceholder.typicode.com/posts')
    pprint(result.json())

if __name__ == "__main__":
    main()