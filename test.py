import spacy
nlp = spacy.load("en_legal_ner_trf")
text = "Section 319 Cr.P.C. contemplates a situation where the evidence adduced by the prosecution for Respondent No.3-G. Sambiah on 20th June 1984"
doc = nlp(text)

# Print indentified entites
for ent in doc.ents:
     print(ent,ent.label_)
