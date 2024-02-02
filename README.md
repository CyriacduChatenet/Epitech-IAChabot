# Footix
> Football chatbot crafted with a Mistral AI model, Langchain & Flask framework

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Demo](#demo)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Team](#team)
* [Status](#status)
* [Inspiration](#inspiration)

## General info
This is a school project which aim was to create an innovative chatbot capable of using Natural Langage Processing (NLP) to retreive answers in a string-typed database. 
The database was scraped using Langchain.
<br>We chose to focus on the sport topic, precisely, football. Footix the chatbot allows the user to ask information about anything related to football. Then, it gives back the corresponding answer, using NLP, within 10 seconds!
<br><br>We had 14 days to implement the project. We made it in 5.
<br><br>Here, you can find the source code of Footix, the football chatbot, but the algorithm could be adapted to any kind of subject. We also added a scraping script we coded to be able to retreive the european championship scores : `scraping.py`

## Screenshots

![MicrosoftTeams-image (2)](https://github.com/ael-tek/Lil-Bot/assets/63455059/bdd8a999-430f-4479-a272-98ba7a1c6686)

## Demo

https://github.com/CyriacduChatenet/Footix/assets/63455059/7dafad26-2597-4c88-ab2c-b48332e596c6

<br> (No sound for compressing reasons) <br>

## Technologies
* Python 3.11.7
* Flask 3.0.1
* Werkzeug 3.0.1
* Langchain
* Mistral 7B
* Javascript
* HTML/CSS

[![python](https://img.shields.io/badge/Python-3572A5?style=for-the-badge&logo=python&logoColor=FFFFFF)](https://www.python.org/)
[![html5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://devdocs.io/css/)
[![css3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://devdocs.io/html/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)


## Setup
1- If not done, install Python:
<br><br>
https://www.python.org/downloads/
<br><br><br>
2- Install Langchain:
<br><br>
`pip install langchain`
<br><br><br>
3- Install Flask:
<br><br>
`pip install flask`
`pip install flask_cors`
<br><br><br>
4- Follow the possible package installations that will be asked by the Langchain dependances
<br><br><br>
5- ⚠️ If you want to scrap the Ligue 1 data (and not be using the `results.csv` data), you need to go into the `test.py` file, uncomment the line 24 and comment the line 25 ⚠️

## Features

## Team
Project made by 
*  @MattisFernandez, AI Engineer
*  @ael-tek, AI Engineer
*  @CyriacduChatenet, Developer
*  @Juliette-Dupin, Developer
  
## Status
Project is: _finished_ since Friday, February 2, 2024

## Inspiration
* The chatbot's name, Footix, is a French denomination. Nowadays, the word "Footix" can be considered the worst insult to say to a football fan, meaning they don't know football or start following a team because they won. :trollface:
* No one on the team likes football. One is a fan of hockey, another one of rugby, another one likes horse riding and the another swimming. In short, we don't like football. But we chose this sport 'cause people tend to like it. :trollface:
