import sys
import requests
import bs4

# Example Usage
# $>d.py http://www.google.com links.txt
if len(sys.argv) == 3:
    url = sys.argv[1]
    file_name = sys.argv[2]

    # Make the request
    print('Daving the Page...')
    response = requests.get(url)
    response.raise_for_status()

    # Retrieve all links on the page
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    # Print links to text file
    file = open(file_name, 'wb')
    print('Collecting the links...')

    for link in links:
        href = link.get('href') + '\n\n'
        file.write(href.encode())

    # Close File
    file.close()
    print('Saved to %s' % file_name)

# output usage instructions
else:
    print('Usage: ./collect_links.py wwww.example.com file.txt')
