// пагинация //
function ajaxPagination() {
    $('.content a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('.content').empty()
                    $('.content').append($(data).find('.content').html())
                    $('html, body').animate({scrollTop: $(".content").offset().top}, 0);
                }
            })
        })
    })
}

$(document).ready(function () {
    ajaxPagination()
})

$(document).ajaxStop(function () {
    ajaxPagination()
})
// /пагинация //