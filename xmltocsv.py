# Import the necessary libraries
import csv
import xml.etree.cElementTree as ET
from lxml import etree

# Parse xml document and get the root
parser = etree.XMLParser(recover=True)
tree = ET.parse('unlabeled_review.xml', parser = parser)
root = tree.getroot()

# Create and open csv file
xml_data_to_csv = open('result.csv', 'w')

# Create the list that contains header of the csv file
data_head = []

# Create a variable to write the csv file
Csv_writer = csv.writer(xml_data_to_csv)

# Loop for each node
count = 0
i = 0


for x in root.findall('review'):
    List_nodes = []
    if count == 0:
        # Get head by the tag
        unique_id = x.find('unique_id').tag
        data_head.append(unique_id)
        
        asin = x.find('asin').tag
        data_head.append(asin)
        
        product_name = x.find('product_name').tag
        data_head.append(product_name)
        
        product_type = x.find('product_type').tag
        data_head.append(product_type)
        
        helpful = x.find('helpful').tag
        data_head.append(helpful)
        
        rating = x.find('rating').tag
        data_head.append(rating)
        
        title = x.find('title').tag
        data_head.append(title)
        
        date = x.find('date').tag
        data_head.append(date)
        
        reviewer = x.find('reviewer').tag
        data_head.append(reviewer)
        
        reviewer_location = x.find('reviewer_location').tag
        data_head.append(reviewer_location)
        
        review_text = x.find('review_text').tag
        data_head.append(review_text)
        
        # Write the header in csv file
        Csv_writer.writerow(data_head)
        count = count + 1
    
    unique_id = x.find('unique_id').text
    List_nodes.append(unique_id)
    
    asin = x.find('asin').text
    List_nodes.append(asin)
    
    product_name = x.find('product_name').text
    List_nodes.append(unique_id)
    
    product_type = x.find('product_type').text
    List_nodes.append(product_type)
    
    helpful = x.find('helpful').text
    List_nodes.append(helpful)
    
    rating = x.find('rating').text
    List_nodes.append(rating)
    
    title = x.find('title').text
    List_nodes.append(title)
    
    date = x.find('date').text
    List_nodes.append(date)
    
    reviewer = x.find('reviewer').text
    List_nodes.append(reviewer)
    
    reviewer_location = x.find('reviewer_location').text
    List_nodes.append(unique_id)
    
    review_text = x.find('review_text').text
    List_nodes.append(review_text)
    
    Csv_writer.writerow(List_nodes)
xml_data_to_csv.close()
    
import pandas as pd
dataset = pd.read_csv('result.csv')
     