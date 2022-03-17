## 100's - Informational Responses
### 100 Continue
*An interim response and client should continue with request*

### 101 Switching Protocols
*Indicates to client / browser the server is switching protocols*

### 102 Processing
*Server is processing the request*

### 103 Checkpoint
*Resume aborted PUT or GET requests*

### 122 Request - URI Too Long
*The URI is too long and exceeds the maximum 2083 characters*

## 200's - Successful Responses
### 200 OK
*Server successfully processed request*

### 201 Created
*Request was successful and server created new resource*

### 202 Accepted
*Request accepted but not processed yet*

### 203 Non-Authoritative Information
*Request processed successfully but information returned may be from another source*

### 204 No Content
*Request completed but no content was returned*

### 205 Reset Content
*Request completed but no content was returned; requires requestor reset document view*

### 206 Partial Content
*Server delivered a partial GET request*

### 207 Multiple Status
*Successful response for WebDAV*

### 208 Already Reported
*Results previously returned and not inlcuded again*

### 210 Content Different
*Content and/or property mismatch between client and server*

### 226 IM Used
*Server has fulfilled the request and response is an instance manipulated result*

## 300's - Redirection Responses
### 300 Multiple Choices
*Server has multiple actions available based on the request; user can select from list*

### 301 Moved Permanently
*Requested page has been permanently moved to a different URL*

### 302 Moved Temporarily / Found
*Requested page has been temporarily moved to a different URL; requestor should continue to use original URL*

### 303 See Other
*The requested page can be located at a different URL; user is not automatically forwarded*

### 304 Not Modified
*Page has not been modified sonce last request*

### 305 Use Proxy
*Requestor must use a proxy to access the requested page*

### 306 Switch Proxy
*No longer used*

### 307 Temporary Redirect
*Requested page has been temporarily moved to a different URL; requestor should continue to use original URL*

### 308 Resume Incomplete
*Used in resumable requests proposal to resume aborted POST and PUT requests*

## 400's - Client Error Responses
### 400 Bad Request
*Request cannot be fulfilled due to incorrect syntax*

### 401 Unauthorized
*Authentication is required or has not been provided*

### 402 Payment Required
*Not currently used. Intended for use in digital cash transactions*

### 403 Forbidden
*Client does not have suffcient permissions to access the requested resource*

### 404 Not Found
*Requested page cannot be found at current location but could be available in the future*

### 405 Method Not Allowed
*Request was made using a method not supported by page*

### 406 Not Acceptable
*Server can provide only content that is unacceptable to the client*

### 407 Proxy Authentication Required
*Client must authenticate with a proxy to access resource*

### 408 Request Timeout
*Server timed out waiting for request from client*

### 409 Conflict
*Request could not be processed due to a conflict*

### 410 Gone
*The requested page is no longer available and will not be available again*

### 411 Length Required
*Server has denied request due to unspecified length of content*

### 412 Precondition Failed
*Resource does not meet conditions of client's request*

### 413 Request Entity Too Large
*Request is too large to fulfill*

### 414 Request URI Too Long
*Requested URL is too long for the server to process*

### 415 Unsupported Media Type
*Server does not media type requested*

### 416 Requested Range Not Satisfiable
*Client requested portion of file but server cannot satisfy the request*

### 417 Expectation Failed
*Server cannot meet requirements of Expect request header field*

### 418 I'm A Teapot
*An IETF April Fools' joke*

### 420 Enhance Your Calm
*Client rate limiting by Twitter*

### 422 Unprocessable Entity
*Unable to process request due to semantic errors*

### 423 Locked
*Requested resource is locked*

### 424 Method Failure
*Request failed due to failure of a previous request (e.g. a PROPPATCH)*

### 426 Upgrade Required
*Client should switch to a different protocol*

### 428 Precondition Required
*Server requires request to be conditional to prevent conflicts*

### 429 Too Many Requests
*User has sent too many requests in a specified time period*

### 431 Request Header Fields Too Large
*Request cannot be processed due to individual field or collective fields are too large*

### 444 No Response
*Indicates Nginx server has not returned requested information and has closed connection*

### 449 Retry With
*Request should be performed after the specified action*

### 450 Blocked By Windows Parental Controls
*Page blocked by Windows Parental Controls*

### 451 Redirect
*Either more efficient server available or server can't access user's mailbox*

### 499 Client Closed Request
*Indicates client has closed connection prior to server completing request*

## 500's - Server Error Responses
### 500 Internal Server Error
*Server encountered an unexpected condition that prevented request fulfillment.*

### 501 Not Implemented
*Request is unrecognizable or server lacks ability to fulfill it*

### 502 Bad Gateway
*Server received an invalid response from an upstream server and could not fulfill request*

### 503 Service Unavailable
*Server is currently unavailable*

### 504 Gateway Timeout
*Server did not receive a timely response from upstream server*

### 505 HTTP Version Not Supported
*Server does not support the HTTP protocol used in request*

### 506 Variant Also Negotiates
*Content negotiation results in circular reference*

### 507 Insufficient Storage
*Insufficient storage*

### 508 Loop Detected
*Server detected an infinite loop while processing request*

### 509 Bandwidth Limit Exceeded
*Apache extension not defined in RFC's to communicate bandwidth allocation exceeded*

### 510 Not Extended
*Further extensions to the request are required to fulfill it*

### 511 Network Authentication Required
*Client is required to authenticate to gain network access*

### 598 Network Read Timeout Error
*Client behind proxy experiences network read timeout error*

### 599 Network Connect Timeout Error
*Client behind proxy experiences network connect timeout error*
