from exa_py import Exa

exa = Exa('2ec4ca91-5375-4d24-a2ea-3e81abd40715')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

print(response)