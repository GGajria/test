#query_param_scopes = messageContext.variables['scope']
#kms_scopes = messageContext.variables['scopesList']
query_param_scopes = "PROFILE saml token"
kms_scopes = "PROFILE,CP1 RENTALHISTORY,CP5 authorization_code client_credentials saml token refresh_token"
isScopeValid = 'false'
arr_qp_scopes = query_param_scopes.split(' ')
arr_kms_scopes = kms_scopes.split(' ')

ks_scopeList = []
for ks_scope in arr_kms_scopes:
        eachScope = ks_scope.split(",").pop(0).upper()
        ks_scopeList.append(eachScope)
        
for qp_scope in arr_qp_scopes:
        if qp_scope.upper() in ks_scopeList:
            isScopeValid = 'true'
        else:
            isScopeValid = 'false'
            break 
print   isScopeValid 
    #for kms_scope in arr_kms_scopes:
    #    if kms_scope.upper() == qp_scope.upper():
    #        messageContext.variables['isScopeValid'] = 'true'
    #    else:
    #        messageContext.variables['isScopeValid'] = 'false'
    #        break
