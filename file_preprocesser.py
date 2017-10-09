
# coding: utf-8

# In[6]:


from data_preprocesser import create_formatted_file_for_each_word, write_text_xml_content_to_file
import glob
XML_FOLDER = 'test_xml'
ARTICEL_FOLDER = 'articles'


# In[7]:


def get_xml_documents_filepaths(folder):
    """
    Takes a filepath as argument.
    Returns a list with all .xml documents within the folder.
    """
    files = glob.glob(folder + '/*.xml')
    return files


# In[8]:


def get_articels_filepaths(folder):
    """
    Takes a filepath as argument.
    Returns a list with all .txt articels within the folder.
    """
    files = glob.glob(folder + '/*.txt')
    return files


# In[10]:


def process_all_xml_files_in_folder(folder=XML_FOLDER, articel_folder=ARTICEL_FOLDER):
    """
    Processes all .xml documents within the given folder.
    Uses the data_preprocesser module as underlying logic.
    """
    xml_files = get_xml_documents_filepaths(folder)
    for xml_file in xml_files:
        write_text_xml_content_to_file(xml_file)
    
    articels = get_articels_filepaths(articel_folder)
    for articel in articels:
        create_formatted_file_for_each_word(articel)


# In[ ]:


if __name__ == "__main__":
    import sys
    process_all_xml_files_in_folder(sys.argv[1], sys.argv[2])

