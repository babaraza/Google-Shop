from bs4 import BeautifulSoup
import requests

# Searches through Google Shoppping for a Rotring 800 pen and returns results


def do_search(search_query):
    url = 'https://www.google.com/search'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    params = {
        'q': search_query,
        'tbm': 'shop',
        'source': 'lnms'
    }

    s = requests.Session()
    resp = s.get(url, headers=headers, params=params)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, 'lxml')
    results = soup.find_all(class_='sh-dlr__list-result')

    return results


def show_results(results):
    final_results = {}

    for result in results:
        # check = result.find_all('a')[1].text.lower()
        # if 'rotring' in check and 'pencil' not in check:
        final_results[float(result.find('span', {'aria-hidden': True}).text.replace('$', ''))] = result.find_all('a')[1].text

    for k, v in sorted(final_results.items()):
        print(f'${k} - {v}')


if __name__ == '__main__':
    show_results(do_search('rotring 800 pen'))
