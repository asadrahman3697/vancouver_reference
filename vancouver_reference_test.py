#! python
import unittest
import json
from vancouver_reference import VancouverReference

class VancouverReferenceTest(unittest.TestCase):
    
    
    def setUp(self):
        test_filename = 'isbn.example.json' 
        with open(test_filename) as f:
            json_data = json.load(f)
        
        self.reference_data = VancouverReference(json_data)
        self.reference_data.extract_data()

    def test_extract_data(self):
        self.reference_data.extract_data()
        
        title = self.reference_data.title
        self.assertEqual(title, 'Learning Python')

        year = self.reference_data.year
        self.assertEqual(year, '2003')
        
        publisher = self.reference_data.publisher
        self.assertEqual(publisher, 'O\'Reilly')
        
        title = self.reference_data.title
        self.assertEqual(title, 'Learning Python')
        
        year = self.reference_data.year
        self.assertEqual(year, '2003')
        
        city = self.reference_data.city
        self.assertEqual(city, 'Sebastopol, CA')
        
        author = self.reference_data.author
        self.assertEqual(author, 'by Mark Lutz and David Ascher.')
        
    def test_process_author(self):
        author_string = self.reference_data.process_author()
        self.assertEqual(author_string, 'Mark Lutz, David Ascher.')
        
    def test_multi_process_author(self):
        self.reference_data.author = 'by Mark Lutz, Mark Lutz, Mark Lutz ' + \
        'and David Ascher.'
        author_string = self.reference_data.process_author()
        self.assertEqual(author_string, 'Mark Lutz, Mark Lutz, Mark Lutz, ' + \
        'David Ascher.')
        
        self.reference_data.author = 'by Mark Lutz, Mark Lutz, Mark Lutz' + \
            ', Mark Lutz, Mark Lutz, Mark Lutz, Mark Lutz and David Ascher.'
        author_string = self.reference_data.process_author()
        self.assertEqual(author_string, 'Mark Lutz, Mark Lutz, Mark Lutz, ' + \
            'Mark Lutz, Mark Lutz, Mark Lutz et al.')
            
    def test_reference_data(self):
        self.assertEqual(self.reference_data.get_reference_data(),
            'Mark Lutz, David Ascher. Learning Python. ' + \
            'Sebastopol, CA: O\'Reilly; 2003.')
        
if __name__ == '__main__':
    unittest.main()
