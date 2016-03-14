$('.post-reply-btn').click(function(){

    var id = $(this).attr('data-id');

    var form = '#post-' + id + '-reply-wrapper';

    $(form).css({
        'display': 'block'
    });

});

$('.post-reply-cancel-btn').click(function(){

    var id = $(this).attr('data-id');

    var form = '#post-' + id + '-reply-wrapper';

    $(form).css({
        'display': 'none'
    });

});