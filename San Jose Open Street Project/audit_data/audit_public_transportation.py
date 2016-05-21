import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json


def audit_pt(pt_dic, pt):
'''creating a dictionary of public transportation, the keys are the type of public transit and the values are the number of times that they appear'''
    if pt not in pt_dic.keys(): 
        pt_dic[pt]=1
    else: 
        pt_dic[pt]+=1

def is_pt(elem):
    return (elem.attrib['k'] == "public_transport")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    pt_dic={}
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_pt(tag):
                    audit_pt(pt_dic, tag.attrib['v'])
    osm_file.close()
    print pt_dic

audit("sample.osm")