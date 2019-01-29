import os
import json
#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tf-master
#tf-master, tf-ps, tf-worker-1, tf-worker-2,.... 


dockerip=172.17.0.2

ips={'master':172.17.0.2,
     'ps':172.17.0.3,
     'worker-1':172.17.0.4}


cluster = {'master': ['{}:8000'.format(ips['master'])],
           'ps': ['{}:8000'.format(ips['ps'])],
           'worker': ['{}:8000'.format(ips['worker-1'])]}

fnames=['master', 'ps', 'worker']

for ntype in fnames:
    
    tfc = json.dumps(
        {'cluster': cluster,
         'task': {'type': ntype, 'index': 0},
         'model_dir': '/pnfs',
         'environment': 'cloud'
        })
    print tfc
    #f=open(ntype+'.env', 'w+')
    #f.write(tfc)
    #f.close()


