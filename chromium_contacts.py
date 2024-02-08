from operator import itemgetter

def add_names_to_contributors(contributors, list_of_names):
  for name_line in list_of_names:
    name_and_email_string = name_line.split(": ")[1]
    name_and_email_list = name_and_email_string.split('<')
    if len(name_and_email_list) > 1:
      name = name_and_email_list[0].rstrip()
      split_name = name.split(' ', maxsplit=1)
      first_name = split_name[0]
      last_name = split_name[1] if (len(split_name) > 1) else ""
      email = name_and_email_list[1].rstrip(">")
      if name in contributors:
        contributors[name]['Count'] += 1
      elif (email.find('gserviceaccount') == -1) and (email.find('metadata') == -1) and (email.find('roller') == -1):
        contact = {}
        contact['Name'] = name
        contact['First'] = first_name 
        contact['Last'] = last_name 
        contact['Email'] = email
        contact['Count'] = 1
        contributors[name] = contact 

def main():
  all_contributors = {}
  authors_file = open("authors.txt", 'r')
  authors_string = authors_file.read()
  if authors_string != "":
    add_names_to_contributors(all_contributors, authors_string.splitlines())
  reviewers_file = open("reviewers.txt", 'r')
  reviewers_string = reviewers_file.read()
  if reviewers_string != "":
    add_names_to_contributors(all_contributors, reviewers_string.splitlines())
  contributors = sorted(all_contributors.items(), key=lambda kv: kv[1]['Count'], reverse=True)
  print('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,E-mail 1 - Type,E-mail 1 - Value')
  count = 0
  for contact in contributors:
    name = contact[1]['Name']
    first_name = contact[1]['First'] 
    last_name = contact[1]['Last']
    email = contact[1]['Email']
    print(f'{name},{first_name},,{last_name},,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,* ,{email}')
    count += 1
    if count > 5000:
      break

main()