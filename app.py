import sys
import requests
from pprint import pprint


def main():
    print("Executing Python Module")

    # getting parameter passed
    url = sys.argv[1]

    print(f"Parameter from shellscript: {url}")

    # retrieve data from url using HTTP Get method
    result = requests.get(url)
    
    pprint(result.json())


if __name__ == "__main__":
    main()