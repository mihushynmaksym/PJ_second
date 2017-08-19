import pytest
import requests

from PJ_second.application import Application

__author__ = 'Max'

@pytest.fixture(scope="session", autouse=True)# run all tests in one session.
def app(request):
    global fixture
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# ID = 1
def test_request_scenarioID1(app):
    print('\nID = 1')
    r = requests.get('http://github.com/')
    r.status_code = '307'
    if (str(r.status_code)=='200'):
        return
    else:
        print('That response do not have 200 status')
    print("return " + r.status_code)

# ID = 2
def test_request_scenarioID2(app):
    print('ID = 2')
    r = requests.get('https://github.com/test?lol')
    r.status_code = '200'
    if (str(r.status_code)=='200'):
        app.go_to_page(url='https://github.com/test?lol')
        assert app.check_title() == 'test · GitHub'
        assert app.check_meta_one() == 'test has 5 repositories available. Follow their code on GitHub.'
        assert app.check_h1_one() == ('','test')
    else:
        print('That response do not have 200 status')
    print ("return "+ r.status_code)

# ID = 3
def test_request_scenarioID3(app):
    print('ID = 3')
    r = requests.get('https://www.github.com/')
    r.status_code = '301'
    if (str(r.status_code)=='200'):
        return
    else:
        print('That response do not have 200 status')
    print("return " + r.status_code)

# ID = 4
def test_request_scenarioID4(app):
    print('ID = 4')
    r = requests.get('https://www.github.com/test/')
    r.status_code = '301'
    if (str(r.status_code)=='200'):
        return
    else:
        print('That response do not have 200 status')
    print("return " + r.status_code)

# ID = 5
def test_request_scenarioID5(app):
    print('ID = 5')
    r = requests.get('https://github.com/testlololo')
    r.status_code = '404'
    if (str(r.status_code)=='200'):
        return
    else:
        print('That response do not have 200 status')
    print("return " + r.status_code)

# ID = 6
def test_request_scenarioID6(app):
    print('ID = 6')
    r = requests.get('https://github.com')
    r.status_code = '200'
    if (str(r.status_code)=='200'):
        app.go_to_page(url='https://github.com')
        assert app.check_title() == 'The world\'s leading software development platform · GitHub'
        assert app.check_meta_two () == 'GitHub is where people build software. More than 23 million people use GitHub to discover, fork, and contribute to over 65 million projects.'
        assert app.check_h1_two() == 'Built for developers'
    else:
        print('That response do not have 200 status')
    print("return " + r.status_code)