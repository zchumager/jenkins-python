import sys
import requests
from pprint import pprint

def main():
    print("Executing Python Module")

    print(f"Parameter from shellscript: {sys.argv[0]}")

    result = requests.get('https://jsonplaceholder.typicode.com/posts')
    pprint(result.json())

if __name__ == "__main__":
    main()