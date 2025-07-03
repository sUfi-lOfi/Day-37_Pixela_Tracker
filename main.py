import datetime
import os
import requests
from dotenv import load_dotenv
load_dotenv("./variable.env")

now = datetime.datetime.now()
date_today= now.strftime("%Y%m%d")
header = {
    "X-USER-TOKEN" : os.getenv("api_token")
}

#------------------Creating a user-----------------#

# create_user_params = dict(token=os.getenv("api_token"),username="sufilofi1",agreeTermsOfService="yes",notMinor="yes")
# create_user_url = "https://pixe.la/v1/users"
# create_user_request = requests.post(create_user_url,json=create_user_params)
# print(create_user_request.text)

#-------------Creating a graph-------------#

# create_graph_url = "https://pixe.la/v1/users/sufilofi1/graphs"
# create_graph_params = dict(id="graph1,name="graph1",unit="commits",type="int",color="ajisai")
# create_graph_request = requests.post(create_graph_url,json=create_graph_params,headers=header)
# print(create_graph_request.text)

#---------Posting a pixel---------#

# post_pixel_url = "https://pixe.la/v1/users/sufilofi1/graphs/graph1"
# post_pixel_params = dict(date=date_today,quantity="12")
# post_pixel_request = requests.post(post_pixel_url,json=post_pixel_params,headers=header)
# print(post_pixel_request.text)

#-------------Update Pixel-----------#

# update_pixel_url = f"https://pixe.la/v1/users/sufilofi1/graphs/graph1/{date_today}"
# update_pixel_params = dict(quantity="6")
# update_pixel_request= requests.put(update_pixel_url,json=update_pixel_params,headers=header)
# print(update_pixel_request.text)

#----------Delete Pixel--------#

delete_pixel_url = f"https://pixe.la/v1/users/sufilofi1/graphs/graph1/{date_today}"
delete_pixel_request = requests.delete(delete_pixel_url,headers=header)
print(delete_pixel_request.text)

