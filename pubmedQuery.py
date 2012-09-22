#!/usr/bin/python
#! -*- coding: utf-8 -*-

from __future__ import division
import urllib, urllib2
import xml.etree.ElementTree as ET
import datetime
import itertools
from collections import defaultdict
import operator

now = datetime.datetime.now()
year = now.year
eUtilsURL = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

def eSearch(term, mindate=year-2, maxdate=year, retmax=10000000):
  """
  search the keyword on pubmed using eUtils, and return the pubmed IDs
  Note: the date range is from now to the last two years
  """

  #search URL using pubmed eUtils
  eSearchPubmedURL = eUtilsURL  + 'esearch.fcgi?db=pubmed'\
                                + '&mindate=%d&maxdate=%d&retmax=%d&term=%s'%\
                                   (mindate, maxdate, retmax, term)

  data_XML = urllib.urlopen(eSearchPubmedURL).read()

  #parsing XML into an element
  XML = ET.fromstring(data_XML)

  #collect all the pubmed IDs
  ids = [x.text for x in XML.findall("IdList/Id")]

  return ids  

def chunker(seq, size):
  """
  Chunk the the elements of a list
  #! use in case if the list_ids are sooo biggg...
  """
  return (seq[pos: pos+size] for pos in xrange(0, len(seq), size))

def eFetch_author(ids, chunk_size=100):
  """
  fetch the authors and put them into a list
  """

  author_list=[]
  for group in chunker(ids, chunk_size):
    eFetchPubmedURL = eUtilsURL + 'efetch.fcgi?&db=pubmed&retmode=xml&id=%s' % (','.join(group))
    data_XML = urllib.urlopen(eFetchPubmedURL).read()
    XML = ET.fromstring(data_XML)                               
    author_tag = "PubmedArticle/MedlineCitation/Article/AuthorList/Author/" 
    authors_ForeName= [author.text for author in XML.findall(author_tag+"ForeName")]
    authors_LastName = [author.text for author in XML.findall(author_tag+"LastName")]
    # join the ForeName and LastName
    authors = [' '.join(author) for author in zip(authors_ForeName, authors_LastName)]
    author_list.append(authors)

  # combine all the lists into one list
  author_list = list(itertools.chain(*author_list))
  return author_list

def author_score(author_list):
  """
  author_score based on the frequencies 
  """

  #for counting ...
  dictScore = defaultdict(int)
  for author in author_list:
    dictScore[author] +=1
  
  #sort from the higher to the lower frequencies
  sorted_dictScore = sorted(dictScore.iteritems(), key = operator.itemgetter(1), reverse=True)
  total_score = len(sorted_dictScore)

  for author,score in sorted_dictScore:
    print '%s\'score\t: %.2f'%(author,score/total_score)

  return sorted_dictScore

if __name__ == "__main__":
  "self-test code"
  ids = eSearch("hi-c map")
  author_list = eFetch_author(ids)
  author_score(author_list)
