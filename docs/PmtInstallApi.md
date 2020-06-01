# xepmts.PmtInstallApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pmt_install_item**](PmtInstallApi.md#delete_pmt_install_item) | **DELETE** /PmtInstalls/{pmtinstallId} | Deletes a PmtInstall document
[**delete_pmt_installs**](PmtInstallApi.md#delete_pmt_installs) | **DELETE** /PmtInstalls | Deletes all PmtInstalls
[**get_pmt_install_item**](PmtInstallApi.md#get_pmt_install_item) | **GET** /PmtInstalls/{pmtinstallId} | Retrieves a PmtInstall document
[**get_pmt_install_item_by_uid**](PmtInstallApi.md#get_pmt_install_item_by_uid) | **GET** /PmtInstalls/{Uid} | Retrieves a PmtInstall document by uid
[**get_pmt_installs**](PmtInstallApi.md#get_pmt_installs) | **GET** /PmtInstalls | Retrieves one or more PmtInstalls
[**post_pmt_installs**](PmtInstallApi.md#post_pmt_installs) | **POST** /PmtInstalls | Stores one or more PmtInstalls.
[**put_pmt_install_item**](PmtInstallApi.md#put_pmt_install_item) | **PUT** /PmtInstalls/{pmtinstallId} | Replaces a PmtInstall document

# **delete_pmt_install_item**
> delete_pmt_install_item(pmtinstall_id, if_match)

Deletes a PmtInstall document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))
pmtinstall_id = 'pmtinstall_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a PmtInstall document
    api_instance.delete_pmt_install_item(pmtinstall_id, if_match)
except ApiException as e:
    print("Exception when calling PmtInstallApi->delete_pmt_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmtinstall_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pmt_installs**
> delete_pmt_installs()

Deletes all PmtInstalls

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))

try:
    # Deletes all PmtInstalls
    api_instance.delete_pmt_installs()
except ApiException as e:
    print("Exception when calling PmtInstallApi->delete_pmt_installs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pmt_install_item**
> PmtInstall get_pmt_install_item(pmtinstall_id)

Retrieves a PmtInstall document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))
pmtinstall_id = 'pmtinstall_id_example' # str | 

try:
    # Retrieves a PmtInstall document
    api_response = api_instance.get_pmt_install_item(pmtinstall_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtInstallApi->get_pmt_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmtinstall_id** | **str**|  | 

### Return type

[**PmtInstall**](PmtInstall.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pmt_install_item_by_uid**
> PmtInstall get_pmt_install_item_by_uid(uid)

Retrieves a PmtInstall document by uid

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Retrieves a PmtInstall document by uid
    api_response = api_instance.get_pmt_install_item_by_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtInstallApi->get_pmt_install_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**PmtInstall**](PmtInstall.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pmt_installs**
> InlineResponse2004 get_pmt_installs(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more PmtInstalls

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more PmtInstalls
    api_response = api_instance.get_pmt_installs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtInstallApi->get_pmt_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pmt_installs**
> post_pmt_installs(body)

Stores one or more PmtInstalls.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))
body = xepmts.PmtInstall() # PmtInstall | A PmtInstall or list of PmtInstall documents

try:
    # Stores one or more PmtInstalls.
    api_instance.post_pmt_installs(body)
except ApiException as e:
    print("Exception when calling PmtInstallApi->post_pmt_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtInstall**](PmtInstall.md)| A PmtInstall or list of PmtInstall documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pmt_install_item**
> put_pmt_install_item(body, if_match, pmtinstall_id)

Replaces a PmtInstall document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.PmtInstallApi(xepmts.ApiClient(configuration))
body = xepmts.PmtInstall() # PmtInstall | A PmtInstall or list of PmtInstall documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmtinstall_id = 'pmtinstall_id_example' # str | 

try:
    # Replaces a PmtInstall document
    api_instance.put_pmt_install_item(body, if_match, pmtinstall_id)
except ApiException as e:
    print("Exception when calling PmtInstallApi->put_pmt_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtInstall**](PmtInstall.md)| A PmtInstall or list of PmtInstall documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmtinstall_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

