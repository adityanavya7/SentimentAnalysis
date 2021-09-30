# SentimentAnalysis
A machine learning end to end flask web app for sentiment analysis model created using Scikit-learn &amp; VADER Sentiment. <br />
The project uses technologies like : <br />
[Flask](https://flask.palletsprojects.com/en/2.0.x/)<br />
[Sklearn](https://pypi.org/project/scikit-learn/) <br />
[Requests](https://docs.python-requests.org/en/latest/) <br />
[NLTK](https://www.nltk.org/) <br />
[RE](https://docs.python.org/3/library/re.html) <br />
[vaderSentiment](https://pypi.org/project/vaderSentiment/) <br />
[Bootsrap 5](https://getbootstrap.com/docs/5.1/getting-started/introduction/) <br />
[Python](https://www.python.org/downloads/windows/) <br />

### VADER SENTIMENT <br />
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains. <br />
More about [VADER](https://pypi.org/project/vaderSentiment/)
<br />
<br />

### WHAT IS SENTIMENT ANALYSIS <br />
Sentiment analysis, an important area in Natural Language Processing, is the process of automatically detecting affective states of text. Sentiment analysis is widely applied to voice-of-customer materials such as product reviews in online shopping websites like Amazon, movie reviews or social media. It can be just a basic task of classifying the polarity of a text as being positive/negative or it can go beyond polarity, looking at sentiment states etc. <br />
Sentiment analysis refers to analyzing an opinion or feelings about something using data like text or images, regarding almost anything. Sentiment analysis helps companies in their decision-making process. For instance, if public sentiment towards a product is not so good, a company may try to modify the product or stop the production altogether in order to avoid any losses. <br />

There are many sources of public sentiment e.g. public interviews, opinion polls, surveys, etc. However, with more and more people joining social media platforms, websites like Facebook and Twitter can be parsed for public sentiment. <br />
<br />

## Commands to run the Application <br />

### [Git](https://git-scm.com/downloads) <br />

If you already have Git installed, you can get the latest development version via Git itself: *git clone https://github.com/git/git* <br />

### [Python 3 or above](https://www.python.org/downloads/) <br />

If you already have Python installed, you can check the version on command prompt by the command*$ python --version* <br />

### PIP <br />

> *python get-pip.py* <br />

One can easily verify if the pip has been installed correctly by performing a version check on the same. Just go to the command line and execute the following command: <br />
> *pip -V*


### For Flask <br />

Create an environment <br />
> *mkdir myproject <br />*
> *cd myproject <br />*
> *py -3 -m venv venv* <br />

Or, create a virtual environment by <br />
> *pip virtualenv*

Before you work on your project, activate the corresponding environment: <br />
> *venv\Scripts\activate* <br />

Within the activated environment, use the following command to install Flask: <br />
> *$ pip install Flask*

### Installing NLTK <br />

NLTK requires Python versions 3.6, 3.7, 3.8, or 3.9
> *pip install nltk* <br />
Test installation: *Start > Python38 then type import nltk*

### scikit-learn <br />

> *pip install -U scikit-learn* <br />

In order to check your installation you can use <br />
> *python -m pip show scikit-learn  # to see which version and where scikit-learn is installed* <br />
> *python -m pip freeze  # to see all packages installed in the active virtualenv* <br />
> *python -c "import sklearn; sklearn.show_versions()"* <br />

### sklearn install

> *pip install sklearn*

### vaderSentiment 

> *pip install vaderSentiment*

## Necessary Files

### app.py

The *app.py* is the main file with all the backend functions and all the background calculations needed in order to calculate the sentiment of a particular string <br />
The imported libraries which are necesaary to run are <br />
<br />
![](/CodeSamples/app2.PNG) <br />

In order to run the application we have to activate the virtual environment and all the above necessary libraries and files must be installed <br />
Then, we will run the application by the following command <br />

> *set FLASK_APP=app.py*  <br />
> *flask run* <br />

The main parametre on which the sentiment is to get calculated is <br />
<br />
![paramater](/CodeSamples/app1.PNG) <br />

On running the command, we get something like this <br />
<br />
![](/CodeSamples/run.PNG) <br />

Here *env* specifies that the application is running in an virtual environment.


### templates/start.html

The *start.html* is the front page that will load when the application will start to run and the shows the output of the input string.
While running the application, the start page looks something like this <br />
<br />
![](/CodeSamples/start.PNG) <br />

### templates/speech.html

The *speech.html* is what we get on clicking the speech tab on the nav bar. The purpose was to find the sentiment by retrieving the text from speech but unfortunately this is still under process, but we can retrieve the text from speech by this.

The *speech.html* will look like this <br />
<br />
![](/CodeSamples/speech.PNG) <br />

### templates/about.html

The *about.html* page is the about page of this project where we display the necessary innformation, the team involved, the technologies used and the problem statement.

The about page looks like : <br />
<br />
![](/CodeSamples/about.PNG) <br />

### templates/team.html

The *team.html* consistes details of the group along with our mentor and alumni.

The team page looks like : <br />
<br />
![](/CodeSamples/team.PNG)<br />

### templates/tech.html

The *tech.html* consistes the main technologies used along with their documentation.

The tech page looks like : <br />
<br />
![](/CodeSamples/tech.PNG)<br />

### templates/statem.html

The *statem.html* consistes the problem statement.

The statem page looks like : <br />
<br />
![](/CodeSamples/statem.PNG)<br />

### static style
