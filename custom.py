import DAN

ServerIP = '140.113.199.199'   #=None:AutoSearch, or ='IP':Connect to this IP
Comm_interval = 2.0 # unit:second

def profile_init():
    DAN.profile['dm_name']='FSR'
    DAN.profile['d_name']=DAN.profile['dm_name']+'.'+DAN.get_mac_addr()[-4:]

def odf():  # int only
    return [
        #('Luminance', 0, 'Luminance'),
    ]

def idf():
    return [
       ('Force-I', int),
     #  ('PIN2', int),
     #  ('PIN3', str),
    ]
