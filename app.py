from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from string import punctuation
import re
from nltk.corpus import stopwords

nltk.download('stopwords')

set(stopwords.words('english'))

app = Flask(__name__, template_folder="templates")

@app.route('/')
def front_app():
    return render_template('start.html')

@app.route('/', methods=['POST'])
def front_app_post():
    stop_words = stopwords.words('english')
    
    input_text = request.form['inputText'].lower()
    
    output_text = ''.join(c for c in input_text if not c.isdigit())
        
    final_output = ' '.join([word for word in output_text.split() if word not in stop_words])

    sentiment_analyze = SentimentIntensityAnalyzer()
    dd = sentiment_analyze.polarity_scores(text=final_output)
    compound = round((1 + dd['compound'])/2, 2)

    return render_template('start.html', final=compound, input_text=output_text,text2=dd['pos'],text5=dd['neg'],text4=compound,text3=dd['neu'])

@app.route('/about.html')
def about():
    return render_template('about.html')
    
@app.route('/speech.html')
def speech():
    return render_template('speech.html')

@app.route('/speech.html', methods=['POST'])
def speech_post():
    stop_words = stopwords.words('english')
    
    input_text1 = request.form['x'].lower()
    
    output_text1 = ''.join(c for c in input_text1 if not c.isdigit())
        
    final_output = ' '.join([word for word in output_text1.split() if word not in stop_words])

    sentiment_analyze = SentimentIntensityAnalyzer()
    dd = sentiment_analyze.polarity_scores(text=final_output)
    compound = round((1 + dd['compound'])/2, 2)

    return render_template('speech.html', final=compound, input_text1=output_text1,text2=dd['pos'],text5=dd['neg'],text4=compound,text3=dd['neu'])

@app.route('/docu.html')
def docu():
    return render_template('docu.html')

@app.route('/statem.html')
def statem():
    return render_template('statem.html')

@app.route('/tech.html')
def tech():
    return render_template('tech.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000, threaded=True)

