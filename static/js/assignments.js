$('input[type="file"]').on('change', function() {
     console.log('changed')
     $('button[type="submit"]').prop('disabled', false);
});