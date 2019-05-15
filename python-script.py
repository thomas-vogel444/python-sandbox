import requests
import json


class JenkinsPage:
    def __init__(self, nodeDescription, numExecutors):
        self.nodeDescription = nodeDescription
        self.numExecutors = numExecutors

    def __str__(self):
        return "Description: %s, Number of Executors: %s" %(self.nodeDescription, self.numExecutors)

class JenkinsClient:
    def getJenkinsPage(self):
        response = json.loads(requests.get("https://lab03.build.tax.service.gov.uk/api/json", auth=('thomas.vogel', 'Dfens1987!444')).content)
        return JenkinsPage(response["nodeDescription"], response["numExecutors"])

if __name__ == '__main__':
    jenkinsClient = JenkinsClient()

    print jenkinsClient.getJenkinsPage()