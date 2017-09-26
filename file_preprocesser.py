
# coding: utf-8

# In[39]:


from data_preprocesser import write_text_xml_content_to_file
import glob
XML_FOLDER = 'test_xml'


# In[56]:


def get_xml_documents_filepaths(folder):
    files = glob.glob(folder + '/*.xml')
    return files


# In[59]:


def process_all_xml_files_in_folder(folder=XML_FOLDER):
    xml_files = get_xml_documents_filepaths(folder)
    for xml_file in xml_files:
        write_text_xml_content_to_file(xml_file)


# In[61]:


if __name__ == "__main__":
    import sys
    process_all_xml_files_in_folder(sys.argv[1])


# In[ ]:




