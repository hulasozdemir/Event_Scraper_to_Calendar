import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
from datetime import datetime, timedelta
from pytz import timezone
import argparse

def fetch_and_save_events(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    cal = Calendar()
    local_tz = timezone('America/Vancouver')  # Adjust timezone as needed

    for i in range(1, 10):  # Looping through 9 events as example
        base_selector = f'#event-card-e-{i} > div.flex.flex-col.space-y-5.overflow-hidden > div > div'
        title_element = soup.select_one(f'{base_selector} > span')
        time_element = soup.select_one(f'{base_selector} > time')

        if title_element and time_element:
            evt = Event()
            title = title_element.text.strip()
            datetime_str = time_element.text.strip()
            datetime_format = '%a, %b %d, %Y, %I:%M %p %Z'
            start_time = datetime.strptime(datetime_str, datetime_format)
            start_time = local_tz.localize(start_time)

            evt.add('summary', title)
            evt.add('dtstart', start_time)
            evt.add('dtend', start_time + timedelta(hours=2))
            
            cal.add_component(evt)

    with open('events.ics', 'wb') as f:
        f.write(cal.to_ical())

def main():
    parser = argparse.ArgumentParser(description='Scrape events from a given URL and save them as an ICS file.')
    parser.add_argument('url', type=str, help='The URL of the events page to scrape')
    args = parser.parse_args()

    fetch_and_save_events(args.url)

if __name__ == "__main__":
    main()
