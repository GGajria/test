uri = str()
uri = "http://50.18.22.174:1779/v3/products/movies/metrics?apiKey=93040871d531b12b5d892d19fec2e0fa&pageNumber=2&pageSize=5&searchQuery=a"
path = uri.lower().split("?")
print path[1]
queryParams = path[1].split("&")
queryParamsList = []
for param in queryParams:
    print param
    queryParamsList.append(param.split("="))
print queryParamsList

for qParam in queryParamsList:
    if qParam[0] == 'apikey':
        print "found apikey and it is " + qParam[1]
    if qParam[0] == 'pagenumber':
        print "found it and it is " + qParam[1]
    if qParam[0] == 'pagesize':
        print "found it and it is " + qParam[1]
    if qParam[0] == 'searchquery':
        print "found it and it is " + qParam[1]
    
         
