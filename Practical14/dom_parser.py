import xml.dom.minidom as minidom
from datetime import datetime

start_time = datetime.now()

dom_tree = minidom.parse("go_obo.xml")
collection = dom_tree.documentElement

terms = collection.getElementsByTagName("term")

results = {
    "biological_process": ("", 0),
    "molecular_function": ("", 0),
    "cellular_component": ("", 0)
}

for term in terms:
    ns = term.getElementsByTagName("namespace")[0].firstChild.data
    name = term.getElementsByTagName("name")[0].firstChild.data
    is_as = term.getElementsByTagName("is_a")
    count = len(is_as)

    if ns in results and count > results[ns][1]:
        results[ns] = (name, count)

end_time = datetime.now()
dom_duration = end_time - start_time

print("DOM results:")
for k, v in results.items():
    print(f"{k}: {v[0]} ({v[1]} is_a elements)")
print(f"DOM Parsing Time: {dom_duration}\n")


#The DOM parsing time is 14.122451s, and the SAX parsing time is 2.841558s, so the SAX is faster.