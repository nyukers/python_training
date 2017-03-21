
class GroupHelper:

    def __init__(self, app):
        self.app = app


    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.return_to_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        # fill group firm
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_fisrt_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion fisrt group
        wd.find_element_by_name("delete").click()
        self.app.return_to_page()

    def modify_fisrt_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill modification form
        self.fill_group_form(new_group_data)
        #submit modification form
        wd.find_element_by_name("update").click()
        self.app.return_to_page()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("groups").click()