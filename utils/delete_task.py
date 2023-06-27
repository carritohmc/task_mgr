import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def delete_task(id):
    task_data = {
        "id": id
    }

    url = "%s/%s" % (BASE_URL, myid) 

    response = requests.delete(url,json=task_data)
    if response.status_code==204:
        print("successfully Deleted task")
    else:
        print("Deletion failed")


if __name__ == "__main__":
    print("Enter the id for the task you want to delete:")
    myid = input("id: ")
    delete_task(myid)