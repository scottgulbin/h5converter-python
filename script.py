from pandas import HDFStore
import os


for root, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith(".h5"):
            print(os.path.join(root, file))
            store = HDFStore(os.path.join(root, file))
            print store.keys()
            store['/musicbrainz/songs'].to_csv('outputFileForTable'+file+'.csv')
             
