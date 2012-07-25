from datetime import datetime, date, time
messageContext.variables['clientIp'] = messageContext.variables['_flow.clientip']
messageContext.variables['requestUri'] = messageContext.variables['_flow.client.request.uriwithqueryparams']

#parse uri query params
uri = str()
uri = messageContext.variables['requestUri']
path = uri.lower().split("?")
queryParams = path[1].split("&")
queryParamsList = []
for param in queryParams:
    queryParamsList.append(param.split("="))
for qParam in queryParamsList:
    if qParam[0] == 'apikey':
        messageContext.variables['apiKey'] = qParam[1]
    if qParam[0] == 'pagenumber':
        messageContext.variables['pageNumber'] = qParam[1]
    if qParam[0] == 'pagesize':
        messageContext.variables['pageSize'] = qParam[1]
    if qParam[0] == 'searchquery':
        messageContext.variables['searchQuery'] = qParam[1]
    if qParam[0] == 'productids':
        messageContext.variables['productIds'] = qParam[1]
    if qParam[0] == 'producttypes':
        messageContext.variables['productTypes'] = qParam[1]
    if qParam[0] == 'searchquery':
        messageContext.variables['searchQuery'] = qParam[1]
    if qParam[0] == 'searchoper':
        messageContext.variables['searchOper'] = qParam[1]
    

messageContext.variables['activityId'] = messageContext.variables['_flow.client.request.header.X-Redbox-ActivityID']
messageContext.variables['dateTime'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
messageContext.variables['sourceURI'] = messageContext.variables['_flow.client.request.uriwithqueryparams']
a = str()
a = messageContext.variables['requestUri']

if (messageContext.variables['productIds'] != "" and messageContext.variables['productIds'] != "None"):
    messageContext.variables['operName'] = "P2"
elif (messageContext.variables['searchQuery'] != "" and messageContext.variables['searchQuery'] != "None"):
    messageContext.variables['operName'] = "P3"
elif (a.upper().find("/METRICS")>0):
    messageContext.variables['operName'] = "P4"
else:
    messageContext.variables['operName'] = "P1"
    
 #reset Nones to blanks
if (messageContext.variables['pageNumber']== "None"):
    messageContext.variables['pageNumber'] = ""
if (messageContext.variables['pageSize']== "None"):
    messageContext.variables['pageSize'] = ""
if (messageContext.variables['productIds'] == "None"):
    messageContext.variables['productIds'] = ""
if (messageContext.variables['productTypes'] == "None"):    
    messageContext.variables['productTypes'] = ""
if (messageContext.variables['searchQuery'] == "None"):    
    messageContext.variables['searchQuery'] = ""
if (messageContext.variables['searchOper'] == "None"):    
    messageContext.variables['searchOper'] = ""    