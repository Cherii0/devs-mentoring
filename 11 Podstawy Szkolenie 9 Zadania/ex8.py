
class Case:

    def __init__(self):
        self.__tasks = {
        "first_case" :
            {
                "name": "first_case",
                "created_task": "2021-10-26T19:48:12+00:00",
                "end_task" : None
            },
        "second_case" :
            {
                "name": "‘second_case’",
                "created_task": "2021-09-26T19:48:12+00:00",
                "end_task": "2021-10-26T19:48:12+00:00"
            }
        }

    def retrieve_seconds(self):
        import datetime

        for task, task_values in self.__tasks.items():
            if task_values["created_task"]:
                start_time = datetime.datetime.strptime(task_values["created_task"], "%Y-%m-%dT%H:%M:%S+00:00")
            else:
                print("created_task is missing")
                return
            if task_values["end_task"]:
                end_time = datetime.datetime.strptime(task_values["end_task"], "%Y-%m-%dT%H:%M:%S+00:00")
            else:
                end_time = datetime.datetime.now()

            print(f"{task}, {int((end_time -  start_time).total_seconds())} seconds")

def main():
    case = Case()
    case.retrieve_seconds()

if __name__ == "__main__":
    main()
