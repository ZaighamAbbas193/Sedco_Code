



class methods:



    def __init__(self,driver):
        self.driver=driver

    def open_url(self,url):
        self.driver.get(url)

    def input(self,locator,input_text):
        # Define a list of locator strategies to try
        locator_strategies = ['xpath', 'id', 'name', 'class name', 'css selector', 'tag name', 'link text',
                              'partial link text']
        # Define a default locator strategy to use if none of the other strategies work
        default_locator_strategy = 'xpath'
        # reading line of code from text rider as line seperated
        # self.driver.find_element('xpath', locator).send_keys(input_text)
        for strategy in locator_strategies:
            try:
                # element_action = self.driver.find_element(strategy, locator).send_keys(input_text)
                self.driver.find_element(strategy, locator).send_keys(input_text)
                a='pass'
                # element_action.send_keys(input_text)
                break
            except:
                a='fail'
                pass
        # If none of the locator strategies work, use the default strategy
        if a=='pass':
            pass
        else:
            self.driver.find_element(default_locator_strategy, locator).send_keys(input_text)




    def click(self,locator):
        locator_strategies = ['xpath', 'id', 'name', 'class name', 'css selector', 'tag name', 'link text',
                              'partial link text']
        # Define a default locator strategy to use if none of the other strategies work
        default_locator_strategy = 'xpath'
        # reading line of code from text rider as line seperated
        # self.driver.find_element('xpath', locator).send_keys(input_text)
        for strategy in locator_strategies:
            try:
                # element_action = self.driver.find_element(strategy, locator).send_keys(input_text)
                self.driver.find_element(strategy, locator).click()
                a = 'pass'
                # element_action.send_keys(input_text)
                break
            except:
                a = 'fail'
                pass
        # If none of the locator strategies work, use the default strategy
        if a == 'pass':
            pass
        else:
            self.driver.find_element(default_locator_strategy, locator).click()




