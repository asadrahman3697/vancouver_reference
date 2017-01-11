#! python
import re

""" The module converts json format into a Vancouver reference string as 
    in the sample shown below:
    Lawhead JB, Baker MC. Introduction to veterinary science. \
    Clifton Park (NY): Thomson Delmar Learning; 2005.
    
    More than 6 authors are listed as et al.

"""

class VancouverReference():
    
    def __init__(self,json_data):
        self.json_data = json_data
       
    def extract_data(self):
        for refdata in self.json_data['list']:
            self.author    = refdata['author']
            self.title     = refdata['title']
            self.city      = refdata['city']
            self.year      = refdata['year']
            self.publisher = refdata['publisher']
        
        return None
        
    def process_author(self):
        authorRemoveBy = re.compile(r'^by')
        author_list = authorRemoveBy.sub('', self.author).strip()  
        author_list = author_list.replace('.', '')
        authorRemoveAnd = re.compile(r' and ')  
        author_list = authorRemoveAnd.sub(',', author_list).split(',')
        
        author_string = ''
        author_count = 0
        
        for author in author_list:
            author = author.strip()
            author_count += 1
            
            author_string += author 
            if author_count == 6:
                author_string += ' et al.'
                break
            
            if author != author_list[-1]:
                author_string += ', '
            else:
                author_string += '.'
                break
           
        return author_string
        
        
    def get_reference_data(self):
        self.extract_data()
        reference_data = self.process_author() + ' ' + \
                         self.title + '. ' + self.city + ': ' + \
                         self.publisher + '; ' + self.year + '.'
        
        return reference_data
        

