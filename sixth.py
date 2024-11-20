import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    try:

        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"HTTP chyba: {response.status_code}")


        content = response.text
        hrefs = re.findall(r'<a\s+href=["\'](.*?)["\']', content)

        return hrefs
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Chyba při stahování URL: {e}")


if __name__ == "__main__":
    try:

        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)


        for link in links:
            print(link)


    except Exception as e:
        print(f"Program skončil chybou: {e}")
