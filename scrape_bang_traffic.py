import re
import urllib.request
import urllib.parse

url="https://trafficindex.org/chennai/"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
pattern = r"<tr>\s*<td.*?><a.*?href='.*?'.*?>.*?</a></td>\s*<td>(.*?)</td>\s*<td><a.*?href='.*?'>(.*?)</a></td>\s*</tr>"
matches = re.findall(pattern, html)
simple_table = [[m[0].split()[-1],m[1]] for m in matches]
with open("trafficdata.csv", "w")  as out:
    for place, value in simple_table:
        out.write(f"{place},{value}\n")