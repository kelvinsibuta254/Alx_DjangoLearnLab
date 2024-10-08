# Advanced Security Features

##  Configure Django for HTTPS Support

###     step 1: SECURE_SSL_REDIRECT

####        Set to True to redirect all HTTP requests to HTTPS.

###     step 2: SECURE_HSTS_SECONDS

####        Set an appropriate value (e.g., 31536000 for one year) to instruct browsers to only access the site via HTTPS for the specified time.

###     step 3: SECURE_HSTS_INCLUDE_SUBDOMAINS and SECURE_HSTS_PRELOAD

####        Set to True to include all subdomains in the HSTS policy and to allow preloading.

## Enforce Secure Cookies

###     step 4: SESSION_COOKIE_SECURE

####        Set to True to ensure session cookies are only transmitted over HTTPS.

###     step 5: CSRF_COOKIE_SECURE

####        Set to True to ensure CSRF cookies are only transmitted over HTTPS.

## Implement Secure Headers

### step 6: X_FRAME_OPTIONS

#### Set to “DENY” to prevent your site from being framed and protect against clickjacking.

### step 7: SECURE_CONTENT_TYPE_NOSNIFF

#### Set to True to prevent browsers from MIME-sniffing a response away from the declared content-type.

### step 8: SECURE_BROWSER_XSS_FILTER

#### Set to True to enable the browser’s XSS filtering and help prevent cross-site scripting attacks.


