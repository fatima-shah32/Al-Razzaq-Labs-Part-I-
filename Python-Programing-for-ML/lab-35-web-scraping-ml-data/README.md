# Lab 35: Basic Web Scraping for ML Data

## Objective

Learn how to scrape, parse, and clean webpage data using BeautifulSoup and requests.

## Tools Used

- Python
- BeautifulSoup4
- Requests

## Steps Performed

1. Installed BeautifulSoup and Requests
2. Connected to https://example.com
3. Downloaded webpage HTML
4. Parsed HTML using BeautifulSoup
5. Extracted h1 data
6. Cleaned extracted text

## Main Code

```python
response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser"
)

headers = soup.find_all("h1")
Conclusion

In this lab, I learned how to use requests and BeautifulSoup to fetch, parse, extract, and clean webpage data. These skills can be used to collect datasets for machine learning projects.
