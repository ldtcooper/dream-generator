import requests
import csv
import re
import json
from typing import List, Dict, Union

post = Dict[str, Union[str, int]]
response = List[post]

class DreamScraper():
    def __init__(self, before_time=None):
        self.before_time = before_time
        self.set_url()

    def set_url(self) -> None:
        """
        Creates the URL to fetch from
        """
        url_base = 'https://api.pushshift.io/reddit/search/submission/?subreddit=dreaminterpretation&sort=desc&sort_type=created_utc&fields=selftext,created_utc&size=1000'
        before_base = '&before='
        if self.before_time != None:
            before_base += str(self.before_time)
            url_base += before_base
        self.url = url_base

    def set_before_time_from_responses(self, responses: response):
        earliest = responses[-1]
        self.before_time = earliest['created_utc']

    def make_request(self) -> List[List[str]]:
        """
        Makes a request to the API with the stored URL
        """
        print('Sending Request')
        r = requests.get(self.url)
        r.raise_for_status()
        print('Resonse Recieved')
        data = r.json()['data']
        self.set_before_time_from_responses(data)
        print('Processing Response')
        return list(map(self.process_post, data))

    def process_post(self, post: post) -> List[str]:
        """
        Formats response as a list of strings, and removes all tabs from the text
        Returns a list with a single string in it to make saving easier
        """
        text = post['selftext']
        clean_text = re.sub('\s+', ' ', text)
        return [clean_text]

    def save_debug_json(self, posts: List[str]):
        """
        Saves the list of posts as a JSON document for easy comparison to the TSV
        FOR DEBUG PURPOSES ONLY
        """
        with open('dreams.json', 'w') as file:
            file.write(json.dumps(posts))

    def write_posts(self, posts: List[List[str]]) -> None:
        """
        Saves a dict of tweets into a TSV
        """
        with open('./dreams.tsv', 'a+') as outfile:
            print('Saving Response')
            dw = csv.writer(
                outfile,
                delimiter='\t'
            )
            dw.writerows(posts)
        print('Response Saved')

    def fetch(self):
        """
        Runs requests until there are no responses left
        """
        response = self.make_request()
        while len(response) > 0:
            self.write_posts(response)
            self.set_url()
            response = self.make_request()

    def debug_run(self):
        """
        Deugging function to test making one request
        """
        response = self.make_request()
        self.write_posts(response)
        self.save_debug_json(response)
        self.set_url()

    def debug_repeated_run(self):
        """
        Debugging function to test making several requests
        """
        response = self.make_request()
        for i in range(5):
            self.write_posts(response)
            self.set_url()
            response = self.make_request()


d = DreamScraper(1584232715)
d.fetch()

