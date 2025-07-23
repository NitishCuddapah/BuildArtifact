import requests

def main():
    print('Hello, this is just demonstration of codebuild')
    response =  requests.get("https://api.github.com")
    if response.status_code == 200:
        print("Reached github API")
        print(response.headers)
    else:
        print('Failed to reach github API')

if __name__ == '__main__':
    main()   