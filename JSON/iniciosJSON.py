import json

cítricos=["limon","naranja","pomelo","lima"]

cítricosJSON=json.dumps(cítricos)

print("JSON de cítricos: ",cítricosJSON)

listacítricos=json.loads(cítricosJSON)

print(listacítricos)