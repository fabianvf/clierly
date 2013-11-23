# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import re
import json

def parse(url):
    paragraphs = list()
    with open('rules.json') as rules:
        rules = rules.read()
        rules = json.loads(rules)
    keywords = {category: [re.compile(r) for r in rules[category]] for category in rules.keys()}

    with open("examples/github.tos") as file:
        for paragraph in file:
            paragraph = paragraph.split(". ")
            p_list = list()
            for sentence in paragraph:
                sentence = sentence.strip()
                flags = set()
                categories = set()
                for key in keywords.keys():
                    for keyword in keywords[key]:
                        if (keyword.search(sentence)):
                            flags.add(keyword.pattern)
                            categories.add(key)
                sentence = (sentence, flags, categories)            
                p_list.append(sentence)
            paragraphs.append(p_list)
    return paragraphs