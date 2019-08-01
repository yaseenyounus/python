# Yaseen Younus
# 31 July 2019
# This program generates Apache Rewrite rules based on the source and destination sites provided to the function. It works with internal as well as external redirects.

# RewriteRule ^/source-path$ https://destination-url-for-external-redirect.html [R=301,NC,L]
# RewriteRule ^/source-path$ /destination-path-for-internal-redirect.html [R=301,NC,L]
# Example : Redirect www.abbott.com/news to www.abbott.com/newsroom.html

import sys 

def redirect_to_internal(path_from, path_to):
    print(f'RewriteRule ^{removeRoot(path_from)}$ {removeRoot(path_to)} [R=301,NC,L]')

def redirect_to_external(path_from, path_to):
    print(f'RewriteRule ^{removeRoot(path_from)}$ {path_to} [R=301,NC,L]')

def removeRoot(url):
    if url[:url.find('/') == -1]:
        return '/'
    else:
        return url[url.find('/'):]


url_from, url_to = sys.argv[1], sys.argv[2]

if url_from[:url_from.find('/')] == url_to[:url_to.find('/')]:
    redirect_to_internal(url_from, url_to)
else:
    redirect_to_external(url_from, url_to)
