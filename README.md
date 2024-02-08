# ChromiumCommitters
Tools for scraping Chromium committer contact info from git logs.

This project may be used to extract names and emails from chromium commit logs. You may modify at will.

The input is two files, one with author lines from ```git log``` and one with reviewer lines. The output, to ```stdout``` is a CSV file that may be directly imported into [contacts.google.com].

The ```authors.txt``` file may be generated using this command line:
```
git log -n 1000000 | grep -E "Author\: .*\<[0-9A-Za-z]+\@[0-9A-Za-z]+\>" >
    ~/development/contact_name_scraper/authors.txt
```
and reviewers.txt using this
```
git log -n 1000000 | grep -E "Reviewed-by\: .*\<[0-9A-Za-z]+\@[0-9A-Za-z]+\>" >
    ~/development/contact_name_scraper/reviewers.txt
```
then run
```
python3 chromium_contacts.py > chromium_contacts.csv
```

The tool was originally developed to solve a problem with autocomplete in the new [issues.chromium.org] bug tracker. To enable autocomplete, import the CSV file from this tool into the contacts for the account you use with the bug tracker, then enable 3rd Party Cookies for the bug tracker (unless you happen to use a Google corporate login).
