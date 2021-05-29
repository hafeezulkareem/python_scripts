import requests
import bs4


URL = "https://en.wikiquote.org/wiki/Main_Page"

def get_a_quote():
    response = requests.get(URL)
    source_code = response.content

    soup = bs4.BeautifulSoup(source_code, 'html.parser')

    daily_quote_section = soup.find_all('table')[3].table
    sections = daily_quote_section.find_all('tr')
    quote, author = sections[0], sections[1]

    print(quote.td.text)
    print(author.td.text)
    print(f"Source:- {URL[0:len(URL) - 14]}")


if __name__ == "__main__":
    get_a_quote()