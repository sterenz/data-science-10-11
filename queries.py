################################################################################
#                                                                              #
# Queries.                                                                     #
#                                                                              #
################################################################################

from const import *
from string import Template
from query_processors import QueryProcessor
from data_model import *


#
# Publications published in year.
#
def do_query_publications_published_in_year(_generic_query_processor: QueryProcessor) -> None:

    # Define a counter to know how many item are retrieved.
    counter: int = 0

    # Define a list to collect items to print in the file.
    result_string_list: list = []

    #
    # Do the query,
    #
    res_publications_published_in_year: list[Publication] = _generic_query_processor.getPublicationsPublishedInYear(PUBLICATIONS_PUBLISHED_IN_YEAR_YEAR)

    # Build the template string.
    header_publications_published_in_year = 'Publications published in $YEAR:\n\n'
    # Pupulate the template string parameter.
    header_publications_published_in_year = Template(header_publications_published_in_year).substitute(YEAR = PUBLICATIONS_PUBLISHED_IN_YEAR_YEAR)

    # Append the header title to the list.
    result_string_list.append(header_publications_published_in_year)

    # For each publication in the list:
    for publication in res_publications_published_in_year:
        counter += 1

        publication_doi  = publication.getIds()
        publication_name = publication.getTitle()
        publication_year = publication.getPublicationYear()
        
        # Build the template string.
        result_string = '\nDoi: $DOI.\nName: $NAME.\nYear: $YEAR.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    DOI  = publication_doi,
                                                    NAME = publication_name,
                                                    YEAR = publication_year
                                                )
        
        # Append the result_string to the result list.
        result_string_list.append(result_string)
        
        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_publications_published_in_year):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/publication_published_in_year.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)
    #
    # File closed automatically.
    #

    print('-- INFO: ''Publications published in year'' Query has been processed. ', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/publication_published_in_year.txt'' ')



#
# Publications by Author id.
#
def do_publications_by_author_id(_generic_query_processor: QueryProcessor) -> None:

    # Define a counter to know how many item are retrieved.
    counter = 0
    
    # Define a list to collect items to print in the file.
    result_string_list = []
    
    #
    # Do the query.
    #
    res_publications_by_author_id = _generic_query_processor.getPublicationsByAuthorId(PUBLICATION_BY_AUTHOR_ID_AUTHOR_ID)

    # Build the template string.
    header_publications_by_author_id = 'List Publications by Author ID published in $AUTHOR_ID:\n\n'
    # Pupulate the template string parameter.
    header_publications_by_author_id = Template(header_publications_by_author_id).substitute(AUTHOR_ID = PUBLICATION_BY_AUTHOR_ID_AUTHOR_ID)

    # Append the header title to the list.
    result_string_list.append(header_publications_by_author_id)

    # For each publication in the list:
    for publication in res_publications_by_author_id:
        counter += 1

        publication_doi  = publication.getIds()
        publication_name = publication.getTitle()
        
        # Build the template string.
        result_string = '\nDoi: $DOI.\nName: $NAME.\nAuthor ORC-ID: $AUTHOR_ID.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    DOI       = publication_doi,
                                                    NAME      = publication_name,
                                                    AUTHOR_ID = PUBLICATION_BY_AUTHOR_ID_AUTHOR_ID
                                                )

        # Append the result_string to the result list.
        result_string_list.append(result_string)

        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_publications_by_author_id):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/publication_by_author_id.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Publications by author id'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/publication_by_author_id.txt'' ')



#
# Most cited Publication.
#
def do_most_cited_publication(_generic_query_processor: QueryProcessor) -> None:
   
    # Define a list to collect items to print in the file.
    result_string_list = []
    
    #
    # Do the query.
    #
    res_most_cited_publication = _generic_query_processor.getMostCitedPublication()

    # Build the template string.
    header_most_cited_publication = 'The most cited Publication is:\n\n'

    # Append the header title to the list.
    result_string_list.append(header_most_cited_publication)

    publication_doi  = res_most_cited_publication.getIds()
    publication_name = res_most_cited_publication.getTitle()

    result_string = '\nDoi: $DOI.\nName: $NAME.\n'
    # Pupulate the template string parameters.
    result_string = Template(result_string).substitute(
                                                DOI  = publication_doi,
                                                NAME = publication_name
                                            )

    # Append the result_string to the result list.
    result_string_list.append(result_string)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/most_cited_publication.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Most cited Publication'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/most_cited_publication.txt'' ')



#
# Most cited Venue.
#
def do_most_cited_venue(_generic_query_processor: QueryProcessor) -> None:

    # Define a list to collect items to print in the file.
    result_string_list = []
    
    #
    # Do the query.
    #
    res_most_cited_venue = _generic_query_processor.getMostCitedVenue()

    # Build the template string.
    header_most_cited_venue = 'The most cited Venue is:\n\n'

    # Append the header title to the list.
    result_string_list.append(header_most_cited_venue)

    venue_id   = res_most_cited_venue.getIds()
    venue_name = res_most_cited_venue.getTitle()

    result_string = '\nId: $ID.\nName: $NAME.\n'
    # Pupulate the template string parameters.
    result_string = Template(result_string).substitute(
                                                ID   = venue_id,
                                                NAME = venue_name
                                            )

    # Append the result_string to the result list.
    result_string_list.append(result_string)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/most_cited_venue.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Most cited Venue'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/most_cited_venue.txt'' ')



#
# Venues by Publisher id.
#
def do_venues_by_publisher_id(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []
    
    #
    # Do the query.
    #
    res_venues_by_publisher_id = _generic_query_processor.getVenuesByPublisherId(VENUES_BY_PUBLISHER_ID_PUBLISHER_ID)

    # Build the template string.
    header_venues_by_publisher_id = 'Venues published by Organization with id = $PUBLISHER_ID:\n\n'
    header_venues_by_publisher_id = Template(header_venues_by_publisher_id).substitute( PUBLISHER_ID = VENUES_BY_PUBLISHER_ID_PUBLISHER_ID)

    # Append the header title to the list.
    result_string_list.append(header_venues_by_publisher_id)

    # For each venue in the list:
    for venue in res_venues_by_publisher_id:
        counter += 1

        venue_id   = venue.getIds()
        venue_name = venue.getTitle()

        result_string = '\nId: $ID.\nName: $NAME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    ID   = venue_id,
                                                    NAME = venue_name
                                                )

        # Append the result_string to the result list.
        result_string_list.append(result_string)

        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_venues_by_publisher_id):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/venues_by_publisher_id.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Venues by Publisher id'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/venues_by_publisher_id.txt'' ')


#
# Publication in Venue.
#
def do_publication_in_venue(_generic_query_processor: QueryProcessor) -> None:

    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_publication_in_venue = _generic_query_processor.getPublicationInVenue(PUBLICATION_IN_VENUE_VENUE_ID)

    # Build the template string.
    header_publication_in_venue = 'Publications by Venue id = $VENUE_ID:\n\n'
    header_publication_in_venue = Template(header_publication_in_venue).substitute( VENUE_ID = PUBLICATION_IN_VENUE_VENUE_ID)

    # Append the header title to the list.
    result_string_list.append(header_publication_in_venue)

    # For each publication in the list:
    for publication in res_publication_in_venue:
        counter += 1

        publication_id   = publication.getIds()
        publication_name = publication.getTitle()

        result_string = '\nId: $ID.\nName: $NAME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    ID   = publication_id,
                                                    NAME = publication_name
                                                )

        # Append the result_string to the result list.
        result_string_list.append(result_string)

        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_publication_in_venue):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/publication_in_venue.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Publication in Venue'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/publication_in_venue.txt'' ')


#
# Journal articles in Issue.
#
def do_journal_articles_in_issue(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_journal_articles_in_issue = _generic_query_processor.getJournalArticlesInIssue(
                                                                JOURNAL_ARTICLES_IN_ISSUE_ISSUE, 
                                                                JOURNAL_ARTICLES_IN_ISSUE_VOLUME, 
                                                                JOURNAL_ARTICLES_IN_ISSUE_VENUE_ID
                                                            )

    # Build the template string.
    header_journal_articles_in_issue = 'Journal articles in Issue = $ISSUE, Volume = $VOLUME, Venue id = $VENUE_ID :\n\n'
    header_journal_articles_in_issue = Template(header_journal_articles_in_issue).substitute( 
                                                                                        ISSUE    = JOURNAL_ARTICLES_IN_ISSUE_ISSUE,
                                                                                        VOLUME   = JOURNAL_ARTICLES_IN_ISSUE_VOLUME,
                                                                                        VENUE_ID = JOURNAL_ARTICLES_IN_ISSUE_VENUE_ID
                                                                                  )

    # Append the header title to the list.
    result_string_list.append(header_journal_articles_in_issue)

    # For each journal_article in the list:
    for journal_article in res_journal_articles_in_issue:
        counter += 1

        journal_article_id     = journal_article.getIds()
        journal_article_name   = journal_article.getTitle()
        journal_article_issue  = journal_article.getIssue()
        journal_article_volume = journal_article.getVolume()

        result_string = '\nId: $ID.\nName: $NAME.\nIssue: $ISSUE.\nVolume: $VOLUME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    ID     = journal_article_id,
                                                    NAME   = journal_article_name,
                                                    ISSUE  = journal_article_issue,
                                                    VOLUME = journal_article_volume
                                                )

        # Append the result_string to the result list.
        result_string_list.append(result_string)

        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_journal_articles_in_issue):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/journal_articles_in_issue.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Journal articles in Issue'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/journal_articles_in_issue.txt'' ')



#
# Journal articles in Volume.
#
def do_journal_articles_in_volume(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_journal_articles_in_volume = _generic_query_processor.getJournalArticlesInVolume(JOURNAL_ARTICLES_IN_VOLUME_VOLUME, JOURNAL_ARTICLES_IN_VOLUME_VENUE_ID)

    # Build the template string.
    header_journal_articles_in_volume = 'Journal articles in Volume = $VOLUME, Venue id = $VENUE_ID :\n\n'
    header_journal_articles_in_volume = Template(header_journal_articles_in_volume).substitute( 
                                                                                        VOLUME   = JOURNAL_ARTICLES_IN_VOLUME_VOLUME,
                                                                                        VENUE_ID = JOURNAL_ARTICLES_IN_VOLUME_VENUE_ID
                                                                                  )

    # Append the header title to the list.
    result_string_list.append(header_journal_articles_in_volume)

    # For each journal_article in the list:
    for journal_article in res_journal_articles_in_volume:
        counter += 1

        journal_article_id     = journal_article.getIds()
        journal_article_name   = journal_article.getTitle()
        journal_article_issue  = journal_article.getIssue()
        journal_article_volume = journal_article.getVolume()

        result_string = '\nId: $ID.\nName: $NAME.\nIssue: $ISSUE.\nVolume: $VOLUME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    ID     = journal_article_id,
                                                    NAME   = journal_article_name,
                                                    ISSUE  = journal_article_issue,
                                                    VOLUME = journal_article_volume
                                                )

        # Append the result_string to the result list.
        result_string_list.append(result_string)

        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_journal_articles_in_volume):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/journal_articles_in_volume.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Journal articles in Volume'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/journal_articles_in_volume.txt'' ')



#
# Journal articles in Journal.
#
def do_journal_articles_in_journal(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_journal_articles_in_journal = _generic_query_processor.getJournalArticlesInJournal(JOURNAL_ARTICLES_IN_JOURNAL_VENUE_ID)

    # Build the template string.
    header_journal_articles_in_journal = 'Journal articles in Journal id = $VENUE_ID :\n\n'
    header_journal_articles_in_journal = Template(header_journal_articles_in_journal).substitute(VENUE_ID = JOURNAL_ARTICLES_IN_JOURNAL_VENUE_ID)

    # Append the header title to the list.
    result_string_list.append(header_journal_articles_in_journal)

    # For each journal_article in the list:
    for journal_article in res_journal_articles_in_journal:
        counter += 1

        journal_article_id     = journal_article.getIds()
        journal_article_name   = journal_article.getTitle()
        journal_article_issue  = journal_article.getIssue()
        journal_article_volume = journal_article.getVolume()

        result_string = '\nId: $ID.\nName: $NAME.\nIssue: $ISSUE.\nVolume: $VOLUME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    ID     = journal_article_id,
                                                    NAME   = journal_article_name,
                                                    ISSUE  = journal_article_issue,
                                                    VOLUME = journal_article_volume
                                                )

        # Append the result_string to the result list.
        result_string_list.append(result_string)

        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_journal_articles_in_journal):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/journal_articles_in_journal.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Journal articles in Journal'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/journal_articles_in_journal.txt'' ')



#
# Publication Authors.
#
def do_publication_authors(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_publication_authors = _generic_query_processor.getPublicationAuthors(PUBLICATION_AUTHORS_PUBLICATION_ID)

    # Build the template string.
    header_publication_authors = 'Authors of Publications with doi: $PUBLICATION_ID:\n\n'
    # Pupulate the template string parameter.
    header_publication_authors = Template(header_publication_authors).substitute(PUBLICATION_ID = PUBLICATION_AUTHORS_PUBLICATION_ID)

    # Append the header title to the list.
    result_string_list.append(header_publication_authors)
    
    # For each author in the list:
    for author in res_publication_authors:
        counter += 1
        
        author_doi         = author.getIds()
        author_name        = author.getGivenName()
        author_family_name = author.getFamilyName()
        
        # Build the template string.
        result_string = '\nDoi: $DOI.\nName: $NAME.\nFamily name: $FAMILY_NAME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    DOI         = author_doi,
                                                    NAME        = author_name,
                                                    FAMILY_NAME = author_family_name
                                                )
        
        # Append the result_string to the result list.
        result_string_list.append(result_string)
        
        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_publication_authors):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/publication_authors.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)
    #
    # File closed automatically.
    #

    print('-- INFO: ''Publication Authors'' Query has been processed. ', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/publication_authors.txt'' ')


#
# Publications by Authors name.
#
def do_publications_by_author_name(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_publications_by_author_name = _generic_query_processor.getPublicationsByAuthorName(PUBLICATIONS_BY_AUTHOR_NAME_NAME)

    # Build the template string.
    header_publications_by_author_name = 'Publications created by Author(s) with name: $AUTHOR_NAME:\n\n'
    # Pupulate the template string parameter.
    header_publications_by_author_name = Template(header_publications_by_author_name).substitute(AUTHOR_NAME = PUBLICATIONS_BY_AUTHOR_NAME_NAME)

    # Append the header title to the list.
    result_string_list.append(header_publications_by_author_name)
  
    # For each author in the list:
    for publication in res_publications_by_author_name:
        counter += 1
        
        publication_doi   = publication.getIds()
        publication_title = publication.getTitle()
        publication_year  = publication.getPublicationYear()
        
        # Build the template string.
        result_string = '\nDoi: $DOI.\nTitle: $TITLE.\nPublication Year: $YEAR.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(
                                                    DOI   = publication_doi,
                                                    TITLE = publication_title,
                                                    YEAR  = publication_year
                                                )
        
        # Append the result_string to the result list.
        result_string_list.append(result_string)
        
        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_publications_by_author_name):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/publications_by_author_name.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Publications by Authors name'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/publications_by_author_name.txt'' ')



#
# Distinct Publisher by Authors name.
#
def do_distinct_publisher_of_publications(_generic_query_processor: QueryProcessor) -> None:
    
    # Define a counter to know how many item are retrieved.
    counter = 0

    # Define a list to collect items to print in the file.
    result_string_list = []

    #
    # Do the query.
    #
    res_distinct_publisher_of_publications = _generic_query_processor.getDistinctPublisherOfPublications(DISTINCT_PUBLISHER_OF_PUBLICATIONS_PUBLICATION_ID_LIST)
    
    # Build the template string.
    header_distinct_publisher_of_publications = 'Publisher of Publication(s) with doi: $PUBLICATIONS_ID_LIST:\n\n'

    publications_ids: str = '' # Init the result string.
    counter: int = 0   # Init the counter to know where i am iterating the list.

    # For each string in the list:
    for item in DISTINCT_PUBLISHER_OF_PUBLICATIONS_PUBLICATION_ID_LIST:
        
        # Incr counter.
        counter += 1
        
        # Remove "'" apex from the string.
        item.replace("'", "")

        if counter < len(DISTINCT_PUBLISHER_OF_PUBLICATIONS_PUBLICATION_ID_LIST):

            publications_ids = item + ', '

        elif counter == len(DISTINCT_PUBLISHER_OF_PUBLICATIONS_PUBLICATION_ID_LIST):

            publications_ids = publications_ids + item


    
    # Pupulate the template string parameter.
    header_distinct_publisher_of_publications = Template(header_distinct_publisher_of_publications).substitute(PUBLICATIONS_ID_LIST = publications_ids)

    # Append the header title to the list.
    result_string_list.append(header_distinct_publisher_of_publications)
  
    # For each publisher in the list:
    for publisher in res_distinct_publisher_of_publications:
        counter += 1
        
        organization_id   = publisher.getIds()
        organization_name = publisher.getName()
        
        # Build the template string.
        result_string = '\nId: $ID.\nName: $NAME.\n'
        # Pupulate the template string parameters.
        result_string = Template(result_string).substitute(ID = organization_id, NAME = organization_name)
        
        # Append the result_string to the result list.
        result_string_list.append(result_string)
        
        # If I'm done to iterate over the list then print the number of items found.
        if counter == len(res_distinct_publisher_of_publications):

            items_found = '\nItems found: $COUNT'
            items_found = Template(items_found).substitute(COUNT = counter)
            
            result_string_list.append(items_found)

    #
    # Opens file and casts as f then, for item in the list write the file.
    #
    with open('./queries-results/distinct_publisher_of_publications.txt', 'w', encoding='utf-8') as f: 
        for string in result_string_list:
            f.write(string)

    #
    # File closed automatically.
    #

    print('-- INFO: ''Distinct Publisher by Authors name'' Query has been processed.', EMOJI_STARS, EMOJI_STARS, EMOJI_STARS)
    print('-- INFO: The result has been write in: ''./queries-results/distinct_publisher_of_publications.txt'' ')