from connectors.JenkinsClient import JenkinsClient

if __name__ == '__main__':
    jenkinsClient = JenkinsClient()

    print jenkinsClient.getJenkinsPage()