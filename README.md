# QA-automation-saucedemo
Automated UI testing of the SauceDemo web application using Python, Selenium WebDriver, and pytest.

This project is an automated testing suite built using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern. It covers end-to-end functional testing of the SauceDemo e-commerce website. Test coverage includes:
  Login functionality (valid/invalid credentials)
  Product listing and details
  Cart management
  Checkout workflow

**Set Up the Environment**
Prerequisites:
  Python 3.8+
  Google Chrome browser
  ChromeDriver (compatible with your Chrome version)

**STEPS**
1.Clone the Repository
  git clone https://github.com/your-username/QA-automation-saucedemo.git
  cd QA-automation-saucedemo

2.Create a Virtual Environment
  python -m venv .venv

3.Activate the Virtual Environment
  .venv\Scripts\activate

 4.Install Dependencies
   pip install -r requirements.txt

 **Run the Tests**   
 1. pytest tests/
 2. Run a specific test: pytest tests/test_login.py

**Generate the HTML Report**
1.Install the pytest-html plugin:
    pip install pytest-html
2.Run tests with the HTML report flag:
    pytest --html=reports/report.html --self-contained-html
3.To open report:
    Navigate to the reports folder
    Open report.html in any browser
    
**Explanation of Dependencies Used**

selenium : Automates browser interactions for end-to-end testing                               
pytest : Framework for writing and running test cases                                        
pytest-html : Plugin to generate HTML reports of test results                                     
webdriver-manager : Automatically handles downloading and setup of the ChromeDriver                     
pytest-order : Allows ordering of tests when execution sequence matters                            


    
  

