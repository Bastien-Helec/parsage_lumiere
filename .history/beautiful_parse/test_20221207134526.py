import mechanize
page  = mechanize.Page.new(URI.parse('http://example.com'), {'content-type'=>'text/html'},(page.body), 200, agent)