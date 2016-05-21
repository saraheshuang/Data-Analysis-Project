import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json


def audit_amenity(amenity_dic, amenity):
'''creating a dictionary of amenities, the keys are amenity names and the values are the number of times that they appear'''
    if amenity not in amenity_dic.keys(): 
        amenity_dic[amenity]=1
    else: 
        amenity_dic[amenity]+=1

def is_amenity(elem):
    return (elem.attrib['k'] == "highway")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    amenity_dic={}
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_amenity(tag):
                    audit_amenity(amenity_dic, tag.attrib['v'])
    osm_file.close()
    print amenity_dic

audit("sample.osm")