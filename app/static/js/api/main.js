// = JSON.stringify({login: "admin", password: "P@ssword123", domain: "http://192.168.111.74:3718"})
$ ().ready ( function () {


    const url = location.protocol + "//" + location.host;


    // $ ( '.end' ).css ( 'display', 'flex' )
    //     .hide ();

    if ($.cookie ( 'api_key' ) != null) {
        console.log ( $.cookie ( 'api_key' ) );
        console.log ( 'hhhh' );
    } else {
        console.log ( $.cookie ( 'api_key' ) );
        window.location.href = '../';
    }
    $ ( '#user' ).html ( $.cookie ( ('name') ) );

    get_info ( 'projects' );
    // get_info ( 'projects', 1 );

    $ ( '.send_statistics' ).on ( 'click', function () {


        let s = JSON.stringify ( {
            key: $.cookie ( 'api_key' ),
            domain: url_red
        } );
        $.ajax ( {
            url: url + '/api/send_mess/',
            type: 'POST',
            data: s,
            dataType: "text",
            success: function (data) {
                if (data === 'success') {
                    // $ ( '.end' )
                    //     .addClass ( 'alert-success' )
                    //     .show ( 400 )
                    //     .html ( 'отправлено' );
                    // setTimeout ( function () {
                    //     $ ( '.end' ).hide ( 100 );
                    // }, 3000 );
                    console.log ( 'норм всё' )
                } else {
                    // $ ( '.end' )
                    //     .addClass ( 'alert-danger' )
                    //     .show ( 400 )
                    //     .html ( 'не отправлено' );
                    // setTimeout ( function () {
                    //     $ ( '.end' ).hide ( 100 );
                    // }, 3000 );
                    console.log ( 'норм не всё' )
                }
            }
        } );
    } );

    // $ ( '.alert' ).on ( 'click', function () {
    //     $ ( '.end' ).hide ();
    // } );
    $ ( '.exit' ).on ( 'click', function () {
        $.removeCookie ( 'api_key', {path: '/'} );
        window.location.href = '../';
    } )

} );