for $x in doc("books.xml")/catalog
return count($x/book[contains(author,"Rajati")])
