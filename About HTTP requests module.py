import requests
import datetime
parameters={
    "token":"hjsdhjdshjdsdfhj",
    "username":"pushpakks14",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# print(requests.post("https://pixe.la/v1/users",json=parameters).text)

graph_parameters={
    "id":"graph1",
    "name":"Running",
    "unit":"rounds",
    "type":"int",
    "color":"sora",
}

headers={
    "X-USER-TOKEN":"hjsdhjdshjdsdfhj"
}

# print(requests.post(url="https://pixe.la/v1/users/pushpakks14/graphs",json=graph_parameters,headers=headers).text)
today=datetime.datetime.now()
now=today.date().strftime("%Y%m%d")
rounds=input("How many rounds of bird valley did you run today?")

pixel_parameters={
    "date":now,
    "quantity":rounds,
}

print(requests.post("https://pixe.la/v1/users/pushpakks14/graphs/graph1",json=pixel_parameters,headers=headers).text)
update_pixel_parameters={
    "quantity":"4",
}

# print(requests.put("https://pixe.la/v1/users/pushpakks14/graphs/graph1/20220708",json=update_pixel_parameters,headers=headers).text)
# print(requests.delete("https://pixe.la/v1/users/pushpakks14/graphs/graph1/20220708",headers=headers).text)