import boto3

your_list = ['1.1.1.1/32','1.1.1.2/32']

client_waf = boto3.client('waf')

def get_change_token():
    return client_waf.get_change_token()['ChangeToken']


ip_update = []

for x in your_list:
    ip_loop={
            'Action': 'INSERT',
            'IPSetDescriptor': {
                'Type': 'IPV4',
                'Value': x
            }}
    ip_update.append(ip_loop)


response = client_waf.update_ip_set(
        IPSetId='',                         #add your ipset id as str
        ChangeToken=get_change_token(),
        Updates=ip_update
    )
