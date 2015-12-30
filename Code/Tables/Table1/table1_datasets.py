from PyTablePrinter.tableprinter import TablePrinter
import glob
import json

"""
This is what we're generating:

Modality | Species | Dataset | Token | XYZT Resolution | Total Size | Reference |
"""

cache_path = "../../../Data/metadata/projinfo_cache"
public_token_files = glob.glob('{}/*.json'.format(cache_path))

# Trim the path from the left and .json from the right:
public_tokens = [i[len(cache_path)+1:-5] for i in public_token_files]
# print public_tokens

token_info = []

for path in public_token_files:
    with open(path, 'r') as infile:
        token_info.append(json.loads(infile.read()))

pt = TablePrinter(token_info)
print pt.to_markdown()


#
# tokens = oo.get_public_tokens()
#
# data = []
#
# for t in tokens:
#     info = oo.get_token_info(t)
#     metadata = ndl.get_metadata(t)
#     if 'reference' in metadata:
#         link = metadata['reference']
#         link = "[{}]({})".format(link[11:40] + "...", link)
#     else:
#         link = ""
#     data.append({
#         "token": t,
#         "modality": metadata['type'] if 'type' in metadata else "",
#         "species": metadata['species'] if 'species' in metadata else "",
#         "dataset": info['dataset']['description'],
#         "resolution": metadata['resolution'] if 'resolution' in metadata else "",
#         "image_size": ' x '.join([str(d) for d in info['dataset']['imagesize']['0']]),
#         "reference": link
#     })
#
# col_order = [
#     "token",
#     "modality",
#     "species",
#     "dataset",
#     "resolution",
#     "image_size",
#     "reference"
# ]
#
# tp = PyTablePrinter.TablePrinter(data, col_order=col_order)
# print tp.to_markdown()