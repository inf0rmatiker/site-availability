#!/bin/python3

import os
import sys
import time
import urllib.request
from urllib.error import HTTPError


def main():
    site_url = "https://radiumoxide.com"
    statistics_file = "captures.txt"
    target_file_path = "index.html"

    with open(statistics_file, "w") as f:
        f.write("time_seconds,status_code,error_reason\n")

        try:

            while True:
                     
                before = time.time()
                after  = before
                code   = 200 # Status OK
                reason = ""  # No error msg
                try:

                    response = urllib.request.urlopen(site_url)
                    html_content = response.read()
                 
                    with open(target_file_path,"wb") as fp:
                        fp.write(html_content)

                except HTTPError as e:
                    print(f"Failed to download page, code [{e.code}], reason: {e.reason}")
                    code   = e.code
                    reason = e.reason

                after  = time.time()
                difference_seconds = after - before
                f.write(f"{difference_seconds},{code},{reason}\n")
                print("Time %.3f seconds" % difference_seconds)
                
                # Remove index.html
                if os.path.isfile(target_file_path):
                    os.remove(target_file_path)

                time.sleep(1.0)

        except KeyboardInterrupt:
            print("Gracefully quitting program...")
            if os.path.isfile(target_file_path):
                os.remove(target_file_path)



if __name__ == '__main__':
    main()
