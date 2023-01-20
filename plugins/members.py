import datetime

from pelican import signals
from pelican.contents import Article
from pelican.readers import BaseReader

def addArticle(articleGenerator):
    settings = articleGenerator.settings

    # Author, category, and tags are objects, not strings, so they need to
    # be handled using BaseReader's process_metadata() function.
    base_reader = BaseReader(settings)

    content = "I am the body of an injected article!"

    new_article = Article(content, {
        "title": "Injected Article!",
        "date": datetime.datetime.now(),
        "category": base_reader.process_metadata("category", "members"),
        "tags": base_reader.process_metadata("tags", "Jupiter"),
        "member_name": base_reader.process_metadata("member_name", "Djane Rey Mabelin"),
        "member_section": base_reader.process_metadata("member_name", "Mercury"),
        "member_address": base_reader.process_metadata("member_name", "Cebu"),
        "member_phone": base_reader.process_metadata("member_name", "00000000"),
    })

    articleGenerator.articles.insert(0, new_article)


def register():
    signals.article_generator_pretaxonomy.connect(addArticle)