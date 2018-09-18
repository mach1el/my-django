$(function () {



    // ------------------------------------------------------- //
    // Navbar Sticky
    // ------------------------------------------------------ //
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > ($('.top-bar').outerHeight())) {
            $('header.nav-holder.make-sticky').addClass('sticky');
            $('header.nav-holder.make-sticky').css('margin-bottom', '' + $('.top-bar').outerHeight() * 1.5 + 'px');
        } else {
            $('header.nav-holder.make-sticky').removeClass('sticky');
            $('header.nav-holder.make-sticky').css('margin-bottom', '0');
        }
    });

    // ------------------------------------------------------- //
    // Scroll To
    // ------------------------------------------------------ //
    $('.scroll-to').on('click', function (e) {

        e.preventDefault();
        var full_url = this.href;
        var parts = full_url.split("#");
        var target = parts[1];

        if ($('header.nav-holder').hasClass('sticky')) {
            var offset = -80;
        } else {
            var offset = -180;
        }

        var offset = $('header.nav-holder').outerHeight();

        $('body').scrollTo($('#' + target), 800, {
            offset: -offset
        });

    });


    // ------------------------------------------------------- //
    // Tooltip Initialization
    // ------------------------------------------------------ //
    $('[data-toggle="tooltip"]').tooltip();


    // ------------------------------------------------------- //
    // Product Gallery Slider
    // ------------------------------------------------------ //
    function productDetailGallery() {
        $('a.thumb').on('click', function (e) {
            e.preventDefault();
            source = $(this).attr('href');
            $('#mainImage').find('img').attr('src', source);
        });

        for (i = 0; i < 3; i++) {
            setTimeout(function () {
                $('a.thumb').eq(i).trigger('click');
            }, 300);
        }
    }

    productDetailGallery();


    // ------------------------------------------------------- //
    // Customers Slider
    // ------------------------------------------------------ //
    $(".customers").owlCarousel({
        responsiveClass: true,
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 6
            }
        }
    });


    // ------------------------------------------------------- //
    // Testimonials Slider
    // ------------------------------------------------------ //
    $(".testimonials").owlCarousel({
        items: 4,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    });


    // ------------------------------------------------------- //
    // Homepage Slider
    // ------------------------------------------------------ //
    $('.homepage').owlCarousel({
        loop: true,
        margin: 0,
        dots: true,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        addClassActive: true,
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>"
        ],
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1,
                loop: true
            }
        }
    });


    // ------------------------------------------------------- //
    // Adding fade effect to dropdowns
    // ------------------------------------------------------ //
    $('.dropdown').on('show.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).fadeIn(100);
    });
    $('.dropdown').on('hide.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).fadeOut(100);
    });


    // ------------------------------------------------------- //
    // Project Caroudel
    // ------------------------------------------------------ //
    $('.project').owlCarousel({
        loop: true,
        margin: 0,
        dots: true,
        nav: true,
        autoplay: true,
        smartSpeed: 1000,
        addClassActive: true,
        lazyload: true,
        navText: [
            "<i class='fa fa-angle-left'></i>",
            "<i class='fa fa-angle-right'></i>"
        ],
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1,
                loop: true
            }
        }
    });


    // ------------------------------------------------------- //
    // jQuery Counter Up
    // ------------------------------------------------------ //
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });


    // ------------------------------------------------------- //
    // click on the box activates the radio
    // ------------------------------------------------------ //
    $('#checkout').on('click', '.box.shipping-method, .box.payment-method', function (e) {
        var radio = $(this).find(':radio');
        radio.prop('checked', true);
    });


    // ------------------------------------------------------- //
    //  Bootstrap Select
    // ------------------------------------------------------ //
    $('.bs-select').selectpicker({
        style: 'btn-light',
        size: 4
    });


    // ------------------------------------------------------- //
    //  Shop Detail Carousel
    // ------------------------------------------------------ //
    $('.shop-detail-carousel').owlCarousel({
        items: 1,
        thumbs: true,
        nav: false,
        dots: false,
        autoplay: true,
        thumbsPrerendered: true
    });


    // ------------------------------------------------------ //
    // For demo purposes, can be deleted
    // ------------------------------------------------------ //

    var stylesheet = $('link#theme-stylesheet');
    $("<link id='new-stylesheet' rel='stylesheet'>").insertAfter(stylesheet);
    var alternateColour = $('link#new-stylesheet');

    if ($.cookie("theme_csspath")) {
        alternateColour.attr("href", $.cookie("theme_csspath"));
    }

    $("#colour").change(function () {

        if ($(this).val() !== '') {

            var theme_csspath = 'css/style.' + $(this).val() + '.css';

            alternateColour.attr("href", theme_csspath);

            $.cookie("theme_csspath", theme_csspath, {
                expires: 365,
                path: document.URL.substr(0, document.URL.lastIndexOf('/'))
            });

        }

        return false;
    });

    if ($.cookie("theme_layout")) {
        $('body').addClass($.cookie("theme_layout"));
    }

    $("#layout").change(function () {

        if ($(this).val() !== '') {

            var theme_layout = $(this).val();

            $('body').removeClass('wide');
            $('body').removeClass('boxed');

            $('body').addClass(theme_layout);

            $.cookie("theme_layout", theme_layout, {
                expires: 365,
                path: document.URL.substr(0, document.URL.lastIndexOf('/'))
            });
        }
    });

});