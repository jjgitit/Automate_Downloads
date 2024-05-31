# Automating download files organization
This side project was developed during my internship at Stickney Research to automate few redundant tasks including Auto Tax Form Filler. I just updated few more types of files that I use personally extending the needs from Stickney Research.

# Setup
To run the program, you need python3 installed on your environment. The modules used in this project are:
`os` and `sys` which are included in your Python3 as default modules. These two modules are used to read and track files under target directory which you can customize for your own need. To customize the location of the directory you want to run this automization, simply modify the global variables named,
`src_dir` and for other folders to organize files by types, modify, `pdf_folder`, `image_folder`, `word_folder`, `excel_folder`, `audio_folder`, `video_folder` to desired path on your computer. 


# How to run
First, navigate to the directory where you want to clone the project. After cloning the project, type `python3 clean_download.py`. From now on, if you download a new file to Downloads, the program will automatically generate folders by types and organize files. To stop the program from running, press `control-c` on the terminal the programming is running on. 

