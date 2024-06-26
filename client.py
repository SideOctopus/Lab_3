import requests

def main():
    base_url = 'http://127.0.0.1:5000/data'
    
    while True:
        print("1) Send POST-request")
        print("2) Send GET-request")
        print("3) Exit")
        choice = int(input("Your choice: "))
        
        if choice == 1:
            message = input("Enter your message: ")
            response = requests.post(base_url, data=message)
            print('POST response:', response.text)
        elif choice == 2:
            response = requests.get(base_url)
            print('GET response:', response.json())
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
