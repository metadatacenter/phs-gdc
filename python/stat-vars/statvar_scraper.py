#!/usr/bin/python3

# statvar_scraper: Utility to extract the hierarchy of statistical variables from the DC website

import json
import requests
from bs4 import BeautifulSoup


def get_statvars():
    # TODO: the statistical variables page is checked-in here:
    #  "https://raw.githubusercontent.com/datacommonsorg/website/master/static/data/hierarchy_statsvar.json".
    #  Maybe read the hierarchy from this file in the future
    url = "https://docs.datacommons.org/statistical_variables.html"
    doc = requests.get(url).text
    soup = BeautifulSoup(doc, 'html.parser')
    main_content = soup.find(id="main-doc-content")

    # Generate tree
    statvars_tree = []
    for tag in main_content.contents:
        if tag.name == 'details':
            statvars_tree.append(parse_details_as_tree(tag))

    with open('dc_statvars_tree.json', 'w', encoding='utf-8') as f:
        json.dump(statvars_tree, f, indent=2)

    # Generate list
    statvars_list = []
    for tag in main_content.contents:
        if tag.name == 'details':
            parse_details_as_list(tag, statvars_list, None)

    with open('dc_statvars_list.json', 'w', encoding='utf-8') as f:
        json.dump(statvars_list, f, indent=2)


def parse_details_as_tree(details):
    node_name = details.summary.string
    node_id = node_name.lower()
    node_children = []
    if details.details:
        for tag in details.contents:
            if tag.name == 'details':
                node_children.append(parse_details_as_tree(tag))
    else:
        if details.ul:
            cont = details.ul.contents
        else:
            cont = details.contents
        for tag in cont:
            if tag.name == 'li':
                node_children.append({
                    "name": tag.a.string,
                    "id": tag.a.string.lower(),
                    "children": []
                })
    return {
        "name": node_name,
        "id": node_id,
        "children": node_children
    }


def parse_details_as_list(details, statvar_list, parent_category):
    category_name = details.summary.string
    if details.details:
        for tag in details.contents:
            if tag.name == 'details':
                parse_details_as_list(tag, statvar_list, category_name)
    else:
        if details.ul:
            cont = details.ul.contents
        else:
            cont = details.contents
        for tag in cont:
            if tag.name == 'li':
                statvar_list.append({
                    "name": tag.a.string,
                    "label": tag.a.string,
                    "category": category_name if parent_category is None else (parent_category + ' - ' + category_name)
                })


def main():
    get_statvars()
    print('Execution completed')


if __name__ == "__main__": main()
