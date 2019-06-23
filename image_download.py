#importing google_images_download module
from google_images_download import google_images_download

#creating an object
image_object = google_images_download.googleimagesdownload()

#search query contains the keyword
search_query = ['iron man']

#download function
#keyword of the image to be downloaded
#format of the image
#limit specifies number of images
#url of the image source
def downloadimages(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 5,
                 "print_urls":True,
                 "size": "medium" 
                 }

    try:
        image_object.download(arguments)

     #handling filenotfound error
    except FileNotFoundError:
            arguments = {"keywords": query, 
			 "format": "jpg", 
			 "limit":4, 
			 "print_urls":True,
                         "size": "medium" 
			 }
            #providing arguments for search query
            #downloading photo based on arguments
            try:
                image_object.download(arguments)
            except:
                pass

#driver code
for query in search_query:
    downloadimages(query)
    print()
