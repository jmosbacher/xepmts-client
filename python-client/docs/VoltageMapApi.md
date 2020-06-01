# xepmts.VoltageMapApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_voltage_map_item**](VoltageMapApi.md#delete_voltage_map_item) | **DELETE** /VoltageMaps/{voltagemapId} | Deletes a VoltageMap document
[**delete_voltage_maps**](VoltageMapApi.md#delete_voltage_maps) | **DELETE** /VoltageMaps | Deletes all VoltageMaps
[**get_voltage_map_item**](VoltageMapApi.md#get_voltage_map_item) | **GET** /VoltageMaps/{voltagemapId} | Retrieves a VoltageMap document
[**get_voltage_map_item_by_name**](VoltageMapApi.md#get_voltage_map_item_by_name) | **GET** /VoltageMaps/{Name} | Retrieves a VoltageMap document by name
[**get_voltage_maps**](VoltageMapApi.md#get_voltage_maps) | **GET** /VoltageMaps | Retrieves one or more VoltageMaps
[**post_voltage_maps**](VoltageMapApi.md#post_voltage_maps) | **POST** /VoltageMaps | Stores one or more VoltageMaps.
[**put_voltage_map_item**](VoltageMapApi.md#put_voltage_map_item) | **PUT** /VoltageMaps/{voltagemapId} | Replaces a VoltageMap document


# **delete_voltage_map_item**
> delete_voltage_map_item(voltagemap_id, if_match)

Deletes a VoltageMap document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    voltagemap_id = 'voltagemap_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

    try:
        # Deletes a VoltageMap document
        api_instance.delete_voltage_map_item(voltagemap_id, if_match)
    except ApiException as e:
        print("Exception when calling VoltageMapApi->delete_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagemap_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | VoltageMap document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voltage_maps**
> delete_voltage_maps()

Deletes all VoltageMaps

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    
    try:
        # Deletes all VoltageMaps
        api_instance.delete_voltage_maps()
    except ApiException as e:
        print("Exception when calling VoltageMapApi->delete_voltage_maps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voltage_map_item**
> VoltageMap get_voltage_map_item(voltagemap_id)

Retrieves a VoltageMap document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    voltagemap_id = 'voltagemap_id_example' # str | 

    try:
        # Retrieves a VoltageMap document
        api_response = api_instance.get_voltage_map_item(voltagemap_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VoltageMapApi->get_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagemap_id** | **str**|  | 

### Return type

[**VoltageMap**](VoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voltage_map_item_by_name**
> VoltageMap get_voltage_map_item_by_name(name)

Retrieves a VoltageMap document by name

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    name = 'name_example' # str | 

    try:
        # Retrieves a VoltageMap document by name
        api_response = api_instance.get_voltage_map_item_by_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VoltageMapApi->get_voltage_map_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**VoltageMap**](VoltageMap.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VoltageMap document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voltage_maps**
> InlineResponse2007 get_voltage_maps(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more VoltageMaps

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more VoltageMaps
        api_response = api_instance.get_voltage_maps(where=where, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VoltageMapApi->get_voltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of VoltageMaps |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_voltage_maps**
> post_voltage_maps(voltage_map)

Stores one or more VoltageMaps.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    voltage_map = xepmts.VoltageMap() # VoltageMap | A VoltageMap or list of VoltageMap documents

    try:
        # Stores one or more VoltageMaps.
        api_instance.post_voltage_maps(voltage_map)
    except ApiException as e:
        print("Exception when calling VoltageMapApi->post_voltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltage_map** | [**VoltageMap**](VoltageMap.md)| A VoltageMap or list of VoltageMap documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_voltage_map_item**
> put_voltage_map_item(voltagemap_id, if_match, voltage_map)

Replaces a VoltageMap document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.VoltageMapApi(api_client)
    voltagemap_id = 'voltagemap_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field
voltage_map = xepmts.VoltageMap() # VoltageMap | A VoltageMap or list of VoltageMap documents

    try:
        # Replaces a VoltageMap document
        api_instance.put_voltage_map_item(voltagemap_id, if_match, voltage_map)
    except ApiException as e:
        print("Exception when calling VoltageMapApi->put_voltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagemap_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 
 **voltage_map** | [**VoltageMap**](VoltageMap.md)| A VoltageMap or list of VoltageMap documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VoltageMap document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

