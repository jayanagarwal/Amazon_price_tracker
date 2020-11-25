(I have used Pycharm as my IDE)

Steps:
1. Delete the folder named amazon.
2. Install virtual environment and create virtual environment.  (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the required Libraries using requirements file.
	i) Once you have activated your environment use the command - pip install -r requirements.txt
4. To verify: pip freeze
	You should be able to see the libraries needed. (You can compare with the requirements document)
5. Inside scraper.py you need to make a few changes:
	i) 
5. Run scraper.py
	i) python scraper.py
	ii) It will ask you for a url so please input a url.
	-> If you enter a wrond url it will return None to you.
	else it will return something like:
	(Please Check the image attached.)
	
The End!

Modifications:
1. We can modify it according to any other ecommerce website.
	Just Read through the comments in the scraper.py and you can then inspect any other website where you would like to extract the data.
2. We can store the data in csv format or any other suitable format to get a dataset of price history.
3. We can create alerts for price drop using other API(I willtry to do this in the future)
4. Visualise the data to make it more easy to understand (plot a graph which shows lowest price, max price and avg price)
