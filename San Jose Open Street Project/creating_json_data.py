import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from collections import defaultdict
"""
Your task is to wrangle the data and transform the shape of the data
into the json data looking like:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"highway":{
        "type":"secondary",
        "name":"Lawrence Expressway",
        "name_type":"Expressway",
        "county":"Santa Clara",
        "zip_left":"94087",
        "name_direction_prefix":"S"
}
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}

"""

file_in="sample.osm"

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
re_postcode=re.compile(r'(\d{5})')
re_tiger=re.compile(r'^tiger:',re.IGNORECASE)
#Clean the name
street_list = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Circle", "Trail", "Way", "Terrace", "Expressway", "Parkway", "Commons","Highway","Walk"]

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

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in street_list:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k']=="addr:street")


def audit(file_in):
    osm_file = open(file_in, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

st_types = audit(file_in)

def update_name(name, mapping):
    st_types = audit(file_in)
    for i in mapping.keys():
        if name in st_types[i]:
            name=name.replace(i,mapping[i])
    return name

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        created_dic={}
        address={}
        street={}
        cycleway={}
        ref=[]
        node['id']=element.attrib['id']
        node['type']=element.tag
        #add visible to the element
        try:
            node['visible']=element.attrib['visible']
        except KeyError:
            pass
        #add location to the element
        try: 
            node['pos']=[float(element.attrib['lat']),float(element.attrib['lon'])]
        except KeyError:
            pass
        #add attributes in Created to the dictionary created
        for i in CREATED:
            try:
                created_dic[i]=element.attrib[i]
            except KeyError:
                pass
        node['created']=created_dic
        #add the information of tag under element to the node dictionary 
        for tag in element:          
            try:
                m=tag.attrib['k']
                #clean the data of street name    
                if is_street_name(tag):
                    for i in mapping.keys():
                        if tag.attrib['v'] in st_types[i]:
                            tag.set("v", update_name(tag.attrib['v'], mapping))
                #remove the tag of cycleway if the value is "no"
                elif tag.attrib["k"]=='cycleway' and tag.attrib['v']=='no':        
                    element.remove(tag)
                #adding tag information to node dictionary
                elif m=='amenity':
                    node['amenity']=tag.attrib['v']
                elif m=='name':
                    node['name']=tag.attrib['v']
                elif m=="cuisine":
                    node['cuisine']=tag.attrib['v']
                elif m=="phone":
                    node['phone']=tag.attrib['v']
                elif contain_tiger(tag.attrib["k"]):
                    tag.set("k", tag.attrib["k"][6:])
                    street[tag.attrib["k"]]=tag.attrib["v"]
                if 'addr' in m:
                    add_item=m.split(':')
                    if len(add_item)==2:
                        if add_item[1]=='postcode':
                            #use the five digits of the postcode for analysis
                            if re_postcode.search(tag.attrib['v']):
                                address[add_item[1]]=re_postcode.search(tag.attrib['v']).group()
                        else:
                        	address[add_item[1]]=tag.attrib['v']
                    node['address']=address
                #adding highway value (by creating a dictionary) to the node dictionary
                if m=='highway':
                    street['street_type']=tag.attrib['v']
                elif m=="lanes":
                    street['lanes']=tag.attrib['v']
                elif m=='sidewalk':
                    street['sidewalk']=tag.attrib['v']
                elif m=="maxspeed":
                    street['maxspeed']=tag.attrib['v']
                elif m=="oneway":
                    street['oneway']=tag.attrib['v']
                elif m=='cycleway':
                    street['cycleway']=tag.attrib['v']
                #adding street dictionary
                if street!={}:
                    node['street']=street
            except KeyError:
                pass
            try:
                m=tag.attrib['ref']
                ref.append(m)
                node['node_refs']=ref
            except KeyError:
                pass
        return node
    else:
        return None

def process_map(file_in, pretty = False):
    #use the script in the example
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

process_map(file_in)