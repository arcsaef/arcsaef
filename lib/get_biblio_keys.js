// https://www.zotero.org/support/dev/client_coding/javascript_api
// return a list of keys for the selected outputs in a Zotero pane.
// output is typically used in with a bibliography from the same Zotero pane.
var items = ZoteroPane.getSelectedItems();
var keyList = [];

for (let i = 0; i < items.length; i++) {
    keyList.push(items[i].getField('key').trim());
}

return JSON.stringify(keyList, null, 2)
