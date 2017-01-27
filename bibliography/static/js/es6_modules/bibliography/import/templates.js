/** a template for the BibTeX file import dialog */
export let importBibFileTemplate = _.template('<div id="importbibtex" title="' + gettext('Import a BibTex library') + '">\
        <form id="import-bib-form" method="post" enctype="multipart/form-data" class="ajax-upload">\
            <input type="file" id="bib-uploader" name="bib" required />\
            <span id="import-bib-btn" class="fw-button fw-white fw-large">' + gettext('Select a file') + '</span>\
            <label id="import-bib-name" class="ajax-upload-label"></label>\
        </form>\
    </div>')


export let searchApiTemplate = _.template('\
<div id="import-api-search" title="' + gettext("Link") + '">\
        <p><input id="text-search" class="linktitle" type="text" value="" placeholder="' + gettext("Search") + '"/></p>\
        <div id="import-api-search-result"></div>\
    </div>\
')

export let searchApiResultTemplate = _.template('\
    <%  _.each(items, function(item) {%>\
    <div class="item">\
        <h3><a class="title api-import" data-id="<%= item.id %>"><%= item.title %></a></h3>\
        <% if (item.doi) { %><p><b>DOI: <%= item.doi %></p><% } %>\
        <% if (item.description) { %><p><b>Description: </b><%= item.description %></p><% } %>\
        <button type="button" class="api-import" data-id="<%= item.id %>">Import</button>\
    </div>\
   <% })  %> \
')