{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4eae8e75-2e3e-438c-a9e8-d3aa7d6ad446",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am learning NLP.\n",
      "SpaCy is easy to use.\n"
     ]
    }
   ],
   "source": [
    "import spacy\n",
    "nlp = spacy.load(\"en_core_web_sm\")\n",
    "doc = nlp(\"I am learning NLP. SpaCy is easy to use.\"\n",
    "for sent in doc.sents:\n",
    "    print(sent.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "192b29de-6dec-40c5-af2c-2ea1d38587c8",
   "metadata": {},
   "source": [
    "Sentence Tokenization with spaCy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6a6b15e5-5208-46cd-8f86-40a5a4d952a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am learning NLP.\n",
      "I like Python.\n",
      "NLP is interesting.\n"
     ]
    }
   ],
   "source": [
    "nlp = spacy.blank(\"en\")\n",
    "nlp.add_pipe(\"sentencizer\")\n",
    "text = \"I am learning NLP. I like Python. NLP is interesting.\"\n",
    "doc = nlp(text)\n",
    "for sent in doc.sents:\n",
    "    print(sent.text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3689dd1-6db1-4729-9f79-de2352e8f061",
   "metadata": {},
   "source": [
    "Sentence Tokenization with NLTK"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6425c8e7-5a07-427c-9c73-57309a2dd2ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am learning NLP.\n",
      "I like Python.\n",
      "NLP is interesting.\n"
     ]
    }
   ],
   "source": [
    "from nltk.tokenize import sent_tokenize\n",
    "text = \"I am learning NLP. I like Python. NLP is interesting.\"\n",
    "sentences = sent_tokenize(text)\n",
    "for sentence in sentences:\n",
    "    print(sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b31b7e8-1d48-4e4d-9412-0f8c8f23d039",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
