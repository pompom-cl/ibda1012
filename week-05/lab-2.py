import requests
from bs4 import BeautifulSoup


def main():
  lines = []
  for i in range(26):
    # web_scrap(i + 97)
    lines += read_file(i + 97)

  cities = []
  for line in lines:
    cities += line.split('.')

  for i in range(len(cities)):
    cities[i] = cities[i].strip()
  print(cities)

  while True:
    city = input("\nEnter city name (x: exit): ").upper()
    if city == 'X':
      break
    if city in cities:
      print("Found")
      print('https://www.google.com/search?q=' + city.lower())
    else:
      print("Not found")


def web_scrap(letter):
  url = f"https://www.diedit.com/nama-kota-berawalan-huruf-{chr(letter)}/"
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    data_list = soup.find_all("p")
    with open(f"cities_{chr(letter)}.txt", "w", encoding='utf-8') as file:
      for data in data_list:
        file.write(data.text.strip() + "\n")
    print(f"Data cities_{chr(letter)}.txt has been successfully downloaded")


def query_name(cities, text):
  n = len(text)
  result = []
  for word in cities:
    n = len(text) - 1
    m = len(word)
    if text == word or \
        text[0] == "*" and word[m-n:] == text[1:] or \
        text[-1] == '*' and word[:n] == text[:n]:
      result.append([word])
  nomor = 1


def read_file(letter):
  lines = []
  with open(f"cities_{chr(letter)}.txt", "r", encoding='UTF-8') as file:
    for line in file:
      if line[0].isdigit() and len(line) > 1:
        lines.append(
            line.strip('\n').replace('0', '').replace('1', '').replace(
                '2',
                '').replace('3', '').replace('4', '').replace('5', '').replace(
                    '6', '').replace('7', '').replace('8', '').replace(
                        '9', '').replace('0', '').upper())
  return lines


if __name__ == "__main__":
  main()
