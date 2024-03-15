GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

COMPANY_TYPE = (
    ('individual', 'Individual'),
    ('properitor', 'Properitor'),
    ('partner', 'Partner'),
    ('llp', 'LLP'),
    ('pvt_ltd', 'PVT LTD'),
    ('ltd', 'LTD'),
)

BUSINESS_TYPE = (
    ('individual', 'Individual'),
    ('business', 'Business'),
)

ADDRESS_TYPE = (
    ('shipping', 'Shipping'),
    ('billing', 'Billing'),
)


BLOOD_GROUP_CHOICES = (
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)


DIVISION_TYPE = (
    ('account center','Account center'),
    ('cost center','Cost Center'),
)

INDUSTRY_TYPE = (
    ('manufacturing','Manufacturing'),
    ('it services & consulting','It Services & Consulting'),
    ('ecommerce','E-commerce'),
    ('infrastructure','Infrastructure'),
    ('crusher & mines','Crusher & Mines'),
)

ACCOUNT_HOLDER_TYPE = (('Primary','Primary'),('Joint','Joint'))
ACCOUNT_TYPE = (('Saving','Saving'),('Current','Current'), ('Salary','Salary'), ('FixedDeposite','FixedDeposite'), ('NRI','NRI'))
