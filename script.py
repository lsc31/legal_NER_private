import spacy
from data_preparation import get_text_from_indiankanoon_url
from spacy import displacy
from legal_ner import extract_entities_from_judgment_text

legal_nlp=spacy.load('en_legal_ner_trf')
print("calling url")
judgment_text = get_text_from_indiankanoon_url('https://indiankanoon.org/doc/542271/')

print(judgment_text)
preamble_spiltting_nlp = spacy.load('en_core_web_sm')
run_type='doc' ###  trade off between accuracy and runtime
do_postprocess=True 
combined_doc = extract_entities_from_judgment_text(judgment_text,legal_nlp,preamble_spiltting_nlp,run_type,do_postprocess)


extracted_ent_labels = list(set([i.label_ for i in combined_doc.ents]))
colors = {'COURT': "#bbabf2", 'PETITIONER': "#f570ea", "RESPONDENT": "#cdee81", 'JUDGE': "#fdd8a5",
          "LAWYER": "#f9d380", 'WITNESS': "violet", "STATUTE": "#faea99", "PROVISION": "yellow",
          'CASE_NUMBER': "#fbb1cf", "PRECEDENT": "#fad6d6", 'DATE': "#b1ecf7", 'OTHER_PERSON': "#b0f6a2",
          'ORG':'#a57db5','GPE':'#7fdbd4'}
options = {"ents": extracted_ent_labels, "colors": colors}
displacy.serve(combined_doc, style='ent',port=8080,options=options)
