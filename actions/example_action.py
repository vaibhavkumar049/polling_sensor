import requests
from st2common.runners.base_action import Action

class ExampleAction(Action):
    def __init__(self, config) -> None:
        super(ExampleAction, self).__init__(config=config)

    def run(self):
        data = {
            "data": "string",
            "status":"pending",
            "rule": "rule3"
        }
        p = requests.post("http://127.0.0.1:5000/order",data)
        self.logger.info("Successfully req to awsbill")

