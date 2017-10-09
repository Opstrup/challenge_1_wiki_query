
# coding: utf-8

# In[1]:


from data_preprocesser import create_formatted_file_for_each_word, write_text_xml_content_to_file
import glob
XML_FOLDER = 'test_xml'


# In[2]:


def get_xml_documents_filepaths(folder):
    """
    Takes a filepath as argument.
    Returns a list with all .xml documents within the folder.
    """
    files = glob.glob(folder + '/*.xml')
    return files


# In[3]:


def process_all_xml_files_in_folder(folder=XML_FOLDER):
    """
    Processes all .xml documents within the given folder.
    Uses the data_preprocesser module as underlying logic.
    """
    xml_files = get_xml_documents_filepaths(folder)
    for xml_file in xml_files:
        write_text_xml_content_to_file(xml_file)
        create_formatted_file_for_each_word(xml_file)


# In[ ]:


if __name__ == "__main__":
    import sys
    process_all_xml_files_in_folder(sys.argv[1])

