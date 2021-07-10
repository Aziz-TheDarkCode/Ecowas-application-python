#
# import json
# # Make it work for Python 2+3 and with Unicode
# import io
#
#
# from idna import unicode
#
# try:
#     to_unicode = unicode
# except NameError:
#     to_unicode = str
# countries = {
#     221: {
#         "name": "Senegal",
#         "capital": "Dakar",
#         "location": "Africa"
#     },
#     222: {
#         "name": "nigeria",
#         "capital": "Abudja",
#         "location": "Africa"
#
#     }
# }
#
#
#
# # Write JSON file
# with io.open('countries.json', 'w', encoding='utf8') as outfile:
#     str_ = json.dumps(countries,
#                       indent=4, sort_keys=True,
#                       separators=(',', ': '), ensure_ascii=False)
#     outfile.write(to_unicode(str_))
