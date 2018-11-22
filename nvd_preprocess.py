#!/usr/bin/python3.6

import csv
import json

def enum_json_object(key,base,value):
  print("{}:".format(key))
  for count in range(len(base)):
    print("\t{}".format(base[count][value]))
   
nvd_file = r'./jnvd.json'
with open(nvd_file) as nvd_json:
  nvd = json.load(nvd_json)
  for item in nvd["CVE_Items"]:
    if item["cve"]["affects"]["vendor"]["vendor_data"]:
      print("CVE ID: {}\n".format(item["cve"]["CVE_data_meta"]["ID"]))
      enum_json_object("Affects",item["cve"]["affects"]["vendor"]["vendor_data"],"vendor_name") 
      enum_json_object("Problem",item["cve"]["problemtype"]["problemtype_data"],"value")
      enum_json_object("References",item["cve"]["references"]["reference_data"],"url")
    print("="*30)

