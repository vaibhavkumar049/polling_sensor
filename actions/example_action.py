import requests
from st2common.runners.base_action import Action

class ExampleAction(Action):
    def __init__(self, config) -> None:
        super(ExampleAction, self).__init__(config=config)

    def run(self):
        p = requests.post("https://62210679afd560ea69a5358c.mockapi.io/data",{"data":"completed"})
        self.logger.info("Successfully req to awsbill")

