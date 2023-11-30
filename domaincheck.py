#!/usr/bin/

# importing module
import requests
from prettytable import PrettyTable
def domain_scanner(domain_name,sub_domnames):
    domainlist = PrettyTable(['Domain Name', 'Status'])
    print('----After URL scanning subdomains----')
    # loop for getting URL's
    for subdomain in sub_domnames:       
        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"         
        # using try catch block to avoid crash of the program
        try:
            # sending get request to the url
            requests.get(url)
            # if after putting subdomain one by one url is valid then printing the url
            domainlist.add_row([f'[+] {url}', 'UP'])
            # if url is invalid then pass it
        except requests.ConnectionError:
            domainlist.add_row([f'[-] {url}', 'DOWN'])
    print(domainlist)

# main function
if __name__ == '__main__':
    # inputting the domain name
    dom_name = input("Enter the Domain Name:")
 
    # opening the subdomain text file
    with open('subdomainlist.txt','r') as file:
       
        # reading the file
        name = file.read()
        # using splitlines() function storing the list of splitted strings
        sub_dom = name.splitlines()

    # calling the function for scanning the subdomains and getting the url
    domain_scanner(dom_name,sub_dom)