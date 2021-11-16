# Build a streamlit app that uses NER and NLP techniques at the backend and can be helpful to kids
# in understanding the grammar concepts.
import streamlit as st
import spacy
from spacy_streamlit import visualize_parser, visualize_ner
from spacy import displacy
#loads library and corpus, then passes the text through it
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

#Setup the streamlit page to take user inputs
#template = """<div style = "background-color:red; padding:1px;">
#                <h2 style = "color=:white; text-align:center">Grammar app </h2>
#                </div>""" #allows multiple lines of html
#css colour codes available online, basic css
#st.markdown(template,unsafe_allow_html=True) #tells streamlit to run the home written "unsafe" html above
st.title("Grammar app")
st.write("")
st.write("")
st.write("This app will show you the different parts of a sentence")
st.write("")
st.write("")
st.write("*Don't forget to select which type of information you are interested in on the left hand side*")
st.write("")
st.write("")
input_text = st.text_input(label="Please enter your sentence here so you can learn more about it:")
st.sidebar.title("Select what you would like to learn more about")
dropdown = st.sidebar.selectbox("Select one",["","Sentence structure","Named Entity Recognition"])
text_1 = nlp(input_text)
for token in text_1:
    print(token.text,token.lemma_,token.pos_,token.tag_,token.dep_,token.shape_,token.is_alpha)
#will automatically detect just entities
for word in text_1.ents:
    print(word.text, word.label_)
if dropdown == "Sentence structure":
    visualize_parser(text_1, title="Parts of a sentence")
    st.write("(you can scroll across the image from left to right to see more)")
    st.subheader("let's have a look at this sentence in more detail")
    for i in text_1:
        st.write(i.text,"* is classed as *", i.pos_, ",* this means it is a *", spacy.explain(i.pos_))
elif dropdown == "Named Entity Recognition":
    visualize_ner(text_1, labels=nlp.get_pipe("ner").labels, title="Real World Objects", show_table=False)
    st.subheader("so what does all this mean.....?")
    for i in text_1.ents:
        st.write(i.text,"* is labelled as *", i.label_, ",* this means it is classed as being a *", spacy.explain(i.label_))