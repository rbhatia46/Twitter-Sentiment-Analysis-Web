# Twitter-Sentiment-Analysis-Web
Twitter Sentiment Analysis using Textblob and Tweepy, wrapped with Flask as a web app.

![Working Demo](https://i.ibb.co/Vx8stRF/Working.gif)

## Installation
1. Clone/Download this repository.
2. Obtain your Twitter API credentials.
3. Replace appropriate credentials in ```main.py``` file.
4. Install all the required dependencies listed in ```requirements.txt```.
5. Run the flask server using ```python main.py``` to see the result on port 5000(by default).

## A brief on the libraries used :
Mainly I have used  TextBlob and Tweepy for the main functionality. TextBlob is a great choice for NLP tasks, built on top of the famous Python library for NLP, i.e., NLTK.
Tweepy is used for Interacting easily with the Twitter API and handling complex tasks such as Authentication(OAuth) with a breeze.

TextBlob allows us to perform sentiment analysis with very few lines of code.
Applying ```.sentiment``` on a TextBlob gives us two things - **Polarity** and **Subjectivity**. <br><br>
* Polarity is a float value within the range [-1.0 to 1.0] where 0 indicates neutral, +1 indicates a very positive sentiment and -1 represents a very negative sentiment.

* Subjectivity is a float value within the range [0.0 to 1.0] where 0.0 is very objective and 1.0 is very subjective. Subjective sentence expresses some personal feelings, views, beliefs, opinions, allegations, desires, beliefs, suspicions, and speculations where as Objective sentences are factual.
