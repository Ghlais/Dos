import requests

# استخدم واجهة المستخدم للحصول على العنوان IP ورقم المنفذ وقائمة البروكسيات
server_ip = input("Ip: ")
server_port = input("Port: ")

with open('proxys.txt', 'r') as file:
    proxies = file.read().splitlines()


url = f'http://{server_ip}:{server_port}'


for proxy in proxies:
    proxy_dict = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }
    
    try:
        response = requests.get(url, proxies=proxy_dict)
        if response.status_code == 200:
            print(f'The response from the proxy succeeded: {proxy}')
        else:
            print(f'Failed to respond from proxy: {proxy}')
    except Exception as e:
        print(f'An error occurred while connecting to the proxy: {proxy}')
