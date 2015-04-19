# longform-scrape

longform.com urls have descriptive slugs (eg [http://longform.org/posts/a-fortune-at-the-top-of-the-world](http://longform.org/posts/a-fortune-at-the-top-of-the-world) but they have an implicit postid, and calls like [http://longform.org/posts/1](http://longform.org/posts/1) will redirect to the appropriate content.

As of 4/18/15, there were ~8200 posts on longform.org; this script will pull down detail (author, publication, title, date) on about 7650 of them.  The others are collections, sponsored content, or other special posts - this scraper doesn't currently process those.
