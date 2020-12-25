import requests
import subprocess
import sys

title_art = r"""

 ######  ##     ## ########  #### ##    ## ##    ## ##     ## ########     ####  #######  
##    ## ##     ## ##     ##  ##  ###   ## ##   ##  ###   ### ##            ##  ##     ## 
##       ##     ## ##     ##  ##  ####  ## ##  ##   #### #### ##            ##  ##     ## 
 ######  ######### ########   ##  ## ## ## #####    ## ### ## ######        ##  ##     ## 
      ## ##     ## ##   ##    ##  ##  #### ##  ##   ##     ## ##            ##  ##     ## 
##    ## ##     ## ##    ##   ##  ##   ### ##   ##  ##     ## ##       ###  ##  ##     ## 
 ######  ##     ## ##     ## #### ##    ## ##    ## ##     ## ######## ### ####  #######  """
print(title_art+'\n')


def main():

    movie_name = input("Enter Your Long Url:\n")
    print(f"Generating......")
    base_url = f"https://shrinkme.io/api?api=9b8aab2630a0e5c289837488ea83536e6912dd99&url={movie_name}"
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    index = 0
    print("Your Shot Url= "+data['shortenedUrl']+'\n'+"Created By Seshu Sai")

if __name__ == "__main__":
    main()
