import requests, json, sys
from pyfiglet import Figlet

title = Figlet(font='slant').renderText("Track Loc")
version = 1
author = "Fyke Lleva"

def main():
    print(f'''
{title} 
version: {version}
author: {author}
    ''')
    menu()

def getLocation(ip_address):
    responds = requests.get(f'http://ip-api.com/json/{ip_address}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query').json()
    data = json.dumps(responds, indent=4)
    return data

def menu():
    print('''
------------------------
Welcome to ip locator!

press (s) to start
press (e) to exit             
          
------------------------
''')
    while True:
        choice = str(input("Choose selection: "))
        if choice == 's':
            ip_address = input("IP Address: ")
            res = getLocation(ip_address)
            print (res)
            continue
        elif choice == 'e':
            print("You've Exited!")
            sys.exit()
        else:
            print("Invalid Input!")
            continue



if __name__ == "__main__":
    main()