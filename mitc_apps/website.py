# THIS IS A CUSTOM HOOK THAT REDIRECTS USERS WITH ROLE OF CUSTOMER OR HD CUSTOMER TO /ME

import frappe

def get_website_user_home_page(user):
    roles = set(frappe.get_roles(user))
    target_roles = {"Customer", "HD Customer"}

    if roles & target_roles:
        return "me"
    
    return None
