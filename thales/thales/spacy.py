import spacy


def process(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    output = {
        "sentence": sentence,
        "entities": entities(doc.ents),
        "noun_chunks": noun_chunks(doc.noun_chunks),
        "ad_position": ad_position(doc),
        "proper_names": proper_names(doc),
        "verbs": verbs(doc)
    }

    return output


def entities(entities):
    return [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in entities]


def noun_chunks(noun_chunks):
    return [
        (chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
        for chunk in noun_chunks
    ]


def proper_names(doc):
    return [(token.text, token.lemma_, token.tag_, token.dep_) for token in doc if token.pos_ == "PROPN"]


def ad_position(doc):
    return [(token.text, token.lemma_, token.tag_, token.dep_) for token in doc if token.pos_ == "ADP"]


def verbs(doc):
    return [(token.text, token.lemma_, token.tag_, token.dep_) for token in doc if
            token.pos_ == "VERB" or token.pos_ == "AUX"]