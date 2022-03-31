from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from ngram_matcher import NgramMatcher
import uuid
import PyPDF2
import os
import numpy as np
import json

# Loading dataset into memory
fos_ids = np.load('fos_ids.npy', allow_pickle=True)
fos_names = np.load('fos_names.npy', allow_pickle=True)

with open('OSDG-mapping.json', 'r') as file_:
    mapping = [(sdg, set(fos_ids)) for sdg, fos_ids in json.load(file_).items()]

with open('OSDG-fosmap.json', 'r') as file_:
    fosmap = json.load(file_)

# Creating a NGram Matcher object
ngram_matcher = NgramMatcher(fos_names,
                             lowercase=True,
                             token_pattern=r'(?u)\b\w+\b',
                             ngram_size=(1, 4))
    
def extract_fos(text):
    idxs, frequencies = ngram_matcher.match([text])[0]
    ngrams = sorted(zip(fos_ids[idxs], fos_names[idxs], frequencies), key=lambda ng: len(ng[1]), reverse=True)
    descored_ngrams = list()
        
    for idx, (ngram_id, ngram_name, frequency) in enumerate(ngrams):
        for _, fol_ngram_name, fol_frequency in ngrams[:idx]:
            if ngram_name in fol_ngram_name:
                frequency -= fol_frequency
        
        if frequency > 0:
            descored_ngrams.append([ngram_id, ngram_name, frequency])
        
    ngrams = descored_ngrams
    submerged_ngrams, drop_ngram_ids = list(), set()
    
    for idx, (ngram_id, ngram_name, frequency) in enumerate(ngrams):
        for ngram_id2, ngram_name2, frequency2 in ngrams[idx+1:]:
            if ngram_name2 in ngram_name:
                frequency += frequency2
                drop_ngram_ids.add(ngram_id2)
        
        submerged_ngrams.append([ngram_id, ngram_name, frequency])
    
    submerged_ngrams = list(filter(lambda ng: ng[0] not in drop_ngram_ids, submerged_ngrams))
    
    return {fos_id: frequency for fos_id, _, frequency in submerged_ngrams}

def tag_sdg(fos):
    use_frequency = True
    n_min_relevant_fos = 1
    
    sdgs = []
    fos_ids = fos.keys()
    
    for sdg, sdg_fos_ids in mapping:
        relevant_fos_ids = sdg_fos_ids.intersection(fos_ids)
        
        if relevant_fos_ids and len(relevant_fos_ids) >= n_min_relevant_fos:
            if use_frequency:
                relevance = 0
                
                for fos_id in relevant_fos_ids:
                    relevance += fos.get(fos_id)
            
            else:
                relevance = len(relevant_fos_ids)
                
            sdgs.append({'sdg': sdg,
                         'relevance': float(relevance),
                         'fos_names': list(map(lambda fos_id: fosmap[fos_id], relevant_fos_ids))})
    
    return sorted(sdgs, key=lambda x: x['relevance'], reverse=True)
    
def pdf_to_text(location, start, end):
	pdf_file = open(location, 'rb')
	pdf_reader = PyPDF2.PdfFileReader(pdf_file)
	
	text = ''
	for i in range(start-1, end):
		page = pdf_reader.getPage(i)
		text += page.extractText()
		
	return text
	
app = Flask('SDG Classifier')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/classify', methods=['POST'])
def classifyText():
    if request.method=='POST':
    	posted_data = request.get_json()
    	fos = extract_fos(posted_data['text'])
    	sdgs = tag_sdg(fos)
    	return jsonify(sdgs)
        
@app.route('/classifyPDF', methods=['POST'])
def classifyPDF():
    if request.method=='POST':
    	form = request.form.to_dict()
    	file_name = str(uuid.uuid4()) + '.pdf'
    	file_ = request.files['file']
    	file_.save(file_name)
    	
    	text = pdf_to_text(file_name, int(form['start']), int(form['end']))
    	fos = extract_fos(text)
    	sdgs = tag_sdg(fos)
    	
    	os.remove(file_name)
    	
    	return jsonify(sdgs)
		
if __name__=='__main__':
    app.run(debug=True)
