jQuery(document).ready(function() {
    "use strict";
    setTimeout(function() {
        $("body").addClass("loaded")
    }, 3e3), $(window).on("load", function() {
        $('.scrolling  a[href*="#"]').on("click", function(e) {
            e.preventDefault(), e.stopPropagation();
            var o = $(this).attr("href");
            $(o).velocity("scroll", {
                duration: 800,
                offset: -50,
                easing: "easeOutExpo",
                mobileHA: !1
            })
        }), $(".body-wrapper").each(function() {
            var e = $(".header"),
                o = e.children(".navbar"),
                s = (o.find(".navbar-header"), o.find(".navbar-collapse")),
                a = {
                    nav_top: s.css("margin-top")
                };
            $(window).scroll(function() {
                o.hasClass("bb-fixed-header") && (0 === $(this).scrollTop() || $(this).width() < 750) ? (o.removeClass("bb-fixed-header").appendTo(e), s.animate({
                    "margin-top": a.nav_top
                }, {
                    duration: 100,
                    queue: !1,
                    complete: function() {
                        e.css("height", "auto")
                    }
                })) : !o.hasClass("bb-fixed-header") && $(this).width() > 750 && $(this).scrollTop() > e.offset().top + e.height() - parseInt($("html").css("margin-top"), 10) && (e.css("height", e.height()), o.css({
                    opacity: "0"
                }).addClass("bb-fixed-header"), o.appendTo($("body")).animate({
                    opacity: 1
                }), s.css({
                    "margin-top": "0px"
                }))
            })
        }), $(window).trigger("resize"), $(window).trigger("scroll")
    })
}), $(".navbar").width() > 750 && ($(".nav .dropdown").on("mouseover", function() {
    "use strict";
    $(this).addClass("show")
}), $(".nav .dropdown").on("mouseleave", function() {
    "use strict";
    $(this).removeClass("show")
})), $(".nav-category .dropdown-submenu ").hover(function() {
    "use strict";
    $(this).addClass("show")
}, function() {
    "use strict";
    $(this).removeClass("show")
}), jQuery(document).ready(function() {
    "use strict";
    $(".searchBox a").on("click", function() {
        $(".searchBox .dropdown-menu").toggleClass("display-block"), $(".searchBox a i").toggleClass("fa-close").toggleClass("fa-search")
    }), $("#searchButton").on("click", function(e) {
        e.preventDefault(), $("#searchbox").toggleClass("visibleIt")
    })
})
