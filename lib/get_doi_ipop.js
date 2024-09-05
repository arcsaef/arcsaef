// https://www.zotero.org/support/dev/client_coding/javascript_api
// return a list of doubles - DOI: ipop selected outputs in a Zotero pane.
// output is typically used in org collab analysis.
var items = ZoteroPane.getSelectedItems();
var keyList = [];

for (let i = 0; i < items.length; i++) {
    a = items[i].getField('extra').trim().search(/ipop/i)
    // reasonable assumption that ipop max length is 25 chars
    b = items[i].getField('extra').trim().slice(a, a + 25).search(/\n/i)
    if (b == -1) {
        b = items[i].getField('extra').trim().slice(a, a + 25).search(/\d$/i)
        b++
    }
    ipop = items[i].getField('extra').slice(a, a+b).replace("ipop","")
    doi  = items[i].getField('DOI').trim()
    keyList.push(doi.concat(" ", ipop ));
}
return JSON.stringify(keyList, null, 2)
