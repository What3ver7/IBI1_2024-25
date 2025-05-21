import xml.sax
from datetime import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0
        self.results = {
            "biological_process": ("", 0),
            "molecular_function": ("", 0),
            "cellular_component": ("", 0)
        }
        self.inside_term = False

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.inside_term = True
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0

    def characters(self, content):
        if self.current_tag == "name":
            self.name += content.strip()
        elif self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag == "is_a":
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.results and self.is_a_count > self.results[self.namespace][1]:
                self.results[self.namespace] = (self.name, self.is_a_count)
            self.inside_term = False
        self.current_tag = ""

start_time = datetime.now()

parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml")

end_time = datetime.now()
sax_duration = end_time - start_time

print("SAX results:")
for k, v in handler.results.items():
    print(f"{k}: {v[0]} ({v[1]} is_a elements)")
print(f"SAX Parsing Time: {sax_duration}\n")
