import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

input_osm="sample.osm"
output_file="output.xml"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
re_postcode=re.compile(r'(\d{5})')
re_tiger=re.compile(r'^tiger:',re.IGNORECASE)
#Clean the name
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Circle", "Trail", "Way", "Terrace", "Expressway", "Parkway", "Commons","Highway","Walk"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            'Rd.':"Road",
            'Rd':"Road",
            'Ave':"Avenue",
           'ave': "Avenue",
           'Blvd':'Boulevard',
           'Cir':"Circle",
           "Ct":"Court",
           "Dr":"Drive",
           "Hwy":"Highway",
           "Rd":"Road",
           "St":"Street",
           "street":"Street"       
            }

def contain_tiger(value):
    return re_tiger.match(value)

#returns street type dictionary
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

#audit and return street_types dic
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

#update name of the streets
def update_name(name, mapping):
    st_types = audit(input_osm)
    for i in mapping.keys():
        if name in st_types[i]:
            name=name.replace(i,mapping[i])
    return name


def getelements(filename_or_file):
    context = iter(ET.iterparse(filename_or_file, events=('start', 'end')))
    _, root = next(context) # get root element
    for event, elem in context:
        if event == 'end' and (elem.tag == 'node' or elem.tag=='way'):
            yield elem
            root.clear() # free memory  

            
with open(output_file, 'wb') as file:
    # start root
    file.write(b'<root>')
    st_types = audit(input_osm)
    for elem in getelements(input_osm):
        if elem.tag=="way" or elem.tag=="node":
            for tag in elem.iter("tag"):
                #update the name abbreviation
                if is_street_name(tag):
                    for i in mapping.keys():
                        if tag.attrib['v'] in st_types[i]:
                            tag.set("v", update_name(tag.attrib['v'], mapping))
                #update postcode
                if is_postcode(tag):
                	if re_postcode.search(tag.attrib['v']):
                		tag.set("v",re_postcode.search(tag.attrib['v']).group())
                #remove the cycleway tag if value is no
                if tag.attrib["k"]=='cycleway' and tag.attrib['v']=='no':
                    elem.remove(tag)
                #remove "tiger:" from tiger-related keys
                if contain_tiger(tag.attrib["k"]):
                    tag.set("k", tag.attrib["k"][6:])
        file.write(ET.tostring(elem, encoding='utf-8'))
                
                    # close root
    file.write(b'</root>')




