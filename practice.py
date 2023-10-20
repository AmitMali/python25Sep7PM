emails=[
    "amit@gmail.com",
    "foo@yellow.com",
    "someuser@gmail.com",
    "johndoe@hotmail.com",
    "sumit@yahoo.com",
    "tejas@yahoo.com",
    "rudran@hotmail.com"
]
domains=["www.google.com",
"youtu.be",
"list-manage.com",
"huffpost.com",
"independent.co.uk",
"picasaweb.google.com",
"samsung.com",
"cdc.gov",
"amazon.co.jp",
"soundcloud.com",
"un.org",
"domainmarket.com",
"en.wikipedia.org",
"booking.com",
"reuters.com",
"www.gov.uk",
"ovh.com",
"get.google.com",
"fb.com",
"hugedomains.com",
"estadao.com.br",
"indiatimes.com",
"huffingtonpost.com",
"mozilla.org",
"nature.com"
]

def findEndWithFromList(values,param):
    # values must be and itterable of string type data
    #param must be a string
    result=[]
    for value in values:
        if value.endswith(param):
            result.append(value)

    return result

print(findEndWithFromList(emails,"hotmail.com"))
print(findEndWithFromList(domains,".com"))
