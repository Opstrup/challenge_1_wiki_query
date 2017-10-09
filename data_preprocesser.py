
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

# In[1]:


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


# In[2]:


[12312, 123124, 123123, 123123]


# In[3]:


import xml.etree.ElementTree as ET
import os
XML_NAMESPACE = '{http://www.mediawiki.org/xml/export-0.10/}'


# In[4]:


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


# In[5]:


def clean_up_body_text(text):
    """
    Convert linebreaks to whitespaces 
    Delete continuous whitespaces
    Convert upper case to lower case
    """
    clean_text = text.lower()
    clean_text = ' '.join(clean_text.split())

    return clean_text


# In[6]:


def create_article_file(filename, text):
    """
    Creates a pretty formatted file with name of the article id,
    containing the article body text.
    If the file does not exists it creates the file.
    """
    file = open(filename, 'a')
    file.write(text)
    file.close()


# In[7]:


def write_text_xml_content_to_file(file):
    """
    Takes an xml document as argument and writes the text content of the document to a file.
    It cleans up the text aswell.
    """
    (article_id, body_text) = get_xml_content(file)
    clean_body_text = clean_body_text(body_text)
    create_article_file(article_id, clean_body_text)


# In[12]:


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
    
    for word in uniq_words_in_body_text:
        with open('word_files/' + word + '.txt', 'a') as file:
            file.write(article_id + '\n')


# In[13]:


create_formatted_file_for_each_word('12345.txt')


# In[14]:


create_formatted_file_for_each_word('89.txt')


# In[15]:


create_formatted_file_for_each_word('12.txt')


# In[ ]:




