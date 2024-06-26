from jinja2 import Template
import requests, os, sys, datetime

#https://github.com/Ileriayo/markdown-badges

BADGES_DEV = [
    "![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)",
    "![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)",
    "![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)",
    "![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)",
    "![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)",
    "![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)",
    "![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)",
    "![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)",
]


BADGES_DEVOPS = [
    "![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)",
    "![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)",
    "![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)",
    "![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)",
    "![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)",
]

BADGES_DB = [
    "![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)",
    "![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)",
]

BADGES_AUTRE = [
    "![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)",
    "![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)",

]
    
def get_weather(city):
    url = 'https://wttr.in/{}?m&format=3'.format(city)
    res = requests.get(url)
    return res.text

def get_date():
    return datetime.datetime.now()

PATH_PREFIX = "/home/nsakkriou/github-profile-update/nSakkriou/"

if __name__ == "__main__":
    city = "Rennes"

    if(len(sys.argv) > 1):
        city = sys.argv[1]

    with open(PATH_PREFIX + "README.template.md", "r") as f:
        templateFile = f.read()

    templateJinja = Template(templateFile)

    data = {
       	"badgesDev" : BADGES_DEV,
	"badgesDevops" : BADGES_DEVOPS,
	"badgesDb" : BADGES_DB,
	"badgesAutre" : BADGES_AUTRE,
        "weather" : get_weather(city),
   	"date": get_date()
    }

    with open(PATH_PREFIX + "README.md", "w", encoding="utf-8") as readme:
        readme.write(templateJinja.render(data))
