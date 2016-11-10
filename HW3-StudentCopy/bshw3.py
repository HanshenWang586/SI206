# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
text = soup.prettify()
text = text.replace("student", "AMAZING student");
text = text.repalce('<iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/mimp_3gquc4?feature=oembed" width="560"></iframe>','<img src="HW3-StudentCopy/1.jpg">')
print (text)


