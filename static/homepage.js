// Collect GIPHY search and reset form.


function resetSearchForm(result) {
    // clear giphy-search-form,
    // update results-div with result

    console.dir(result);

    $('#search-field').val('');

    $('#giphy-result').attr('src', result);
    $('#results-div').show();
}

function getSearchValue(evt) {
    // prevent submit button from redirecting,
    // send data to route via post request,
    // call resetSearchForm

    evt.preventDefault();

    var formInputs = {
        'search': $('#search-field').val()
    };

    $.post('/search-giphy',
           formInputs,
           resetSearchForm
           );
}

$('#giphy-search-btn').on('click', getSearchValue);
