import xml.etree.cElementTree as ET
import pprint
import codecs
import json


def audit_cycleway(cycleway_dic, name):
'''return a dictionary of cycleway with the names of cycleway types and the value as the number of times this type of cycleway appear'''
    if name not in cycleway_dic.keys(): 
        cycleway_dic[name]=1
    else: 
        cycleway_dic[name]+=1

def is_cycleway(elem):
    return (elem.attrib['k'] == "cycleway")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    cycleway_dic={}
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_cycleway(tag):
                    audit_cycleway(cycleway_dic, tag.attrib['v'])
    osm_file.close()
    print cycleway_dic

audit("sample.osm")