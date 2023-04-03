import streamlit as st 
import pandas as pd
import os
import shutil
import time

# Function do copy and rename files

def copy_rename(source_destination, target_destination, existing_file_name, new_file_name):
        #Reading source file_path and file_name
        src_file = os.path.join(source_destination, existing_file_name)
        #Copying to destination
        shutil.copy(src_file,target_destination)
        #Targeting the file_path and file to rename
        dst_file = os.path.join(target_destination, existing_file_name)
        #Targeting the file_path of copied file and assigning new file name
        new_dst_file_name = os.path.join(target_destination, new_file_name)
        #Renaming
        os.rename(dst_file, new_dst_file_name)

# Streamlit App Messsage
st.write("""
 # VX Renaming & Copying Script
Made by @yildayat
 """
 )

# Streamlit file upload
st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader("Upload spreadsheet", type=["csv", "xlsx"], accept_multiple_files=False)

# Check if the uploaded file is CSV or Excel and read into Pandas accordingly
if uploaded_file:
    # Check MIME type of the uploaded file
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file, index_col=False)
    else:
        df = pd.read_excel(uploaded_file, index_col=False)
    st.dataframe(df)

# If file has been successfully uploaded, start the operation
if uploaded_file is not None:
    if st.button('Start Rename & Copy'):
        # print is visible in the server output, not in the page
        print('button clicked!')
        source_destination = df['source_destination'].to_list()
        target_destination = df['target_destination'].to_list()
        existing_file_name = df['existing_file_name'].to_list()
        new_file_name = df['new_file_name'].to_list()

        for i in range(len(existing_file_name)):
            copy_rename(source_destination[i], target_destination[i], existing_file_name[i], new_file_name[i])
        
        st.success('Operation Completed!')





