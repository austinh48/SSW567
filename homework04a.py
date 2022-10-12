import unittest
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
    def test1(self):
        self.assertEqual(getRepos('austinh48','SSW555'),'Repo: SSW555 Number of commits: 5', 'Should be 5')
    def test2(self):
        self.assertEqual(getRepos('austinh48','SSW567'),'Repo: SSW555 Number of commits: 22', 'Should be 22, maybe 23 once this is submitted')


if __name__ == '__main__':
    getRepos('austinh48','all')

    unittest.main(exit = True)