import feedparser
import PyRSS2Gen
import datetime

print ('Loading function')

rss_url = "http://www.dnbradio.com/feeds"
my_filter = "SHAPE"
my_rssfile = "dnbradio" + my_filter + "rss.xml"

f = open(my_rssfile, 'w')

def lambda_function (event, context):
	d = feedparser.parse( rss_url )
	print "Feed parsed: ", d['feed']['title']

# modifying entries

	d['feed']['title'] = d['feed']['title'] + " filtered for " + my_filter

	for x in d.entries:
		if my_filter in x.title:
			items = [
				PyRSS2Gen.RSSItem(
					title = x.title,
        			link = x.link,
        			description = x.summary,
        			guid = x.link
        			)
				]


# make the RSS2 object
# Try to grab the title, link, language etc from the orig feed

	rss = PyRSS2Gen.RSS2(
    	title = d['feed'].get("title"),
    	link = d['feed'].get("link"),
    	description = d['feed'].get("description"),

    	language = d['feed'].get("language"),
    	copyright = d['feed'].get("copyright"),
    	managingEditor = d['feed'].get("managingEditor"),
    	webMaster = d['feed'].get("webMaster"),
    	pubDate = d['feed'].get("pubDate"),
    	lastBuildDate = d['feed'].get("lastBuildDate"),

    	categories = d['feed'].get("categories"),
    	generator = d['feed'].get("generator"),
    	docs = d['feed'].get("docs"),

    	items = items
	)


	f.write(rss.to_xml())

	return d 

lambda_function("e", "c")
print ('Done')