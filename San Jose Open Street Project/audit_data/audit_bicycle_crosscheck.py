import xml.etree.cElementTree as ET
import pprint
import codecs
import json


def audit(osmfile):
'''cross check the value of bicycle tags and the cycleway tags, and also mark the tags with element ID'''
    osm_file = open(osmfile, "r")
    cycleway_dic={}
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way":
            tags={}
            for tag in elem.iter("tag"):  
                try: 
                    m=tag.attrib['k']
                    tags[tag.attrib['k']]=tag.attrib['v']
                except KeyError:
                    pass
            if 'bicycle'in tags.keys() and 'cycleway' in tags.keys():
                print tags['bicycle'], tags['cycleway'], elem.attrib['id']
    osm_file.close()

audit("sample.osm")