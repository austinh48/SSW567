import unittest
from unittest import mock
import homework04a
import requests
import json


def getRepos(id, repoName):

    gitRepo = requests.get('https://api.github.com/users/'+id+'/repos')
    
    repoInfo = json.loads(gitRepo.text)

    for x in repoInfo:
        gitCommits = requests.get('https://api.github.com/repos/'+id+'/'+x["name"]+'/commits')
        commitInfo = json.loads(gitCommits.text)
        if repoName == x["name"]:
            print('Repo: ' + x["name"] +' Number of commits: '+ str(len(commitInfo)))
        if repoName == 'all':
            print('Repo: ' + x["name"] +' Number of commits: '+ str(len(commitInfo)))

    
class testRepo(unittest.TestCase):

    @mock.patch('homework04a.getRepos')
    def mock_get_repos(mock_get_re):
        # print(mock_get_re)
        # print(homework04a.getRepos)
        mock_get_re.return_value = ['Repo: SSW555 Number of commits: 5', 'Repo: SSW555 Number of commits: 22']
        result = homework04a.getRepos()
        return result

    mock_get_repos()

    def test1(self):
        from homework04a import testRepo
        self.assertEqual(testRepo.mock_get_repos()[0],'Repo: SSW555 Number of commits: 5', 'Should be 5')
    def test2(self):
        from homework04a import testRepo
        self.assertEqual(testRepo.mock_get_repos()[1],'Repo: SSW555 Number of commits: 22', 'Should be 22, maybe 23 once this is submitted')
 
    

if __name__ == '__main__':
    # getRepos('austinh48','all')

    unittest.main(exit = True)