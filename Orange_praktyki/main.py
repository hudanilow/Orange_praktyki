import requests
import json
import time
import datetime

def program(url, counter):
    with open(filename, 'w') as f:

        while counter <= X:
            current_time = datetime.datetime.now()
            print(f"Request number {counter} at {current_time}")
            f.write(f"Request number {counter} at {current_time}, ")

            #GET request
            response = requests.get(url)
            # print(response.text)

            #time between request and response
            response_time = response.elapsed.total_seconds()
            print(f"Response time: {response_time} seconds")
            f.write(f"Response time: {response_time} seconds, ")

            #HTTP status code
            http_status_code = response.status_code

            if http_status_code == 200:
                print(f"HTTP status code: {http_status_code} which means OK")
                f.write(f"HTTP status code: {http_status_code} which means OK, ")
            else:
                print(f"HTTP status code: {http_status_code}")
                f.write(f"HTTP status code: {http_status_code}, ")

            #is Content-Type JSON
            content_type = response.headers["content-type"]

            if "application/json" in content_type:
                print(f"Response is JSON: {content_type}")
                f.write(f"Response is JSON: {content_type}, ")
            else:
                print(f"Response is: {content_type}")
                f.write(f"Response is: {content_type}, ")

            #JSON validate
            try:
                json.loads(response.content)
                print(f"JSON syntax is correct")
                f.write(f"JSON syntax is correct, ")
            except ValueError as e:
                print(f": {e}")
                f.write(f": {e}")
                exit()

            # File write
            f.write(f"\n")

            print('-' * 30)
            time.sleep(Y)
            counter += 1


if __name__ == '__main__':
    url = 'https://tvgo.orange.pl/gpapi/status'
    X = 10
    Y = 5
    filename = 'log.txt'
    counter = 1
    program(url, counter)


