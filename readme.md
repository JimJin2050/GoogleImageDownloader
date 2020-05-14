1. Download Python installer file and install.
2. Download Chromedriver according to your Chrome version from https://chromedriver.chromium.org/downloads
3. Install python packages by command line: 
        pip install -r requirements.txt
   Please make sure you have already under project directory.
4. Modify the settings in settings.yaml according to your real situation.
   "num_to_download" means how many images you want to download for each keyword, the maximum value is 100.
   "start_index" means the start index of keywords, the minimum value is 1, maximum should be the number of keywords.
   "os" means the type of operating system.
   "excel_file" means the relative path of keywords excel file.
   "headless" means if headless mode should be used. The possible value must be "False" and "True". They are case sensitive.
5. Execute main.py