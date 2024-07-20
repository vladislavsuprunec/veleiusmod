from bs4 import BeautifulSoup

# Example HTML content
html_doc = """
<html>
<head><title>Example</title></head>
<body>
<a href="http://example.com">Example</a>
<a href="http://example.org">Another Example</a>
</body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Loop through all <a> tags and print their href attribute
for a in soup.find_all('a'):
    print(a['href'])  # Accessing the 'href' attribute of each <a> tag
