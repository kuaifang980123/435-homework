for $x in distinct-values(doc("books.xml")/catalog/book/author)
return <result>
<name>{$x}</name>,
<counts>{count(doc("books.xml")//book[contains(author,$x)])}</counts>
</result>