from __future__ import print_function
import boto
conn = boto.connect_emr()
if conn.region.name != "us-east-1":
   msg = "Error: Connected to wrong region {}".format(conn.region.name)
   msg += "\n    Connect to us-east-1 instead"
   raise Exception(msg)

jobflows = conn.describe_jobflows(states=["WAITING", "RUNNING", "STARTING"])
for job in sorted(jobflows, key=lambda u: u.state):
   queue = [step
        for step in job.steps if step.state in {"PENDING", "RUNNING"}]
   print(job.jobflowid, job.state, len(queue), sep="\t") 
