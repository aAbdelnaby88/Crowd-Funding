$(document).on('submit', '#searchForm', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: 'search/',
        data: {
            searchBox: $('.searchBox').val()
        },
        sucess: function() {
            alert('loading...')
        }
    });
});