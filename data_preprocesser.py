
# coding: utf-8

# ### Todo
# * Extract body text - <strong>[DONE]</strong>
# * Extract article id - <strong>[DONE]</strong>
# * Write body text to file with article id - <strong>[DONE]</strong>
# * Create txt file for each word in body text  - <strong>[DONE]</strong>
# * Store all word information in the file  - <strong>[DONE]</strong>
# 
# Example of lookup dic <br>
# Filename: cat.txt <br>
# Format:

# In[ ]:


{
    "article_id" : [
                        { 
                            "start_pos" : 0,
                            "end_pos" : 2
                        },
                        {
                            "start_pos" : 5,
                            "end_pos" : 7
                        }
                       ],
    "article_id" : [
                        { 
                            "start_pos" : 0,
                            "end_pos" : 2
                        },
                        {
                            "start_pos" : 5,
                            "end_pos" : 7
                        }
                       ]
}


# In[ ]:


[12312, 123124, 123123, 123123]


# In[1]:


import xml.etree.ElementTree as ET
import os
XML_NAMESPACE = '{http://www.mediawiki.org/xml/export-0.10/}'
# this filter could be too harsh
BLACK_LISTED_CHARS = ['/', '|', '=', ']]', '[[', '_', 'أعلام', '}}', '{{']


# In[2]:


def get_xml_content(document):
    """
    Reads in an xml file.
    Returns a tuple containing the article title and the body text
    """
    document = ET.parse(document)
    root = document.getroot()
    
    page = root.find(XML_NAMESPACE + 'page')
    revision = page.find(XML_NAMESPACE + 'revision')
    article_id = page.find(XML_NAMESPACE + 'id')
    text = revision.find(XML_NAMESPACE + 'text')

    return (article_id.text, text.text)


# In[8]:


def clean_up_body_text(text):
    """
    Convert linebreaks to whitespaces 
    Delete continuous whitespaces
    Convert upper case to lower case
    """
    clean_text = text.lower()
    clean_text = ' '.join(clean_text.split())

    return clean_text


# In[13]:


def create_article_file(filename, text):
    """
    Creates a pretty formatted file with name of the article id,
    containing the article body text.
    If the file does not exists it creates the file.
    """
    if not os.path.exists('articles/'):
        os.mkdir('articles/')
    
    file = open('articles/' + filename + '.txt', 'a')
    file.write(text)
    file.close()


# In[14]:


def write_text_xml_content_to_file(file):
    """
    Takes an xml document as argument and writes the text content of the document to a file.
    It cleans up the text aswell.
    """
    (article_id, body_text) = get_xml_content(file)
    clean_text = clean_up_body_text(body_text)
    create_article_file(article_id, clean_text)


# In[15]:


def create_formatted_file_for_each_word(file):
    """
    Creates a formatted file for each word in the given article.
    The files are stored in the folder /word_files
    """
    with open(file, 'r') as article:
        body_text = article.read()
        
    splitted_body_text = body_text.split()
    uniq_words_in_body_text = set(splitted_body_text)
    
    # gets the article id from the filename
    article_id = file.split('.')[0]
    
    if not os.path.exists('word_files/'):
        os.mkdir('word_files/')
    
    legal_word = True

    for word in uniq_words_in_body_text:
        # check if word contains a black listed char
        for char in BLACK_LISTED_CHARS:
            if char in word:
                legal_word = False

        if legal_word:
            with open('word_files/' + word + '.txt', 'a') as file:
                file.write(article_id + '\n')
        legal_word = True


# The files below are just some extra handmade test files.

# In[ ]:


create_formatted_file_for_each_word('15.txt')


# In[ ]:


create_formatted_file_for_each_word('89.txt')


# In[ ]:


create_formatted_file_for_each_word('12.txt')


# In[16]:


#write_text_xml_content_to_file('test_xml/Wikipedia-20170926135213.xml')


# In[ ]:




