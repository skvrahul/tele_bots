import time
import threading
import requests
class DLThread(threading.Thread):
	def run(self):
		print('Download started!!')
		link = self.url
		file_name = link.split('/')[-1]
		self.filename =file_name
		with open(file_name, "wb") as f:
			print("Downloading %s" % file_name)
			response = requests.get(link, stream=True)
			#Checking the file header for size or 'content-length'
			total_length = response.headers.get('content-length')
			if total_length is None:
				f.write(response.content)
			else:
				dl = 0
				total_length = int(total_length)
				for data in response.iter_content(chunk_size=4096):
					dl += len(data)
					f.write(data)
					#Calculating percentage of file that is done downloading 
					self.progress = int(100 * dl / total_length)
		self.done = True
	def __init__(self, url):
		threading.Thread.__init__(self)
		self.url = url
		self.progress = 0
		self.done = False
		self.filename = ''

if __name__ == '__main__':
	t1 = DLThread('https://upload.wikimedia.org/wikipedia/commons/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg')
	t1.start()
	while(1):
		print(t1.progress)
		time.sleep(1)