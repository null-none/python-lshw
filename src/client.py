import json


class ListHardware:

	def get_nic_data(self):
	    lshw_cmd = ['lshw', '-json']
	    proc = subprocess.Popen(lshw_cmd, stdout=subprocess.PIPE,
	                                      stderr=subprocess.PIPE)
	    return proc.communicate()[0]

	def find_class(self, data, class_):
	    for entry in data.get('children', []):
	        if entry.get('class') == class_:
	            yield entry

	        for child in self.find_class(entry, class_):
	            yield child

	def read_data(self, proc_output, class_='network'):
	    for entry in self.find_class(json.loads(proc_output), class_):
	        yield entry['vendor'], entry['description'], entry['product']