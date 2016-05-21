import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

re_postcode=re.compile(r'(\d{5})')
def audit_postcode(postcode_dic, postcode):
'''creating a dictionary of postcode, the keys are the postcodes and the values are the number of times that they appear'''
    if postcode not in postcode_dic.keys(): 
        postcode_dic[postcode]=1
    else: 
        postcode_dic[postcode]+=1

def is_postcode(elem):
#return whether the tag is a postcode tag
    return (elem.attrib['k'] == "addr:postcode")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    postcode_dic={}
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way" or elem.tag=="node":
            for tag in elem.iter("tag"):
                if is_postcode(tag):
                	if re_postcode.search(tag.attrib['v']):
                		value=re_postcode.search(tag.attrib['v']).group()
                		audit_postcode(postcode_dic, value)
    osm_file.close()
    print postcode_dic

audit("sample.osm")