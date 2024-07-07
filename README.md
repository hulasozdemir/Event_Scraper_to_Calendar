This Python script scrapes event details from specified Meetup group URLs and generates an ICS file. Makes life easier.

The script uses BeautifulSoup to parse HTML content and extract details of events such as titles and times. It then formats this data into an .ics file format.



# Usage

Install the dependencies:

```
pip install -r requirementx.txt
```

Run the script from the command line by specifying the URL of the event page

```
python get_events.py "https://www.meetup.com/Your-Meetup-Group/events/"
```
