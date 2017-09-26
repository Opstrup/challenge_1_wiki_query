
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET
XML_NAMESPACE = '{http://www.mediawiki.org/xml/export-0.10/}'
WIKI_TXT_FILE = 'wiki_txt_file.txt'


# In[2]:


def get_text_in_xml_document(document):
    """
    Reads in an xml file, finds the text element in the document.
    Returns the string of the text element
    """
    document = ET.parse(document)
    root = document.getroot()
    
    page = root.find(XML_NAMESPACE + 'page')
    revision = page.find(XML_NAMESPACE + 'revision')
    text = revision.find(XML_NAMESPACE + 'text')

    return text.text


# In[3]:


def clean_up_text(text):
    """
    Convert linebreaks to whitespaces 
    Delete continuous whitespaces
    Convert upper case to lower case
    """
    clean_text = text.lower()
    clean_text = ' '.join(clean_text.split())

    return clean_text


# In[18]:


def write_to_file(text):
    """
    Opens the text file and writes the text content from the xml document as new line.
    If the file does not exists it creates the file.
    """
    file = open(WIKI_TXT_FILE, 'a')
    file.write(text +'\n')
    file.close()


# In[20]:


def write_text_xml_content_to_file(file):
    """
    Takes an xml document as argument and writes the text content of the document to a file.
    It cleans up the text aswell.
    """
    text = get_text_in_xml_document(file)
    clean_text = clean_up_text(text)
    write_to_file(clean_text)

