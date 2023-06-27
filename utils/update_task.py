import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def update_task(summary, description, myid):
    task_data = {
        "summary": summary,
        "description" : description,
        "is_done" :0,
        "archived":0
    }

    url = "%s/%s" % (BASE_URL, myid) 

    response = requests.put(url,json=task_data)
    if response.status_code==204:
        print("Update was successful")
    else:
        print("Update failed")


if __name__ == "__main__":
    print("Update a task by filling out the prompts below:")
    summary = input("Summary: ")
    description = input("Description: ")
    myid= input("id")
    update_task(summary, description, myid)