import requests
import subprocess
import sys

title_art = r"""
 ______  _____         _____ __   _ _     _ _______
 |  ____ |_____] |        |   | \  | |____/  |______
 |_____| |       |_____ __|__ |  \_| |    \_ ______|
 """
print(title_art+'\n')


def main():
 
    movie_name = input("Enter Your Long Url:\n")
    print(f"Generating......")
    base_url = f"https://gplinks.in/api?api=714d94cc0bee820944c8007db0f684d40e29fe27&url={movie_name}"
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    
    print("Your Shot Url= "+data['shortenedUrl']+'\n'+"Created By Seshu Sai")

if __name__ == "__main__":
    main()
