$('.post-reply-btn').click(function(){

    var id = $(this).attr('data-id');

    var form = '#post-' + id + '-reply-wrapper';

    $(form).css({
        'display': 'block'
    });

});