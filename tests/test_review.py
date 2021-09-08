import unittest 
from app.models import Review
 
class ReviewTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the Review class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_review = Review(1234,'Sample review','https://image.tmdb.org/t/p/w500/khsjha27hbs','The movie was awesome!!')
  
  def test_instance(self): 
    self.assertTrue(isinstance(self.new_review,Review))
    
  def test_init(self): 
    '''
    Test to check whether the object is instantiated properly
    '''
    self.assertEqual(self.new_review.movie_id,1234)
    self.assertEqual(self.new_review.title,'Sample review')
    self.assertEqual(self.new_review.imageurl,'https://image.tmdb.org/t/p/w500/khsjha27hbs')
    self.assertEqual(self.new_review.review,'The movie was awesome!!')