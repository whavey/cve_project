#!/bin/bash

curl -X GET "localhost:9200/nvd_json/_search" -H 'Content-Type: application/json' -d'
{
    "_source": ["NVD.CVE_data_meta.ID","NVD.description.description_data.value"],
    "query" : {
        "match_all": {}
    },
    "size": 100
}
'|jq -r '.hits.hits[]._source.NVD | [.CVE_data_meta.ID,.description.description_data.value] | @sh' | grep -v null | sed "s/'//g" | awk '{f=$1;$1=""; print > f}'
for cve_f in `ls | grep CVE`;do
  sort -u $cve_f | tr " " "\n" > $cve_f"_description"
  rm $cve_f -f
done

