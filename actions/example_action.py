import requests
from st2common.runners.base_action import Action

class ExampleAction(Action):
    def __init__(self, config) -> None:
        super(ExampleAction, self).__init__(config=config)

    def run(self):
        p = requests.post("https://awsbill.free.beeceptor.com/post",{"data":"completed"})
        self.logger.info("Successfully req to awsbill")

