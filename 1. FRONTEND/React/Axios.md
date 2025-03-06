AXIOS INTERCEPTORS:

- Create an axios instance - baseURL and headers.
- Headers - contentType and Access-control-allow-origin
- Call that axios instance while making api call. Call get/post etc methods on Axios instance. eg: axiosInstance.get(), axiosInstance.post()
- Call interceptors on axios url.
- Interceptors can be used to display loading spinners till the time we get API response
- Interceptors can be used during authentication to add token to the request.

Axios interceptors - use or eject

1. Request interceptor: Called before making a request to modify a request.
   axiosInstance.interceptors.request.use()
2. Response interceptor: Called after receiving response.
   axiosInstance.interceptors.response.use()

```
// Handle request process
axiosInstance.interceptors.request.use(
request => requestHandler(request)
error => errorHandler(error),
);

// Handle response process
axiosInstance.interceptors.response.use(
response => successHandler(response),
error => errorHandler(error),
);
```

- use() - function takes two functions arguments.

- success handler: function to handle success: argument - config object in request interceptor to modify request OR response object in response interceptor to modify response
- failure handler: function to handle the errors
