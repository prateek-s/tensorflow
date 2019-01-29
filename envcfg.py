import os
import json
#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tf-master
#tf-master, tf-ps, tf-worker-1, tf-worker-2,.... 




ips={'master':'172.18.0.2',
     'ps':'172.18.0.3',
     'worker-0':'172.18.0.4',
     'worker-1': '172.18.0.5'}


cluster = {'master': ['{}:8000'.format(ips['master'])],
           'ps': ['{}:8000'.format(ips['ps'])],
           'worker': ['{}:8000'.format(ips['worker-0']),
           '{}:8000'.format(ips['worker-1'])]}

fnames=['master', 'ps', 'worker-0', 'worker-1']
index = 0 
for nodename in fnames:
    nsplits=nodename.split('-')
    ntype=nsplits[0]
    if len(nsplits) > 1:
        index=int(nsplits[1])
        
    tfc = json.dumps(
        {'cluster': cluster,
         'task': {'type': ntype, 'index': index},
         'model_dir': '/pnfs',
         'environment': 'cloud'
        })
    print tfc
    f=open(nodename+'.env', 'w+')
    f.write(tfc)
    f.close()


