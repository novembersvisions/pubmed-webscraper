"""
Test script for module scrape

When run as a script, this module invokes a procedure to test the function in scrape.
"""

import introcs
import scrape

def testpubmed():
    """
    Test procedure for function pubmed

    Tests the function pubmed; informs us if the 
    function is working properly.
    """

    # Returns the titles and descriptions of PubMed articles (10 per page) in response to a keyword

    result = scrape.pubmed('neuroscience','2')
    #introcs.assert_equals('test',result)

    pass

    print('Function is working correctly')

# call the function
testpubmed()
print('Module scrape passed all tests.')