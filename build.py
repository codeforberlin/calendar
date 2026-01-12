from pathlib import Path

import icalendar
import requests

url = 'https://tools.wmflabs.org/icalendar/wpb.php'

sumamry = 'OK Lab Berlin'

out_path = Path('public') / 'ok-lab-berlin.ics'
out_path.parent.mkdir(exist_ok=True)

cal = icalendar.Calendar()
cal.add('prodid', '-//OK Lab Calendar/')
cal.add('version', '2.0')

response = requests.get(url)

source = icalendar.Calendar.from_ical(response.content)
for event in source.walk('VEVENT'):
    if event.get('SUMMARY') == sumamry:
        cal.add_component(event)

with open(out_path, 'wb') as f:
    f.write(cal.to_ical())
