from bs4 import BeautifulSoup
# with open(file="website.html") as website:
#     contents=website.read()
#
# soup=BeautifulSoup(contents,"html.parser")
import requests
response=requests.get("https://news.ycombinator.com/")
webpage_contents=response.text
soup=BeautifulSoup(webpage_contents,"html.parser")
article_text=soup.find_all(name="a",class_="titlelink")
article_link=soup.find_all(name="a",class_="titlelink")
article_score=soup.find_all(name="span",class_="score")
text=[texts.getText() for texts in article_text]
link=[links.get("href") for links in article_link]
score=[int(scores.getText().split()[0]) for scores in article_score]
max_score=max(score)
max_score_index=score.index(max_score)
max_score_text=text[max_score_index]
max_score_link=link[max_score_index]
print(max_score_text)
print(max_score_link)

