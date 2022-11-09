import json
from urllib.request import urlopen
import csv

def get_id():
	with urlopen('https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty') as jobs: 
    		jobs_id = json.loads(jobs.read())
	return jobs_id

def get_job(id):
	with urlopen(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty") as job:
		jobs = json.loads(job.read())
		clean_job =[jobs.pop("id",None),jobs.pop("title",None),jobs.pop("url",None)]
	return clean_job
	
def get_all_jobs(jobs_id):
	all_jobs=[]
	for job in jobs_id:
		all_jobs.append(get_job(job))
	return all_jobs

def write_to_csv(file_name,all_jobs):
	with open(file_name, "w+") as file:
		writer = csv.writer(file)
		for row in all_jobs:
			writer.writerow(row)

def main():
	file_name=input("please enter your name")
	if len(file_name) > 4 and file_name.endswith(".csv"):
		ids= get_id()
		data = get_all_jobs(ids)
		write_to_csv(file_name,data)
	else:
		 print("The filename must end in csv") 
	
if __name__=="__main__":
	main()
	
		

