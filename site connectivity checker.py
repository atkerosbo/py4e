#site connectivity checker
import urllib.request as urllib

def main(url):
    print("Checking connectivity")

    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("the response code was: " , response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the URL of the site: ")

main(input_url)
