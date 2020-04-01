import spacy


def process(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    output = {
        "sentence": sentence,
        "entities": [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents],
        "noun_chunks": [
            (chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
            for chunk in doc.noun_chunks
        ],
        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]
    }

    return output
