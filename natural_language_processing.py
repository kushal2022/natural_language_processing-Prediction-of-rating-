# Natural Language Processing

# Importing the libraries
import xml.etree.cElementTree as ET
from lxml import etree
import csv
import pandas as pd

# Data pre-processing 
parser = etree.XMLParser(recover=True)
tree = ET.parse('unlabeled_review.xml', parser = parser)
root = tree.getroot()

xml_to_csv = open('result.csv', 'w', newline = '', encoding = 'iso-8859-1', errors='ignore')
csv_writer = csv.writer(xml_to_csv)

col_names = ['rating', 'review_text']
csv_writer.writerow(col_names)

for x in root.findall('review'):
    list_nodes = []
    
    rating  = x.find('rating').text
    list_nodes.append(rating)
    
    review_text = x.find('review_text').text
    list_nodes.append(review_text)
    
    csv_writer.writerow(list_nodes)
xml_to_csv.close()

# Importing the dataset
dataset = pd.read_csv('result.csv')

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 7722):
    review = re.sub('[^a-zA-Z]', ' ', dataset['review_text'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)