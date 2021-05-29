import requests


def get_random_wiki_article_link():
    WIKI_RANDOM_LINK_API_URL = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=1&format=json"

    response = requests.get(WIKI_RANDOM_LINK_API_URL)

    if response.status_code == 200:
        random_article_data = response.json()['query']['random']
        random_article_title = random_article_data[0]['title']
        return random_article_title
    else:
        print("Something went wrong! Please try again!")


def main():
    article_base_url = "https://en.wikipedia.org/wiki/"

    while True:
        random_article = get_random_wiki_article_link()
        user_response = input(f"Would you like to read `{random_article}` (Y/N): ")
        if user_response.lower() == 'y':
            print(f"{article_base_url}{'_'.join(random_article.split())}")
            break

if __name__ == '__main__':
    main()