For HTML converter:

* Remove div styles: `div style\=\"[^<]*\">`   replace with  `div>`
* Remove font-family styles: `font-family:[\w\+\- ]+;` replace with ''
* Remove word-breaks: `\-[ \n\t\r]*\<br\>` replace with ''
* Line breaks to space: `[ \n\t\r]*\<br\>` replace with ' '
* Remove blank spans: `\<span[^>]*\>\<\/span\>` replace with ''
