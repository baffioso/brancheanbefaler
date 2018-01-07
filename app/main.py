from flask import Flask, request, render_template
from sklearn.externals import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import DanishStemmer

nltk.download('stopwords')
stopwords = stopwords.words('danish')
stemmer = DanishStemmer()

def text_process(name):
    """
    Tekstprocessering som laver om til små bogstaver, fjerner stopord og finder ordstammen
    """
    lst = name.lower().split(' ')
    stop = [word for word in lst if word not in stopwords]
    stem = [stemmer.stem(word) for word in stop]

    return stem

pipeline = joblib.load('model/predict_business.pkl')

def predict_business(name):
    return pipeline.predict([name])[0]

app = Flask(__name__)

@app.route('/')
def search():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def prediction():
    text = request.form['text']
    prediction = predict_business(text)
    return render_template('index.html', text = prediction)

if __name__ == '__main__':
    app.run(debug = True)